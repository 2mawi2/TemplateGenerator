from unittest import TestCase

from assertpy import assert_that

from gen.application.factories.template_factory import TemplateFactory
from gen.application.factories.wawi_uri_factory import WaWiUriFactory
from gen.model.template import Template
from gen.model.template_type import TemplateType
from gen.utils import values


class TestTemplateFactory(TestCase):
    def test_create_crud(self):
        uri_fac = WaWiUriFactory(values.default_base_uri)
        fac = TemplateFactory(TemplateType.CRUD, values.default_base_uri)
        default_replacers = values.default_replacers("ProductElementPrice", "ERP")
        expected = [
            Template(values.crud_controller_template,
                     uri_fac.controller("ERP", "ProductElementPrice"),
                     default_replacers),
            Template(values.icrud_controller_template,
                     uri_fac.i_controller("ERP", "ProductElementPrice"),
                     default_replacers),
            Template(values.test_controller_template,
                     uri_fac.test_controller("ERP", "ProductElementPrice"),
                     default_replacers),
            Template(values.crud_repository_template,
                     uri_fac.repo("ERP", "ProductElementPrice"),
                     default_replacers),
            Template(values.icrud_repository_template,
                     uri_fac.i_repo("ERP", "ProductElementPrice"),
                     default_replacers),
            Template(values.test_repository_template,
                     uri_fac.test_repository("ERP", "ProductElementPrice"),
                     default_replacers),
            Template(values.crud_api_controller_template,
                     uri_fac.api_controller("ERP", "ProductElementPrice"),
                     default_replacers),
            Template(values.test_api_controller_template,
                     uri_fac.test_api_controller("ERP", "ProductElementPrice"),
                     default_replacers),
        ]
        assert_that(fac.create("ERP", "ProductElementPrice")).is_equal_to(expected)

    def test_create_searchable(self):
        uri_fac = WaWiUriFactory(values.default_base_uri)
        fac = TemplateFactory(TemplateType.SEARCHABLE, values.default_base_uri)
        default_replacers = values.default_replacers("ProductElementPrice", "ERP")
        expected = [
            Template(values.searchable_controller_template,
                     uri_fac.controller("ERP", "ProductElementPrice"),
                     default_replacers),
            Template(values.isearchable_controller_template,
                     uri_fac.i_controller("ERP", "ProductElementPrice"),
                     default_replacers),
            Template(values.test_controller_template,
                     uri_fac.test_controller("ERP", "ProductElementPrice"),
                     default_replacers),
            Template(values.searchable_repository_template,
                     uri_fac.repo("ERP", "ProductElementPrice"),
                     default_replacers),
            Template(values.isearchable_repository_template,
                     uri_fac.i_repo("ERP", "ProductElementPrice"),
                     default_replacers),
            Template(values.test_repository_template,
                     uri_fac.test_repository("ERP", "ProductElementPrice"),
                     default_replacers),
            Template(values.searchable_api_controller_template,
                     uri_fac.api_controller("ERP", "ProductElementPrice"),
                     default_replacers),
            Template(values.test_api_controller_template,
                     uri_fac.test_api_controller("ERP", "ProductElementPrice"),
                     default_replacers),
        ]
        assert_that(fac.create("ERP", "ProductElementPrice")).is_equal_to(expected)
