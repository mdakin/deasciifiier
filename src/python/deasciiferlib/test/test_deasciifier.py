 # coding=UTF-8
import logging
import unittest
from hamcrest import *

from deasciiferlib.deasciifier import Deasciifier
from deasciiferlib.deasciifier import logger as deasciifier_logger

test_logger = logging.getLogger('Deasciifier')

class SimpleTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super(SimpleTest, cls).setUpClass()
        cls.deasciifier = Deasciifier()


    def setUp(self):
        logging.basicConfig(level=logging.INFO)
        deasciifier_logger.setLevel(logging.INFO)
        test_logger.setLevel(logging.INFO)

    # IMPORTANT NOTE from Ali Ok!
    # IMPORTANT NOTE from Ali Ok!
    # Original code doesn't works problematic when there is no space around words. Last char is never checked!
    # IMPORTANT NOTE from Ali Ok!
    # IMPORTANT NOTE from Ali Ok!

    def test_should_deasciifySomeWords(self):
        deasciifier_logger.setLevel(logging.DEBUG)
        assert_that(self.deasciifier.deasciify(u' gece '), equal_to(u' gece '))
        deasciifier_logger.debug("\n\n\n------------------\n\n\n------------------\n\n\n------------------\n\n\n------------------\n\n\n")
        assert_that(self.deasciifier.deasciify(u' gecen '), equal_to(u' geçen '))
