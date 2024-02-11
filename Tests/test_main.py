from unittest import TestCase
from Kalkulacka.kalkulacka import Kalkulacka


class TestKalkulacka(TestCase):

    def test_secti(self):
        k = Kalkulacka()
        self.assertEqual(10, k.secti(4, 6))


    def test_odecti(self):
        k = Kalkulacka()
        self.assertEqual(2, k.odecti(6, 4))

    def test_vynasob(self):
        k = Kalkulacka()
        self.assertEqual(50, k.vynasob(10, 5))

    def test_vydel(self):
        k = Kalkulacka()
        self.assertEqual(0, k.vydel(0, 10))
