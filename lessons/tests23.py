import unittest
from LES23 import div_nums


class DivTest(unittest.TestCase):
    def test_args(self):
        self.assertEqual(div_nums(2, 3, div=5), 1)

    def test_kwargs(self):
        self.assertEqual(div_nums(a=2, c=3, div=5, d=5), 2)

    def test_mix(self):
        self.assertEqual(div_nums(3, '2', 'BOB', a=2, c=3, div=5, d=5), 3)