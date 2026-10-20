#include "hud_bridge.hpp"
#include <cassert>

using namespace mazda_hud;

int main() {
    Guidance g{Turn::Unknown, 0, false};
    Frame f{Turn::Unknown, 0, false, false};

    assert(map_aa(4, 1, 270, g));
    assert(g.turn == Turn::Left);
    assert(g.distance_m == 270);

    assert(render(g, Display::Green, f));
    assert(!f.show_road);
    assert(!f.show_lanes);

    assert(render(g, Display::Extended, f));
    assert(f.show_road);
    assert(f.show_lanes);

    assert(map_carplay(12, 80, g));
    assert(g.turn == Turn::Right);

    assert(!map_aa(999, 1, 10, g));
    assert(!map_carplay(56, 10, g));
    assert(!map_aa(4, 1, -1, g));

    return 0;
}
