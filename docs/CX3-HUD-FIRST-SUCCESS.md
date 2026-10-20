# First real HUD output observed — 2026-10-20

After preparing USB with third-party Mazda HUD Toolkit v2.4.1, the CX-3 owner shared a photo showing:
- Android Auto navigation on the central CMU screen;
- green flip-up HUD displaying a left-turn arrow and approximately 160 m remaining;
- speed 0 km/h (vehicle stationary).

**Confirmed:** the 2015 CX-3 green HUD can physically display a navigation maneuver while the Toolkit modification is in use. This materially advances the compatibility evidence beyond offline simulations.

**Not yet confirmed:** exact navigation app emitting the event (Yandex vs Maps), expected arrows for multiple maneuver types, sustained operation in wireless AA, CarPlay, OEM speed-limit functionality, or clean rollback.

Next diagnostic steps (vehicle parked except for actual road verification by passenger):
1. Record app name, wireless/wired AA connection, and whether music/audio still works.
2. Verify route changes cause corresponding HUD changes.
3. Retrieve USB Toolkit status/logs from `hud-mod/logs/` if available; strip personal route coordinates and other private data before public upload.
4. Avoid reinstalling or uninstalling while working; use passive verification.
