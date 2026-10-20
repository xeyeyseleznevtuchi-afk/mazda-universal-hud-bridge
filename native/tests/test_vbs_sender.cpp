#include "vbs_sender.hpp"
#include <cassert>
using namespace mazda_hud;
class FakeBus : public VbsBus {
public:
    int calls = 0;
    bool send_display(const VbsDisplayRequest& req) override {
        ++calls;
        return req.direction_glyph == 42 && req.distance == 270;
    }
};
int main() {
    FakeBus bus;
    VbsSender sender(bus);
    Guidance event = {Turn::Right, 270, true};
    assert(!sender.send(event, 42, false, true));
    assert(!sender.send(event, 42, true, false));
    assert(!sender.send(event, 0, true, true));
    assert(bus.calls == 0);
    assert(sender.send(event, 42, true, true));
    assert(bus.calls == 1);
    return 0;
}
