# VBS sending boundary

Current status: **mockable interface only; no production Mazda D-Bus sender**.

`VbsSender` accepts a validated guidance event and an OEM glyph supplied by
a future vehicle-specific capability mapping. It refuses to send unless both
`hardware_validated` and `enable_send` are true. Unit tests verify that an
unvalidated call does not reach the mock bus.

The independent reference trace documents:
- method `SetHUDDisplayMsgReq` sent to `com.jci.vbs.navi`
- struct field types: `uint32, uint16, byte, uint16, byte, byte`
- optional street method `SetHUD_Display_Msg2`.

Reference: https://gist.github.com/patrikguth/ae37a207e0044ef372cbfb7a1e9379a6

**Not yet verified:** D-Bus service path, interface, bus selection, call
semantics, glyph mapping, timeouts, on-device ABI, HUD behavior.
Do not infer these from the method name. The generic interface cannot safely
send on the real car until those are proven. A future backend should default
to disabled even after compiling.

Use `cmake -S native -B build/native && cmake --build build/native &&
ctest --test-dir build/native --output-on-failure` on a computer.

Note: upstream documentation says its `svcjcinavi` merge shim is useful
with the OEM navigation SD present. A card rejected as invalid is not evidence
that OEM navigation service is usable. Direct VBS remains an experimental path.
