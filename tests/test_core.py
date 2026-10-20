import unittest
from hud_core import normalize, simplify_street
class HudTests(unittest.TestCase):
    def test_yandex_green(self):
        self.assertEqual(normalize({'app':'Yandex Navigator','maneuver':'right','distance_m':270}),{'active':True,'icon':'RIGHT','distance_m':270})
    def test_extended(self):
        x=normalize({'maneuver':'left','distance_m':15,'lanes':[1,0]},'extended_hud')
        self.assertEqual(x['lanes'],[1,0])
    def test_unknown(self):
        with self.assertRaises(ValueError):normalize({'maneuver':'teleport','distance_m':20})
    def test_stopped(self):
        self.assertEqual(normalize({'active':False}),{'active':False})
    def test_negative(self):
        with self.assertRaises(ValueError):normalize({'maneuver':'right','distance_m':-3})
    def test_russian_street(self):
        self.assertEqual(simplify_street('улица Ленина'), 'ulitsa Lenina')
    def test_russian_street(self):
        self.assertEqual(simplify_street('улица Ленина'), 'ulitsa Lenina')
    def test_ascii(self):
        self.assertTrue(all(ord(x)<128 for x in simplify_street('улица Ленина')))
if __name__=='__main__': unittest.main()
