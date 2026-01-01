"""Config flow for Smart Meter integration."""
from __future__ import annotations

import logging
from typing import Any

import aiohttp
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.const import CONF_HOST, CONF_PORT
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResult
from homeassistant.exceptions import HomeAssistantError
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .const import DOMAIN, DEFAULT_PORT, API_ENDPOINT

_LOGGER = logging.getLogger(__name__)

STEP_USER_DATA_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_HOST): str,
        vol.Required(CONF_PORT, default=DEFAULT_PORT): int,
    }
)


class SmartMeterHub:
    """Smart Meter Hub for validation."""

    def __init__(self, host: str, port: int, session: aiohttp.ClientSession) -> None:
        """Initialize."""
        self.host = host
        self.port = port
        self.session = session

    async def test_connection(self) -> dict[str, Any]:
        """Test if we can connect to the Smart Meter."""
        url = f"http://{self.host}:{self.port}{API_ENDPOINT}"
        
        try:
            async with self.session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as response:
                if response.status != 200:
                    raise CannotConnect(f"HTTP {response.status}")
                
                data = await response.json()
                
                # Check if we have required fields
                if "mac_address" not in data:
                    raise InvalidData("Missing mac_address in response")
                
                return data
                
        except aiohttp.ClientError as err:
            _LOGGER.error("Error connecting to Smart Meter at %s: %s", url, err)
            raise CannotConnect(f"Connection error: {err}") from err
        except Exception as err:
            _LOGGER.error("Unexpected error: %s", err)
            raise CannotConnect(f"Unexpected error: {err}") from err


async def validate_input(hass: HomeAssistant, data: dict[str, Any]) -> dict[str, Any]:
    """Validate the user input allows us to connect."""
    session = async_get_clientsession(hass)
    hub = SmartMeterHub(data[CONF_HOST], data[CONF_PORT], session)

    device_data = await hub.test_connection()

    # Return info that you want to store in the config entry
    return {
        "title": f"Smart Meter ({device_data.get('mac_address', 'Unknown')})",
        "mac_address": device_data.get("mac_address"),
        "model": device_data.get("gateway_model"),
    }


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Smart Meter."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the initial step."""
        errors: dict[str, str] = {}
        
        if user_input is not None:
            try:
                info = await validate_input(self.hass, user_input)
                
                # Set unique ID based on MAC address
                if info.get("mac_address"):
                    await self.async_set_unique_id(info["mac_address"])
                    self._abort_if_unique_id_configured()
                
                return self.async_create_entry(
                    title=info["title"],
                    data=user_input,
                )
            except CannotConnect:
                errors["base"] = "cannot_connect"
            except InvalidData:
                errors["base"] = "invalid_data"
            except Exception:  # pylint: disable=broad-except
                _LOGGER.exception("Unexpected exception")
                errors["base"] = "unknown"

        return self.async_show_form(
            step_id="user",
            data_schema=STEP_USER_DATA_SCHEMA,
            errors=errors,
        )


class CannotConnect(HomeAssistantError):
    """Error to indicate we cannot connect."""


class InvalidData(HomeAssistantError):
    """Error to indicate we received invalid data."""
