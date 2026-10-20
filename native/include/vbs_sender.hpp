#pragma once
#include "vbs_transport.hpp"
namespace mazda_hud {
// Real CMU bus connection is intentionally not part of this interface.
// An implementation must verify the OEM destination/path/interface at runtime.
class VbsBus {
public:
    virtual ~VbsBus() {}
    virtual bool send_display(const VbsDisplayRequest& request) = 0;
};
class VbsSender {
public:
    explicit VbsSender(VbsBus& bus) : bus_(bus) {}
    // Fail-closed: only enabled by an explicit opt-in after vehicle validation.
    bool send(const Guidance& event, uint32_t verified_glyph,
              bool hardware_validated, bool enable_send);
private:
    VbsBus& bus_;
};
}
