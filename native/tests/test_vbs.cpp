#include "vbs_transport.hpp"
#include <cassert>
using namespace mazda_hud;
int main() {
 Guidance guidance{Turn::Right, 270, true};
 VbsDisplayRequest r{0,0,0,0,0,0};
 assert(!stage_vbs(guidance, 0, r)); // Unknown glyph mapping must not be guessed
 assert(stage_vbs(guidance, 3, r)); // 3 is merely a test-supplied placeholder
 assert(r.direction_glyph == 3 && r.distance == 270 && r.distance_unit == 1);
 assert(!stage_vbs(Guidance{Turn::Left, 65536, true}, 1, r));
 assert(!stage_vbs(Guidance{Turn::Left, -1, true}, 1, r));
 assert(!stage_vbs(Guidance{Turn::Left, 20, false}, 1, r));
 assert(!stage_vbs(Guidance{Turn::Unknown, 20, true}, 1, r));
 return 0;
}
