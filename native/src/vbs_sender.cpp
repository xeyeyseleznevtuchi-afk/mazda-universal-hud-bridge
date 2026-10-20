#include "vbs_sender.hpp"
namespace mazda_hud {
bool VbsSender::send(const Guidance& event, uint32_t glyph,
                     bool hardware_validated, bool enable_send) {
    if (!hardware_validated || !enable_send) return false;
    VbsDisplayRequest staged = {0, 0, 0, 0, 0, 0};
    if (!stage_vbs(event, glyph, staged)) return false;
    return bus_.send_display(staged);
}
}
