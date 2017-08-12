from unittest import TestCase
from assertpy import assert_that

from Generator.FileIO import FileIO
from Generator.Generator import Generator
from Generator.Template import Template
from Tests import TestUtils


class TestGenerator(TestCase):
    def setUp(self):
        self.test_name = "Example"
        self.package_name = "ERP"
        self.lower_case_package_name = "erp"
        self.test_name2 = "Example2"
        self.output_uri = TestUtils.output_uri(self.test_name)
        self.output_uri2 = TestUtils.output_uri(self.test_name) + "2"
        self.template = TestUtils.example_template_uri
        self.template_backup = FileIO.read(self.template)

    def tearDown(self):
        FileIO.write(self.template, self.template_backup)
        FileIO.delete(self.output_uri)
        FileIO.delete(self.output_uri2)

    def test_generate_should_replace_name(self):
        template = Template(self.template, self.output_uri, self.test_name, self.package_name)
        generator = Generator([template])
        generator.generate()
        result = FileIO.read(self.output_uri)
        assert_that(result).contains(f"{self.test_name}Repository")

    def test_generate_should_replace_package(self):
        template = Template(self.template, self.output_uri, self.test_name, self.package_name)
        generator = Generator([template])
        generator.generate()
        result = FileIO.read(self.output_uri)
        assert_that(result).contains(f"Persistence{self.package_name}")

    def test_generate_should_replace_lower_case_package(self):
        template = Template(self.template, self.output_uri, self.test_name, self.package_name)
        generator = Generator([template])
        generator.generate()
        result = FileIO.read(self.output_uri)
        assert_that(result).contains(f"{self.lower_case_package_name}-package-name")

    def test_generate_should_replace_name_multiple_files(self):
        template = Template(self.template, self.output_uri, self.test_name, self.package_name)
        template2 = Template(self.template, self.output_uri2, self.test_name2, self.package_name)
        generator = Generator([template, template2])
        generator.generate()
        result = FileIO.read(self.output_uri)
        result2 = FileIO.read(self.output_uri2)

        assert_that(result).contains(f"{self.test_name}Repository")
        assert_that(result2).contains(f"{self.test_name2}Repository")

    def test_generate_should_not_overwrite_existing_file(self):
        template = Template(self.template, self.output_uri, self.test_name, self.package_name)
        FileIO.write(self.output_uri, "test")
        generator = Generator([template])
        generator.generate()
        result = FileIO.read(self.output_uri)
        assert_that(result).contains(f"test")
