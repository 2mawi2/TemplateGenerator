from unittest import TestCase

from assertpy import assert_that

from gen.model.template import Template


class TestTemplateFactory(TestCase):
    def test_template_str(self):
        template = Template("someUri", "someOutput", {"some": "replacers"})
        assert_that(template.__str__()).is_equal_to("someUri, someOutput, {'some': 'replacers'}")

    def test_template_equ(self):
        template = Template("someUri", "someOutput", {"some": "replacers"})
        template2: object = Template("someUri", "someOutput", {"some": "replacers"})
        assert_that(template).is_equal_to(template2)

    def test_template_equ(self):
        template = Template("someUri", "someOutput", {"some": "replacers"})
        template2: object = object
        assert_that(template).is_not_equal_to(template2)
