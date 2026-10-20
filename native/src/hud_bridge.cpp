#include "hud_bridge.hpp"

namespace mazda_hud {

static bool valid_distance(int32_t d) {
    return d >= 0 && d <= 2000000;
}

bool map_aa(uint32_t event, uint32_t side,
            int32_t distance_m, Guidance& out) {

    if (!valid_distance(distance_m) || side < 1 || side > 3)
        return false;

    Turn turn = Turn::Unknown;

    switch (event) {
        case 3:
            turn = side == 1 ? Turn::SlightLeft :
                   side == 2 ? Turn::SlightRight : Turn::Straight;
            break;
        case 4:
        case 5:
        case 9:
            turn = side == 1 ? Turn::Left :
                   side == 2 ? Turn::Right : Turn::Straight;
            break;
        case 6:
            turn = Turn::UTurn;
            break;
        case 10:
            turn = side == 1 ? Turn::MergeLeft :
                   side == 2 ? Turn::MergeRight : Turn::Straight;
            break;
        case 14:
            turn = Turn::Straight;
            break;
        case 19:
            turn = Turn::Destination;
            break;
        default:
            return false;
    }

    out = {turn, distance_m, true};
    return true;
}

bool map_carplay(uint32_t maneuver,
                 int32_t distance_m, Guidance& out) {

    if (!valid_distance(distance_m))
        return false;

    if (maneuver != 11 && maneuver != 12)
        return false;

    out = {
        maneuver == 11 ? Turn::Left : Turn::Right,
        distance_m,
        true
    };

    return true;
}

bool render(const Guidance& guidance,
            Display display, Frame& out) {

    if (!guidance.active ||
        guidance.turn == Turn::Unknown ||
        !valid_distance(guidance.distance_m))
        return false;

    bool extended = display == Display::Extended;

    out = {
        guidance.turn,
        guidance.distance_m,
        extended,
        extended
    };

    return true;
}

}
