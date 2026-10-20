# Connect 2 Style — interface research and implementation track

## Verified open-source references

- https://github.com/Trevelopment/MZD-AIO — theme installer and UI-related tweaks.
- https://github.com/bencroskery/MZD-THEMES — author says themes use `background.png` plus a custom `jci` directory, and warns some assets must be copied into `copy_to_usb/config/jci` manually.
- https://github.com/bencroskery/MZD-WEB — browser preview tooling for Mazda Connect UI.

Do not assume these public repositories contain the entire OEM interface or are safe on firmware 74.00.324A.

## Target

- Mazda CX-3 DK 2015, CMU150 `74.00.324A-EU`.
- OEM display approximately 800×480 as a **prototype canvas**, pending actual display bounds verification.
- Retain stock controller behavior, rear camera, parking aids, settings, Android Auto with Yandex, and installed third-party HUD shims.
- Implement a coherent Connect 2-inspired identity without copying proprietary graphical assets.

## Deliverables

1. **Browser-only exploratory UI** (no CMU permissions or live car APIs). First prototype: main launcher, focus states, media state, rotary keyboard simulation.
2. Document asset mapping against public theme formats: `background.png`, selective `jci` assets; never presume an arbitrary custom HTML page can run as the OEM shell.
3. Only after source mapping, create a minimal **style-only** patch from checked, explicit file paths with per-file preimages and reversible restoration.
4. Keep all firmware checks fail-closed; do not change `eq 70` to `eq 74` to bypass compatibility.

## Safety / constraints

Current working HUD mod uses service `LD_PRELOAD` lines; no theme installer may touch `sm.conf`, `sm_WCP.conf`, `aap_system_attributes*.xml`, or `/data_persist/oem-aa-mod`.

The browser concept is **not** a ready-to-install firmware theme.
