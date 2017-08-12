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
        self.first_letter_upper_case_package_name = "Erp"
        self.lower_case_package_name = "erp"

        self.tag_replacers: dict = {
            "<#name#>": "Example",
            "<#nameLC#>": "example",
            "<#package#>": "ERP",
            "<#packageLC#>": "erp",
            "<#packageFLUC#>": "Erp",
        }

        self.tag_replacers2: dict = {
            "<#name#>": "Example2",
            "<#nameLC#>": "example2",
            "<#package#>": "ERP",
            "<#packageLC#>": "erp",
            "<#packageFLUC#>": "Erp",
        }

        self.output_uri = TestUtils.output_uri(self.test_name)
        self.output_uri2 = TestUtils.output_uri(self.test_name) + "2"
        self.template = TestUtils.example_template_uri
        self.template_backup = FileIO.read(self.template)

    def tearDown(self):
        FileIO.write(self.template, self.template_backup)
        FileIO.delete(self.output_uri)
        FileIO.delete(self.output_uri2)

    def test_generate_should_replace_all_tag_replacers(self):
        template = Template(self.template, self.output_uri, self.tag_replacers)
        generator = Generator([template])
        generator.generate()
        result = FileIO.read(self.output_uri)
        self.assert_all_placeholders_are_replaced(result, self.tag_replacers)

    def test_generate_should_replace_name_multiple_files(self):
        template = Template(self.template, self.output_uri, self.tag_replacers)
        template2 = Template(self.template, self.output_uri2, self.tag_replacers2)
        generator = Generator([template, template2])
        generator.generate()
        result = FileIO.read(self.output_uri)
        result2 = FileIO.read(self.output_uri2)
        self.assert_all_placeholders_are_replaced(result, self.tag_replacers)
        self.assert_all_placeholders_are_replaced(result2, self.tag_replacers2)

    @staticmethod
    def assert_all_placeholders_are_replaced(result, placeholders: dict) -> bool:
        for key, value in placeholders.items():
            assert_that(result).does_not_contain(key)
            assert_that(result).contains(value)

    def test_generate_should_raise_error_if_file_exists(self):
        template = Template(self.template, self.output_uri, self.tag_replacers)
        FileIO.write(self.output_uri, "test")
        generator = Generator([template])
        with self.assertRaises(FileExistsError):
            generator.generate()

    def test_generate_should_raise_error_if_template_not_exists(self):
        template = Template("wronguri", self.output_uri, self.tag_replacers)
        FileIO.write(self.output_uri, "test")
        generator = Generator([template])
        with self.assertRaises(FileNotFoundError):
            generator.generate()
