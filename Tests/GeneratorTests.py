from unittest import TestCase
from assertpy import assert_that

from Generator.FileIO import FileIO
from Generator.Generator import Generator
from Generator.Template import Template
from Tests import TestUtils


class TestGenerator(TestCase):
    def setUp(self):
        self.test_name = "Example"
        self.test_name2 = "Example2"
        self.output_uri = TestUtils.output_uri(self.test_name)
        self.output_uri2 = TestUtils.output_uri(self.test_name) + "2"
        self.template = TestUtils.example_template_uri
        self.template_backup = FileIO.read(self.template)

    def tearDown(self):
        FileIO.write(self.template, self.template_backup)
        FileIO.delete(self.output_uri)
        FileIO.delete(self.output_uri2)

    def test_generate(self):
        template = Template(self.template, self.output_uri, self.test_name)
        generator = Generator([template])
        generator.generate()
        result = FileIO.read(self.output_uri)
        assert_that(result).contains(f"{self.test_name}Repository")

    def test_generate(self):
        template = Template(self.template, self.output_uri, self.test_name)
        template2 = Template(self.template, self.output_uri2, self.test_name2)
        generator = Generator([template, template2])
        generator.generate()
        result = FileIO.read(self.output_uri)
        result2 = FileIO.read(self.output_uri2)

        assert_that(result).contains(f"{self.test_name}Repository")
        assert_that(result2).contains(f"{self.test_name2}Repository")
