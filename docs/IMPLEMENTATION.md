# Implementation boundaries

## Android Auto acquisition

`oem-aa-mod` injects into OEM `jciAAPA` and optionally `aap_service`. Its `libpatch-blmjciaapa.so` handles legacy AA navigation callbacks and its optional `libpatch-aap_service.so` handles GAL 1.6 frames. The exact transport from aftermarket P3.1 hardware to OEM services must be validated on this vehicle.

## HUD output

Upstream supports `svcnavi` with OEM navigation SD card (single-writer pathway) and `vbs` without SD (direct `com.jci.vbs.navi`, potential conflict). The green HUD's available message types and glyphs remain unknown. Implement a capability whitelist after parked hardware tests.

## Adapter contract

`normalize(payload, profile)` handles only validated synthetic events. It is **not** a parser for the Android Auto wire protocol. A future native C/C++ adapter should consume decoded nav events and emit typed maneuver, distance and supported road/lane fields.

## Installation strategy (future)

Prefer a reversible, diff-only installer with validation of each destination and a transaction log. Never restore entire upstream `sm.conf` backups over user-modified files. Ship compiled binary only after target-hardware testing, preserve AGPL notices, and document boot-time recovery.
