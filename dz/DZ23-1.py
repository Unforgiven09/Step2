import logging
import unittest
from DZ23 import *

logging.basicConfig(level=logging.WARNING,
                    filename="logs23.log",
                    filemode='w',
                    format="We have some error: %(asctime)s : %(levelname)s : %(name)s : %(message)s")


class TestCalculator(unittest.TestCase):
    def test_zero_args(self):
        try:
            self.assertEqual(Calculator.count(), 0)
        except Exception as ex:
            logger = logging.getLogger('test_zero_args')
            logger.error(ex)

    def test_one_arg(self):
        try:
            self.assertEqual(Calculator.count(1), 1)
        except Exception as ex:
            logger = logging.getLogger('test_one_arg')
            logger.error(ex)

    def test_more_args(self):
        try:
            self.assertEqual(Calculator.count(1, 2, 3), 0)
        except Exception as ex:
            logger = logging.getLogger('test_more_args')
            logger.error(ex)

    def test_wrong_kwargs0(self):
        try:
            self.assertEqual(Calculator.count(1, 2), 0)
        except Exception as ex:
            logger = logging.getLogger('test_wrong_kwargs0')
            logger.error(ex)

    def test_wrong_kwargs2(self):
        try:
            self.assertEqual(Calculator.count(1, 2, a='+', v='/'), 0)
        except Exception as ex:
            logger = logging.getLogger('test_wrong_kwargs2')
            logger.error(ex)

    def test_wrong_kwargs1(self):
        try:
            self.assertEqual(Calculator.count(1, 2, a='a'), 0)
        except Exception as ex:
            logger = logging.getLogger('test_wrong_kwargs1')
            logger.error(ex)

    def test_sum(self):
        try:
            self.assertEqual(Calculator.count(1, 2, a='+'), 3)
        except Exception as ex:
            logger = logging.getLogger('test_sum')
            logger.error(ex)

    def test_division(self):
        try:
            self.assertEqual(Calculator.count(1, 0, a='/'), -1)
        except Exception as ex:
            logger = logging.getLogger('test_division')
            logger.error(ex)
