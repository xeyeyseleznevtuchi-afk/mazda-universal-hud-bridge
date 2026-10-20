"""Offline adapters for *decoded* guidance data, not wire-protocol decoders.

These functions never communicate with a Mazda CMU. Callers must first decode
Android Auto GAL or Apple iAP2 messages using a verified transport adapter.
"""
from hud_core import normalize

AA_EVENTS = {
    3: ("slight_left", "slight_right", "straight"),
    4: ("left", "right", "straight"),
    5: ("left", "right", "straight"),
    6: ("uturn", "uturn", "uturn"),
    9: ("left", "right", "straight"),
    10: ("merge_left", "merge_right", "straight"),
    14: ("straight", "straight", "straight"),
    19: ("destination", "destination", "destination"),
}
# Apple maneuver types verified in KidMixer documentation. These examples are
# deliberately narrow: unmapped types must not be guessed.
CARPLAY_EVENTS = {11: "left", 12: "right"}
AA_SIDES = {1: 0, 2: 1, 3: 2}

def from_android_auto(decoded: dict, profile: str = "green_prefacelift") -> dict:
    """Normalize a decoded AA turn + distance pair (not raw GAL bytes)."""
    event = int(decoded["turn_event"])
    side = int(decoded.get("turn_side", 3))
    if event not in AA_EVENTS or side not in AA_SIDES:
        raise ValueError("Unmapped Android Auto maneuver/side")
    return normalize({
        "app": decoded.get("app", "unknown"),
        "maneuver": AA_EVENTS[event][AA_SIDES[side]],
        "distance_m": decoded["distance_m"],
        "road": decoded.get("road", ""),
        "lanes": decoded.get("lanes", []),
        "active": decoded.get("active", True),
    }, profile)

def from_carplay(decoded: dict, profile: str = "green_prefacelift") -> dict:
    """Normalize a decoded iAP2 maneuver + distance pair (not raw iAP2)."""
    event = int(decoded["maneuver_type"])
    if event not in CARPLAY_EVENTS:
        raise ValueError("Unmapped Apple maneuver type")
    return normalize({
        "app": decoded.get("app", "unknown"),
        "maneuver": CARPLAY_EVENTS[event],
        "distance_m": decoded["distance_m"],
        "road": decoded.get("road", ""),
        "active": decoded.get("active", True),
    }, profile)
