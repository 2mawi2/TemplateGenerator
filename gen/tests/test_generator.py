from unittest import TestCase

from assertpy import assert_that

from gen.app.file_generator.file_generator import FileGenerator
from gen.app.file_generator.file_io import FileIO
from gen.model.template import Template
from gen.utils import test_utils


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

        self.output_uri = test_utils.output_uri(self.test_name)
        self.output_uri2 = test_utils.output_uri(self.test_name) + "2"
        self.template = test_utils.example_template_uri
        self.template_backup = FileIO.read(self.template)

    def tearDown(self):
        FileIO.write(self.template, self.template_backup)
        FileIO.delete(self.output_uri)
        FileIO.delete(self.output_uri2)

    def test_generate_should_replace_all_tag_replacers(self):
        template = Template(self.template, self.output_uri, self.tag_replacers)
        generator = FileGenerator([template])
        generator.generate()
        result = FileIO.read(self.output_uri)
        self.assert_all_placeholders_are_replaced(result, self.tag_replacers)

    def test_generate_should_replace_name_multiple_files(self):
        template = Template(self.template, self.output_uri, self.tag_replacers)
        template2 = Template(self.template, self.output_uri2, self.tag_replacers2)
        generator = FileGenerator([template, template2])
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

    def test_generate_should_not_override_file(self):
        template = Template(self.template, self.output_uri, self.tag_replacers)
        FileIO.write(self.output_uri, "test")
        generator = FileGenerator([template])
        generator.generate()
        result = FileIO.read(self.output_uri)
        assert_that(result).is_equal_to("test")

    def test_generate_should_raise_error_if_template_not_exists(self):
        template = Template("wronguri", self.output_uri, self.tag_replacers)
        FileIO.write(self.output_uri, "test")
        generator = FileGenerator([template])
        with self.assertRaises(FileNotFoundError):
            generator.generate()
