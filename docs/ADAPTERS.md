# Source adapters — offline interface (v0.4)

`nav_adapters.py` translates **already-decoded** Android Auto and Apple CarPlay
navigation events into the existing canonical HUD event schema.

Android Auto inputs: `turn_event` (hu.proto enum), `turn_side` (1 left,
2 right, 3 unspecified), `distance_m`, optional `road`, `lanes`, `app`.
Apple inputs: `maneuver_type` (iAP2), `distance_m`, optional `road`, `app`.

Currently mapped AA event IDs: 3, 4, 5, 6, 9, 10, 14, 19. Apple IDs: 11, 12.
Unrecognized mappings raise an exception instead of emitting a wrong arrow.
The small mapping tables are provisional and need parked-car validation.

References:
- [oem-aa-mod](https://github.com/VitaliyKurokhtin/oem-aa-mod) — GAL navigation decoding and OEM Android Auto hooks
- [mazda-carplay-hud](https://github.com/KidMixer/mazda-carplay-hud) — iAP2 decoder and OEM HUD transport

**Not implemented:** direct wire decoding, OEM hooks, injection, head-unit
writing, capability probing, app-specific protocol compatibility, and USB
installation. No upstream binary or AGPL source has been vendored.

The green display gets maneuver and distance only until hardware tests
establish its supported HUD glyph and text capabilities. Adapter support for
a *synthetic* Yandex event does **not** prove that Yandex or the aftermarket
wireless hub sends the necessary messages on real hardware.
