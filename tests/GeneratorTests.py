from unittest import TestCase
from assertpy import assert_that

from generator.FileIO import FileIO
from generator.Generator import Generator
from generator.Template import Template
from tests import TestUtils


class TestGenerator(TestCase):
    def __init__(self, methodName='runTest'):
        self.template = TestUtils.example_template_uri
        super().__init__(methodName)

    def setUp(self):
        self.template_backup = FileIO.read(self.template)

    def tearDown(self):
        FileIO.write(self.template, self.template_backup)

    def test_generate(self):
        test_name = "Example"
        output_uri = TestUtils.output_uri(test_name)
        template = Template(self.template, output_uri, test_name)
        generator = Generator(template)

        generator.generate()
        result = FileIO.read(output_uri)
        assert_that(result).contains(f"{test_name}Repository")
