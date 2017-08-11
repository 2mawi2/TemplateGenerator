from unittest import TestCase
from assertpy import assert_that

from generator.Generator import Generator, Template


class TestGenerator(TestCase):
    def test_generate(self):
        template = Template("testUri", "testName")
        generator = Generator(template)
        assert_that(generator.generate()).is_equal_to(True)
