#pragma once
#include <cstdint>

namespace mazda_hud {

enum class Turn : uint8_t {
    Unknown, Left, Right, SlightLeft, SlightRight,
    Straight, UTurn, MergeLeft, MergeRight, Destination
};

enum class Display : uint8_t {
    Green, Extended
};

struct Guidance {
    Turn turn;
    int32_t distance_m;
    bool active;
};

struct Frame {
    Turn turn;
    int32_t distance_m;
    bool show_road;
    bool show_lanes;
};

bool map_aa(uint32_t event, uint32_t side,
            int32_t distance_m, Guidance& out);

bool map_carplay(uint32_t maneuver,
                 int32_t distance_m, Guidance& out);

bool render(const Guidance& guidance,
            Display display, Frame& out);

}
