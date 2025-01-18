import logging
import unittest
from DZ23 import *

logging.basicConfig(level=logging.WARNING,
                    filename="logs23-1.log",
                    filemode='w',
                    format="We have some error: %(asctime)s : %(levelname)s : %(name)s : %(message)s")


class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        try:
            self.assertEqual(factorial(5), 120)
        except Exception as ex:
            logger = logging.getLogger('test_factorial')
            logger.error(ex)

    def test_factorial_0(self):
        try:
            self.assertEqual(factorial(0), 1)
        except Exception as ex:
            logger = logging.getLogger('test_factorial')
            logger.error(ex)

    def test_factorial_less_0(self):
        try:
            self.assertEqual(factorial(-5), 120)
        except Exception as ex:
            logger = logging.getLogger('test_factorial_less_0')
            logger.error(ex)

    def test_factorial_float(self):
        try:
            self.assertEqual(factorial(5.0), 120)
        except Exception as ex:
            logger = logging.getLogger('test_factorial_float')
            logger.error(ex)

    def test_factorial_str(self):
        try:
            self.assertEqual(factorial('5'), 120)
        except Exception as ex:
            logger = logging.getLogger('test_factorial_float')
            logger.error(ex)
