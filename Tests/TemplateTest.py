from unittest import TestCase

from assertpy import assert_that

from Generator.Template import Template


class TestTemplate(TestCase):
    def test_default_replacers(self):
        result = Template.default_replacers("Customer", "ERP")
        expected = {
            "<#name#>": "Customer",
            "<#package#>": "ERP",
            "<#packageLC#>": "erp",
            "<#packageFLUC#>": "Erp",
        }
        assert_that(result).is_equal_to(expected)
