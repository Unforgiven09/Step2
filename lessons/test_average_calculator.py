import logging
import unittest

from average_calculator import *

logging.basicConfig(level=logging.DEBUG,
                    filename="logs.log",
                    filemode='w',
                    format=f"test {__name__}:%(asctime)s:%(levelname)s - %(message)s")


class TestAverageCalculator(unittest.TestCase):
    def test_empty(self):
        logging.info(self.assertEqual(calculate_average(), None))

    def test_solo(self):
        logging.info(self.assertEqual(calculate_average(3), 3))

    def test_basic(self):
        logging.info(self.assertEqual(calculate_average(1, 2, 3), 2))

    def test_neg(self):
        logging.info(self.assertEqual(calculate_average(-1, -2, 3), 0))
