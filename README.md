# Mazda Universal HUD Bridge

[![Offline tests](https://img.shields.io/badge/tests-offline_only-yellow)](#testing)

Open research and simulator for routing Android Auto navigation events to Mazda Active Driving Display (HUD). **Not an installable vehicle modification yet.**

## Target

- Mazda Connect 1 firmware **74.00.324A** (device-reported; installer checks upstream firmware family `74.00.324`).
- 2015 Mazda CX-3 pre-facelift with **green monochrome HUD**.
- Aftermarket wireless USB module **ET-1594 / TK78-66-9U0C Ver.P3.1**, transport not yet verified.
- Preferred app **Yandex Navigator**; also Yandex Maps, Google Maps, Waze and any navigation app that emits appropriate Android Auto guidance messages.

**Compatibility is determined by the Android Auto navigation protocol and hardware routing, not by the app name.** A Yandex example in this repository is synthetic test data, not evidence of successful transfer from Yandex Navigator to Mazda HUD.

## Why not simply port the CarPlay patch?

[KidMixer/mazda-carplay-hud](https://github.com/KidMixer/mazda-carplay-hud) decodes Apple's iAP2 inside `jciCARPLAY`. Android Auto instead provides guidance via `jciAAPA` and `aap_service`. [VitaliyKurokhtin/oem-aa-mod](https://github.com/VitaliyKurokhtin/oem-aa-mod) already has Android Auto HUD implementations (GAL 1.5, optional GAL 1.6), so this project treats that as the reference implementation rather than copying Apple-specific decoder logic.

## What works now

- Application-independent normalization of synthetic guidance events.
- Offline Android Auto GAL and CarPlay iAP2 **decoded-event adapters** with explicit maneuver whitelists; [details](docs/ADAPTERS.md).
- Conservative profile for green HUD (`turn`, `distance`) and experimental extended profile (`road`, `lanes`).
- Offline Python test suite; no real CMU access required.
- Safety and hardware-compatibility documentation; no blind modification of existing tweaks.

## What is **not** implemented

- Reading live Android Auto / CarPlay protocol traffic from the aftermarket hub (the new adapters receive decoded dictionaries, not protocol bytes).
- Writing frames to the factory HUD from this Python project.
- Binary `LD_PRELOAD` patches, flashed firmware, USB installer or uninstall script.
- Verified compatibility with the pre-facelift green HUD and Yandex Navigator on P3.1.

## Device inspection (v0.3)

A **read-only**, manually run CMU diagnostic is available at [diagnostic/inspect-cmu.sh](diagnostic/inspect-cmu.sh). It produces a sanitized report of service availability and potential conflicts. See [DIAGNOSTIC.md](docs/DIAGNOSTIC.md). It is not a USB installer, and it must not be run without authorized device shell access.

## Testing

```bash
python3 -m unittest discover -s tests -v
python3 simulate.py examples/yandex.json
```

## Architecture

```text
Android navigation app (Yandex / Google / Waze / ...)
  -> Android Auto on smartphone
  -> P3.1 aftermarket hub [TRANSPORT TO VERIFY]
  -> Mazda OEM aap_service / jciAAPA [TO VERIFY]
  -> OEM protocol decoder [NOT YET IMPLEMENTED HERE]
  -> decoded-event adapter (nav_adapters.py) [OFFLINE]
  -> canonical event schema (hud_core.py) [OFFLINE]
  -> capability-aware HUD renderer [NOT YET IMPLEMENTED]
  -> Mazda OEM HUD protocol / green HUD [HARDWARE TEST NEEDED]
```

Read [COMPATIBILITY.md](docs/COMPATIBILITY.md), [SAFETY.md](docs/SAFETY.md), and [IMPLEMENTATION.md](docs/IMPLEMENTATION.md) before working with a vehicle. Please open a sanitized [device report](.github/ISSUE_TEMPLATE/device-report.yml) for new hardware confirmations.

## Attribution / license

Copyright 2026 project contributors. This research project uses **AGPL-3.0-or-later** for collaboration with the AGPL Mazda community code. The current Python examples are newly authored here; upstream source code has **not** been copied into this archive. Before distributing compiled derivatives of other projects, retain upstream copyright notices and comply with their licenses. See [CREDITS.md](CREDITS.md).
