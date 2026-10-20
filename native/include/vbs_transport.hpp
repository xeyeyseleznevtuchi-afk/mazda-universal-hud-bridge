#pragma once
#include <cstdint>
#include "hud_bridge.hpp"

namespace mazda_hud {
// Staging representation of SetHUDDisplayMsgReq observed on the Mazda VBS bus.
// This is NOT a D-Bus sender and does not claim a verified icon mapping.
struct VbsDisplayRequest {
    uint32_t direction_glyph; // OEM-specific numeric glyph; caller must supply a validated mapping
    uint16_t distance;
    uint8_t distance_unit; // observed: 1=m, 2=mi, 3=km, 4=yd, 5=ft
    uint16_t reserved;
    uint8_t reserved_byte;
    uint8_t sync;
};

// Generic bridge to transport staging. Reject unsupported/ambiguous input.
// Passing a numeric glyph is intentional: Turn enum values are NOT Mazda glyph IDs.
bool stage_vbs(const Guidance& guidance, uint32_t verified_glyph,
               VbsDisplayRequest& output);
}
