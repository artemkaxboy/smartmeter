"""Platform for sensor integration."""
from __future__ import annotations

import logging
from typing import Any

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, SENSORS

_LOGGER = logging.getLogger(__name__)


def format_entity_id(sensor_key: str) -> str:
    """Format sensor key to a proper entity ID with underscores."""
    import re
    
    # Special handling for keys with existing underscores (like PowerDelivered_l1)
    if "_l" in sensor_key.lower():
        # Split by existing underscore
        parts = sensor_key.split("_")
        base = parts[0]
        suffix = "_" + "_".join(parts[1:]).lower()
        # Add underscores between camelCase in base part
        base = re.sub(r'(?<!^)(?=[A-Z])', '_', base).lower()
        return base + suffix
    
    # Handle Tariff1, Tariff2 -> tariff_1, tariff_2
    result = re.sub(r'Tariff(\d)', r'Tariff_\1', sensor_key)
    
    # Convert camelCase to snake_case
    result = re.sub(r'(?<!^)(?=[A-Z])', '_', result).lower()
    
    return result


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Smart Meter sensors from a config entry."""
    coordinator = hass.data[DOMAIN][config_entry.entry_id]

    # Create sensors for all available data points
    sensors = []
    
    # Get initial data to determine which sensors to create
    if coordinator.data:
        for key, sensor_config in SENSORS.items():
            if key in coordinator.data:
                sensors.append(
                    SmartMeterSensor(
                        coordinator,
                        config_entry,
                        key,
                        sensor_config,
                    )
                )
    
    async_add_entities(sensors, update_before_add=True)


class SmartMeterSensor(CoordinatorEntity, SensorEntity):
    """Representation of a Smart Meter sensor."""

    def __init__(self, coordinator, config_entry, sensor_key, sensor_config):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._config_entry = config_entry
        self._sensor_key = sensor_key
        self._sensor_config = sensor_config
        
        # Format the sensor key for entity ID
        formatted_key = format_entity_id(sensor_key)
        
        # Set unique ID and entity ID
        mac = coordinator.data.get("mac_address", "unknown").replace("_", "").replace(":", "").lower()
        self._attr_unique_id = f"{mac}_{formatted_key}"
        self.entity_id = f"sensor.smartmeter_{formatted_key}"
        
        # Set name
        self._attr_name = sensor_config["name"]
        
        # Set icon
        if sensor_config.get("icon"):
            self._attr_icon = sensor_config["icon"]
        
        # Set device class
        if sensor_config.get("device_class"):
            self._attr_device_class = sensor_config["device_class"]
        
        # Set state class
        if sensor_config.get("state_class"):
            self._attr_state_class = sensor_config["state_class"]
        
        # Set unit of measurement
        if sensor_config.get("unit"):
            self._attr_unit_of_measurement = sensor_config["unit"]
            self._attr_native_unit_of_measurement = sensor_config["unit"]

    @property
    def device_info(self) -> DeviceInfo:
        """Return device information."""
        return DeviceInfo(
            identifiers={(DOMAIN, self.coordinator.data.get("mac_address", "unknown"))},
            name="Smart Meter Gateway",
            manufacturer="Connectix",
            model=self.coordinator.data.get("gateway_model", "Smart Meter Gateway"),
            sw_version=self.coordinator.data.get("firmware_running"),
            configuration_url=f"http://{self.coordinator.host}:{self.coordinator.port}",
        )

    @property
    def native_value(self) -> Any:
        """Return the state of the sensor."""
        value = self.coordinator.data.get(self._sensor_key)
        
        # Try to convert numeric values
        if value is not None and self._sensor_config.get("unit"):
            try:
                return float(value)
            except (ValueError, TypeError):
                pass
        
        return value

    @property
    def available(self) -> bool:
        """Return if entity is available."""
        return self.coordinator.last_update_success and self._sensor_key in self.coordinator.data

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        """Return extra state attributes."""
        attributes = {}
        
        # Add some extra metadata if this is the main energy sensor
        if self._sensor_key == "EnergyDeliveredTariff1":
            attributes["equipment_id"] = self.coordinator.data.get("Equipment_Id")
            attributes["gas_equipment_id"] = self.coordinator.data.get("GasEquipment_Id")
            attributes["startup_time"] = self.coordinator.data.get("startup_time")
            attributes["mqtt_configured"] = self.coordinator.data.get("mqtt_configured")
            attributes["mqtt_server"] = self.coordinator.data.get("mqtt_server")
        
        return attributes
