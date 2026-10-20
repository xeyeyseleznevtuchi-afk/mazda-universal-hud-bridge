# Mazda Universal HUD Bridge — Native Core

Experimental C++11 navigation-event adapter.

Supports offline conversion of selected decoded
Android Auto and Apple CarPlay maneuver types.

Display profiles:
- Green: maneuver and distance
- Extended: capability flags for future HUD testing

This is NOT a vehicle installer.

Not yet implemented:
- Live Android Auto / CarPlay protocol decoding
- OEM Mazda HUD transport
- Device-specific capability detection
- USB installation and rollback

Reference implementations:
https://github.com/VitaliyKurokhtin/oem-aa-mod
https://github.com/KidMixer/mazda-carplay-hud
