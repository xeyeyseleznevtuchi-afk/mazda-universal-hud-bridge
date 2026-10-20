# VBS transport staging (offline)

The experimental `native/vbs_transport` layer models the
`SetHUDDisplayMsgReq` request described in community D-Bus logs.
It is deliberately a staging function, **not** a real D-Bus or OEM-library
transport and **not** a deployable car modification.

Observed fields include a numeric directional glyph, distance, unit and
synchronization byte. The actual glyph mapping and extra fields remain
unverified on this vehicle; thus `stage_vbs` requires the caller to supply
a separately confirmed nonzero OEM glyph. Never substitute the internal
`Turn` enum ordinal.

Known limitations:
- Does not send any VBS messages.
- Rejects distances above 65535 m rather than truncating.
- Does not implement unit conversion or road text (Msg2).
- The green HUD still requires parked hardware tests.
- Japanese navigation SD showing 'invalid card' is not a prerequisite
  for this development path.

See https://github.com/VitaliyKurokhtin/oem-aa-mod
and https://gist.github.com/patrikguth/ae37a207e0044ef372cbfb7a1e9379a6

Build and run offline only.
