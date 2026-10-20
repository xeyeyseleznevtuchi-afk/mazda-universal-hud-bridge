# Upstream Mazda Toolkit evaluation (corrected 2026-10-20)

Source: https://mazda-toolkit.monodev.org/
Repository link previously assessed: https://github.com/ilshyma/mazda-hud-toolkit

## Correction: the toolkit supports BOTH Android Auto and CarPlay

The upstream website explicitly advertises:
- CarPlay + Android Auto HUD maneuver arrows, distance and speed.
- USB-only on-screen installation, verification and rollback, with optional SSH tooling for advanced work.
- Mazda CX-3 DK 2015–2022 among supported EU CMU150 firmware 74.00.324 vehicles.
- An integrated build based on KidMixer/mazda-carplay-hud and VitaliyKurokhtin/oem-aa-mod.
- A km/h fix and a speed-limit keep-alive helper for supported systems.
- Four installed shims checked in the on-screen validation tool.

These are **developer claims**, not an independent test on our 2015 CX-3,
74.00.324A-EU with green flip-up HUD and ET-1594 wireless hub.
The third-party owner's installation report is not a test on our vehicle.
The website's categorical claim that the mod 'cannot brick' is NOT a safety
guarantee, especially where boot-time service configurations change.

## Consequences for Universal HUD Bridge

Do not reinvent a native VBS transmitter or an Android Auto decoding hook
without reviewing the integrated upstream implementation, its license,
install/rollback paths and firmware compatibility checks.

Before modifying the test car:
1. Audit Toolkit source/release hashes and installation/removal behavior.
2. Audit preservation of existing service configurations and other tweaks.
3. Verify pre-facelift GREEN HUD support, not merely Mazda CX-3 model name.
4. Check AA events from Yandex Navigator (not just Google Maps).
5. Check OEM wireless module coexistence, no loss of working AA/audio.
6. Offer dry-run diagnostics and reversible rollback prior to installation.

Our existing Python/C++ adapters and fake-bus VBS interface remain research
components and do not constitute a functioning alternative to the Toolkit.
