import unittest
from nav_adapters import from_android_auto, from_carplay

class AdapterTests(unittest.TestCase):
    def test_android_yandex_left(self):
        self.assertEqual(from_android_auto({"app":"Yandex Navigator","turn_event":4,"turn_side":1,"distance_m":180}),
                         {"active":True,"icon":"LEFT","distance_m":180})
    def test_android_google_right(self):
        self.assertEqual(from_android_auto({"app":"Google Maps","turn_event":4,"turn_side":2,"distance_m":75})["icon"],"RIGHT")
    def test_apple_right(self):
        self.assertEqual(from_carplay({"maneuver_type":12,"distance_m":100})["icon"],"RIGHT")
    def test_unknown_aa_rejected(self):
        with self.assertRaises(ValueError):
            from_android_auto({"turn_event":13,"distance_m":10})
    def test_unknown_apple_rejected(self):
        with self.assertRaises(ValueError):
            from_carplay({"maneuver_type":56,"distance_m":30})
    def test_invalid_distance_rejected(self):
        with self.assertRaises(ValueError):
            from_carplay({"maneuver_type":11,"distance_m":-1})
    def test_extended_road(self):
        result=from_android_auto({"turn_event":4,"turn_side":2,"distance_m":90,"road":"улица Ленина"}, "extended_hud")
        self.assertEqual(result["road_fallback"],"ulitsa Lenina")

if __name__ == "__main__":
    unittest.main()
