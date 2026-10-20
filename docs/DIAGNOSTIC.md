# Read-only CMU diagnostic (v0.3)

This is a **manual**, **read-only** script. It does not install anything, remount partitions, run a recovery binary, alter XML, reboot, or access the Android Auto protocol.

## Purpose

Identify whether OEM Android Auto services and known HUD preload libraries are present on the Mazda Connect 74.00.324 family. The aftermarket P3.1 USB hub and the green pre-facelift HUD are **not** guaranteed compatible, even if these services exist.

## Running

Only if you already have authorized shell access to your CMU, while parked with stable power:

```sh
sh diagnostic/inspect-cmu.sh /tmp/mazda-hud-diagnostic.txt
cat /tmp/mazda-hud-diagnostic.txt
```

The report is sanitized to firmware family, service names, and presence flags. Read it before sharing. Do **not** send raw `sm.conf`, serials, VIN, MAC, passwords, Wi-Fi keys, or unredacted logs.

### No shell access?

**Do not jailbreak or install a diagnostic USB autorun just for this check.** The prior AIO USB was used to remove conflicting Android Auto Headunit App tweaks; its presence does not confirm current command-line access. A diagnostic USB method needs separate compatibility review.

## Interpret

- `jciAAPA` / `aap_service` present: OEM components exist, but navigation events may not be delivered by the aftermarket hub.
- `libpatch-*` referenced: potentially active third-party preload; resolve conflicts before any install.
- `jcinavi` present: not proof of navigation SD-card availability.
- For Yandex Navigator, Google Maps, Waze, etc., actual app support requires **protocol capture and parked hardware testing**. An app name in a sample is not proof.

See [SAFETY.md](SAFETY.md).
