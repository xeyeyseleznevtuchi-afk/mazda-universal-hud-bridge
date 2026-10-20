# Upstream toolkit evaluation — 2026-10-20

## Source material

- https://github.com/ilshyma/mazda-hud-toolkit
- https://github.com/ilshyma/mazda-hud-toolkit/releases
- https://github.com/KidMixer/mazda-carplay-hud
- https://github.com/VitaliyKurokhtin/oem-aa-mod

A third-party Mazda owner reported installing via the Toolkit website. This is **not** evidence of compatibility with the project's CX-3 test car.

## What the toolkit supplies

The toolkit packages a CarPlay-specific shim and an installer/user interface for Mazda CMU150 74.00.324; its tested example is a 2018 EU CX-9. Its releases also document USB root/SSH access, checksum verification, automatic post-reboot validation and rollback. The tool's current installation path may still use commands, SSH and privileged changes; a friendly menu does **not** prove a no-command USB installation is universal.

KidMixer's CarPlay patch has an OEM VBS_NAVI transport using `libjcidbus`, an existing `hud_send` implementation and a USB DataRetrieval installer described in `install/INSTALL.md`. Its `LD_PRELOAD` target is `jciCARPLAY`; the Android Auto path uses different shims (`jciAAPA` / `aap_service`) in oem-aa-mod.

## Reuse decision

1. Keep Android Auto and CarPlay capture as **separate adapters**.
2. Investigate a **shared VBS_NAVI sender** using KidMixer's original sources and their AGPL-3.0 attribution; do not reimplement undocumented D-Bus endpoints from guesses.
3. Build a unified installer that checks the firmware and OEM service profile; stage changes transactionally, preserve unrelated `LD_PRELOAD` values, and do not restore entire `sm.conf` / `sm_WCP.conf` over user changes.
4. Use USB DataRetrieval if it can be made verifiably reversible and compatible with the target. Do not require SSH as the only installation option.
5. Validate wired and wireless mode separately. Never assume green pre-facelift ADD is compatible with a color HUD implementation.
6. Require proof of actual emitted AA guidance events (especially Yandex Navigator) before advertising app compatibility.

## First test vehicle

2015 Japan-market CX-3, EU 74.00.324A, green flip-up HUD, aftermarket wireless Android Auto USB hub. A Japanese navigation SD card is present but rejected by the EU firmware. This rules out treating a physically inserted SD card as evidence that OEM navigation operates.

No actual OEM VBS sender or installable artifact is delivered by this documentation commit. Native `VbsSender` remains a guarded mock interface.
