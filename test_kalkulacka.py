import unittest
from main import Kalkulacka


class test_kalkulacky(unittest.TestCase):
    def test_scitani(self):
        calc = Kalkulacka()
        self.assertEqual(6, calc.secti(3, 3))
        self.assertEqual(-2, calc.secti(4, -6))

    def test_nasobeni(self):
        calc = Kalkulacka()
        self.assertEqual(21, calc.vynasob(3, 7))
