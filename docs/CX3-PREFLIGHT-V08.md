# CX-3 USB preflight v0.8 — sanitized findings

Observed on the first volunteer test vehicle (2015 CX-3 DK, green flip-up HUD, firmware family 74.00.324 EU):

- USB DataRetrieval launcher completed and returned report.
- Both `sm.conf` and `sm_WCP.conf` readable.
- `jciCARPLAY`, `jciAAPA`, `jcinavi`, and `aap_service` declared in both configurations.
- No `LD_PRELOAD` lines found by the diagnostic grep.
- Four expected `/data_persist/oem-aa-mod` shim files absent.
- Both Android Auto attribute XMLs flagged `possibly_enabled_manual_review`. This is a broad text heuristic and does **not** establish that their navigation subscriptions are enabled or that Android Auto sends guidance.
- Green HUD protocol, Yandex navigation events, and VBS endpoint were not tested.
- Diagnostic decision: no installation permitted.

## Next gate

1. Fix XML subscription detection to scope to the actual `navigation` block instead of searching for any nearby `TRUE`.
2. Check active service configuration selection (get_board_type.sh) read-only.
3. Validate a known VBS receiver path/interface against upstream source before native bus injection.
4. Capture evidence of one AA navigation event without logging personal locations/route content.
5. Verify boot-recovery and rollback strategy before distributing any boot-time modification.

These are coarse diagnostic observations, not vehicle compatibility certification. Do not include private system configurations in public issues.
