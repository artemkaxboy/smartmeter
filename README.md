# Smart Meter Integration for Home Assistant

Custom integration for Smart Meter Gateway by Connectix for Home Assistant.

## Icon

The integration includes a custom icon that will be displayed in the Home Assistant integrations list.

## Features

This integration provides sensors for:
- **Energy consumption** (Tariff 1 & 2)
- **Energy return** (solar panels, Tariff 1 & 2)
- **Current power usage** (total and per phase L1, L2, L3)
- **Voltage monitoring** (per phase)
- **Current monitoring** (per phase)
- **Gas consumption** (total and hourly)
- **Network status** (WiFi RSSI)
- **Device information** (firmware version, update availability)

## Installation

### HACS (Recommended)

1. Add this repository to HACS as a custom repository:
   - Open HACS
   - Go to "Integrations"
   - Click the three dots in the top right corner
   - Select "Custom repositories"
   - Add repository URL: `https://github.com/artemkaxboy/smartmeter`
   - Category: Integration
   
2. Install the integration through HACS
3. Restart Home Assistant

### Manual Installation

1. Copy the `smartmeter` folder to your `custom_components` directory
2. Restart Home Assistant

## Configuration

1. Go to **Settings** → **Devices & Services**
2. Click **Add Integration**
3. Search for "Smart Meter"
4. Enter your Smart Meter gateway details:
   - **Host**: IP address or hostname of your Smart Meter gateway
   - **Port**: Port number (default: 82)

## Energy Dashboard

To use the energy sensors in Home Assistant's Energy Dashboard:

1. Go to **Settings** → **Dashboards** → **Energy**
2. Configure:
   - **Grid consumption**: Select `sensor.smartmeter_energydeliveredtariff1` and `sensor.smartmeter_energydeliveredtariff2`
   - **Return to grid**: Select `sensor.smartmeter_energyreturnedtariff1` and `sensor.smartmeter_energyreturnedtariff2`
   - **Gas consumption**: Select `sensor.smartmeter_gasdelivered`

## Sensors

The integration creates the following sensors:

### Energy Sensors
- `sensor.smartmeter_energydeliveredtariff1` - Energy consumed (Tariff 1)
- `sensor.smartmeter_energydeliveredtariff2` - Energy consumed (Tariff 2)
- `sensor.smartmeter_energyreturnedtariff1` - Energy returned (Tariff 1)
- `sensor.smartmeter_energyreturnedtariff2` - Energy returned (Tariff 2)

### Power Sensors
- `sensor.smartmeter_powerdelivered_total` - Current total power usage (kW)
- `sensor.smartmeter_powerreturned_total` - Current total power return (kW)
- `sensor.smartmeter_powerdelivered_l1` - Power usage Phase 1 (W)
- `sensor.smartmeter_powerdelivered_l2` - Power usage Phase 2 (W)
- `sensor.smartmeter_powerdelivered_l3` - Power usage Phase 3 (W)
- `sensor.smartmeter_powerdeliverednetto` - Netto power usage (W)

### Voltage & Current Sensors
- `sensor.smartmeter_voltage_l1` - Voltage Phase 1 (V)
- `sensor.smartmeter_voltage_l2` - Voltage Phase 2 (V)
- `sensor.smartmeter_voltage_l3` - Voltage Phase 3 (V)
- `sensor.smartmeter_current_l1` - Current Phase 1 (A)
- `sensor.smartmeter_current_l2` - Current Phase 2 (A)
- `sensor.smartmeter_current_l3` - Current Phase 3 (A)

### Gas Sensors
- `sensor.smartmeter_gasdelivered` - Total gas consumption (m³)
- `sensor.smartmeter_gasdeliveredhour` - Hourly gas consumption (m³)

### Device Status
- `sensor.smartmeter_electricitytariff` - Current electricity tariff
- `sensor.smartmeter_wifi_rssi` - WiFi signal strength (dBm)
- `sensor.smartmeter_firmware_running` - Current firmware version
- `sensor.smartmeter_firmware_update_available` - Firmware update availability

## Troubleshooting

### Connection Issues
- Verify the Smart Meter gateway is accessible: `curl http://<your-host>:<port>/smartmeter/api/read`
- Check that the host and port are correct
- Ensure Home Assistant can reach the Smart Meter gateway on your network

### Missing Sensors
- Some sensors may not appear if the Smart Meter doesn't provide that data
- Check the Smart Meter gateway's web interface for available data

## Author

Created by [@artemkaxboy](https://github.com/artemkaxboy)

## License

This integration is provided as-is for personal use.
