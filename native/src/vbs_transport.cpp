#include "vbs_transport.hpp"
namespace mazda_hud {
bool stage_vbs(const Guidance& guidance, uint32_t verified_glyph,
               VbsDisplayRequest& output) {
    if (!guidance.active || guidance.turn == Turn::Unknown ||
        guidance.distance_m < 0 || guidance.distance_m > 65535 ||
        verified_glyph == 0) return false;
    const VbsDisplayRequest staged = {
        verified_glyph, static_cast<uint16_t>(guidance.distance_m),
        1, 0, 0, 1
    };
    output = staged;
    return true;
}
}
