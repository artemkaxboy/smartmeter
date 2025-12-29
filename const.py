"""Constants for the Smart Meter integration."""
from datetime import timedelta

DOMAIN = "smartmeter"
DEFAULT_PORT = 82
DEFAULT_NAME = "Smart Meter"
DEFAULT_SCAN_INTERVAL = timedelta(seconds=30)

CONF_HOST = "host"
CONF_PORT = "port"

# API endpoint
API_ENDPOINT = "/smartmeter/api/read"

# Sensor definitions with units and device classes
SENSORS = {
    "EnergyDeliveredTariff1": {
        "name": "Energy Delivered Tariff 1",
        "unit": "kWh",
        "device_class": "energy",
        "state_class": "total_increasing",
        "icon": "mdi:lightning-bolt",
    },
    "EnergyDeliveredTariff2": {
        "name": "Energy Delivered Tariff 2",
        "unit": "kWh",
        "device_class": "energy",
        "state_class": "total_increasing",
        "icon": "mdi:lightning-bolt",
    },
    "EnergyReturnedTariff1": {
        "name": "Energy Returned Tariff 1",
        "unit": "kWh",
        "device_class": "energy",
        "state_class": "total_increasing",
        "icon": "mdi:solar-power",
    },
    "EnergyReturnedTariff2": {
        "name": "Energy Returned Tariff 2",
        "unit": "kWh",
        "device_class": "energy",
        "state_class": "total_increasing",
        "icon": "mdi:solar-power",
    },
    "PowerDelivered_total": {
        "name": "Power Delivered Total",
        "unit": "kW",
        "device_class": "power",
        "state_class": "measurement",
        "icon": "mdi:flash",
    },
    "PowerReturned_total": {
        "name": "Power Returned Total",
        "unit": "kW",
        "device_class": "power",
        "state_class": "measurement",
        "icon": "mdi:solar-power-variant",
    },
    "PowerDelivered_l1": {
        "name": "Power Delivered L1",
        "unit": "W",
        "device_class": "power",
        "state_class": "measurement",
        "icon": "mdi:flash",
    },
    "PowerDelivered_l2": {
        "name": "Power Delivered L2",
        "unit": "W",
        "device_class": "power",
        "state_class": "measurement",
        "icon": "mdi:flash",
    },
    "PowerDelivered_l3": {
        "name": "Power Delivered L3",
        "unit": "W",
        "device_class": "power",
        "state_class": "measurement",
        "icon": "mdi:flash",
    },
    "PowerReturned_l1": {
        "name": "Power Returned L1",
        "unit": "W",
        "device_class": "power",
        "state_class": "measurement",
        "icon": "mdi:solar-power-variant",
    },
    "PowerReturned_l2": {
        "name": "Power Returned L2",
        "unit": "W",
        "device_class": "power",
        "state_class": "measurement",
        "icon": "mdi:solar-power-variant",
    },
    "PowerReturned_l3": {
        "name": "Power Returned L3",
        "unit": "W",
        "device_class": "power",
        "state_class": "measurement",
        "icon": "mdi:solar-power-variant",
    },
    "Voltage_l1": {
        "name": "Voltage L1",
        "unit": "V",
        "device_class": "voltage",
        "state_class": "measurement",
        "icon": "mdi:sine-wave",
    },
    "Voltage_l2": {
        "name": "Voltage L2",
        "unit": "V",
        "device_class": "voltage",
        "state_class": "measurement",
        "icon": "mdi:sine-wave",
    },
    "Voltage_l3": {
        "name": "Voltage L3",
        "unit": "V",
        "device_class": "voltage",
        "state_class": "measurement",
        "icon": "mdi:sine-wave",
    },
    "Current_l1": {
        "name": "Current L1",
        "unit": "A",
        "device_class": "current",
        "state_class": "measurement",
        "icon": "mdi:current-ac",
    },
    "Current_l2": {
        "name": "Current L2",
        "unit": "A",
        "device_class": "current",
        "state_class": "measurement",
        "icon": "mdi:current-ac",
    },
    "Current_l3": {
        "name": "Current L3",
        "unit": "A",
        "device_class": "current",
        "state_class": "measurement",
        "icon": "mdi:current-ac",
    },
    "GasDelivered": {
        "name": "Gas Delivered Total",
        "unit": "m³",
        "device_class": "gas",
        "state_class": "total_increasing",
        "icon": "mdi:fire",
    },
    "GasDeliveredHour": {
        "name": "Gas Delivered Hour",
        "unit": "m³",
        "device_class": "gas",
        "state_class": "measurement",
        "icon": "mdi:fire",
    },
    "PowerDeliveredHour": {
        "name": "Power Delivered Hour",
        "unit": "kWh",
        "device_class": "energy",
        "state_class": "measurement",
        "icon": "mdi:lightning-bolt",
    },
    "PowerDeliveredNetto": {
        "name": "Power Delivered Netto",
        "unit": "W",
        "device_class": "power",
        "state_class": "measurement",
        "icon": "mdi:flash",
    },
    "ElectricityTariff": {
        "name": "Electricity Tariff",
        "unit": None,
        "device_class": None,
        "state_class": None,
        "icon": "mdi:cash",
    },
    "wifi_rssi": {
        "name": "WiFi RSSI",
        "unit": "dBm",
        "device_class": "signal_strength",
        "state_class": "measurement",
        "icon": "mdi:wifi",
    },
    "firmware_running": {
        "name": "Firmware Version",
        "unit": None,
        "device_class": None,
        "state_class": None,
        "icon": "mdi:chip",
    },
    "firmware_update_available": {
        "name": "Firmware Update Available",
        "unit": None,
        "device_class": None,
        "state_class": None,
        "icon": "mdi:update",
    },
}
