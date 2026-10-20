# Mazda HUD Toolkit source audit — 2026-10-20

Audited upstream:
- https://github.com/ilshyma/mazda-hud-toolkit/blob/main/toolkit.sh
- https://github.com/ilshyma/mazda-hud-toolkit/blob/main/files/unified/install.sh
- https://github.com/ilshyma/mazda-hud-toolkit/blob/main/files/unified/uninstall.sh
- https://github.com/ilshyma/mazda-hud-toolkit/blob/main/files/unified/usb_run.sh
- https://github.com/ilshyma/mazda-hud-toolkit/blob/main/files/usb_unlock/tweaks.sh

Source was reviewed at the publicly readable main branch; this is static code review, not a functional or security proof.

## Confirmed

1. The unified release is v2.4.1 in files/unified/VERSION. Ships four shims: CarPlay, AA / jciAAPA, AA v1.6 / aap_service, and svcjcinavi.
2. The USB path is real. toolkit.sh prepares a FAT32 stick with XSS and CVE-2024-8359 .up filename injection triggers. usb_run.sh exposes install/uninstall/status with on-screen dialogs and optional USB logs.
3. install.sh checks for firmware substring 74.00.324 but does **not stop** on mismatch; it logs a warning and continues.
4. install.sh checks only the active sm config for foreign preloads after stripping libpatch lines. Then it strips recognized libpatch preloads from **both** sm.conf and sm_WCP.conf, inserts the new set only in the selected active config and writes both files.
5. config patching is multi-step, not a transaction: failures after writing service configuration or DLL files can leave partial installation. Backups are created under /data_persist/hud-mod-backup but are NOT restored transactionally by uninstall.
6. uninstall.sh removes all recognized 'libpatch-' preload entries in both configs, resets jciCARPLAY reset_board=no to yes, forces NaviSupported=FALSE and deletes /data_persist/oem-aa-mod wholesale, rather than undoing only its exact own changes. It may remove an independently installed oem-aa-mod or older carplay patch.
7. install.sh overwrites /etc/aap_system_attributes*.xml **if referenced certificate paths exist**; backups saved once and optionally copied from preexisting *.orig. A later update to those files could be lost on removal.
8. The optional speed-limit feature requires working OEM navigation for actual native limit input; the installer itself notes it may have arrows without speed limit if no SD navigation engine is running.
9. usb_run.sh status reports four processes and shim mappings, not proof that a particular navigation app sends live events or that a pre-facelift green HUD can render them.
10. The installer claims 'cannot brick', but modifying service startup configuration still has recovery risk. Treat marketing claim as unverified.

## Compatibility conclusions for the project's first device

- 2015 Japan-market CX-3 with EU firmware 74.00.324A and green flip-up HUD: model and firmware family appear within *claimed* matrix, but old green HUD functionality untested.
- ET-1594 / TK78-66-9U0C aftermarket wireless hub: not tested by this review.
- Japanese SD navigation card is rejected as invalid on EU firmware: stock nav speed-limit stream cannot be assumed to work.
- Yandex Navigator: upstream AA patch exists, but no verified live Yandex maneuver events were observed.

## Recommendations for our universal project

- Do not deploy the upstream toolkit blindly to the first test vehicle.
- Add strict version / board / service / shim hash preflights that **fail closed**.
- Replace bulk preload stripping and wholesale directory deletion with owned-line/file manifests and compare-before-edit cleanup.
- Use per-run backups, per-file integrity hashes, a persistent transaction journal, and rollback on partial failure.
- Preserve existing third-party modifications and both sm configs even if only one is active; no unconditional NaviSupported reset.
- Offer genuinely read-only dry run and diagnostics before any boot-time patch.
- Separate 'AA event received', 'HUD bus accepted', and 'HUD physically displayed' in verification.
- Test installed mode only parked with stable power and a complete recovery plan.

This document includes no personal configuration content.
