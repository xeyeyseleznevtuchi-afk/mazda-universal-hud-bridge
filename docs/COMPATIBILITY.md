# Compatibility matrix

| Component | Status | Evidence needed |
|---|---|---|
| Mazda Connect 1 / 74.00.324A | Reported by owner | Firmware identifier and process list, redacted |
| CX-3 pre-facelift green HUD | Reported by owner | Supported glyph codes / OEM message acceptance |
| Chinese P3.1 wireless AA hub | Reported by owner | Whether AA guidance passes through OEM `aap_service` and `jciAAPA` |
| Yandex Navigator via Android Auto | Unverified | Non-sensitive proof of guidance frames, then parked HUD verification |
| Yandex Maps via Android Auto | Unverified | Same |
| Google Maps via Android Auto | Unverified | Same |
| Waze via Android Auto | Unverified | Same |
| GAL 1.5 | Upstream implementation exists | Device routing + compatibility |
| GAL 1.6, lane guidance | Upstream implementation exists | Hub negotiation and HUD glyph support |

Do not infer green HUD support from newer CX-5/CX-8 color HUD results. Do not infer Russian/Cyrillic street-label rendering from OEM HUD symbol names.
