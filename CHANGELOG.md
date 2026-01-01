# Changelog

All notable changes to the Smart Meter integration will be documented in this file.

## [1.1.0] - 2025-01-01

### Changed
- **Improved sensor entity IDs** - Now using more readable snake_case format with proper underscores:
  - `energydeliveredtariff1` → `energy_delivered_tariff_1`
  - `energydeliveredtariff2` → `energy_delivered_tariff_2`
  - `powerdelivered_l1` → `power_delivered_l1`
  - `gasdeliveredhour` → `gas_delivered_hour`
  - And all other sensors follow the same pattern

### Fixed
- Fixed icons display in HACS and Home Assistant
- Added logo in multiple locations for better compatibility

### Added
- Issue tracker link in manifest.json
- Better icon support with multiple resolutions

## [1.0.0] - 2024-12-30

### Added
- Initial release
- Support for Smart Meter Gateway by Connectix
- Energy monitoring (consumption and return)
- Power monitoring (total and per phase)
- Voltage and current monitoring per phase
- Gas consumption monitoring
- WiFi signal strength sensor
- Firmware version and update status
- UI configuration flow
- Automatic sensor discovery
- Icons for integration and sensors
