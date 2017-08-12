from unittest import TestCase

from assertpy import assert_that

from Application import Templates
from Application.TemplateFactory import TemplateFactory
from Application.TemplateType import TemplateType
from Application.WaWiUriFactory import WaWiUriFactory
from FileGenerator.Template import Template
from Utils import Values


class TestTemplateFactory(TestCase):
    def test_create_crud(self):
        uriFac = WaWiUriFactory(Values.default_base_uri)
        fac = TemplateFactory(TemplateType.CRUD, Values.default_base_uri)
        expected = [
            Template(Templates.crud_controller_template,
                     uriFac.controller("ERP", "ProductElementPrice"),
                     Values.default_replacers("ProductElementPrice", "ERP")),
            Template(Templates.icrud_controller_template,
                     uriFac.i_controller("ERP", "ProductElementPrice"),
                     Values.default_replacers("ProductElementPrice", "ERP")),
            Template(Templates.crud_repository_template,
                     uriFac.repo("ERP", "ProductElementPrice"),
                     Values.default_replacers("ProductElementPrice", "ERP")),
            Template(Templates.icrud_repository_template,
                     uriFac.i_repo("ERP", "ProductElementPrice"),
                     Values.default_replacers("ProductElementPrice", "ERP")),
            Template(Templates.crud_api_controller_template,
                     uriFac.admin_api_controller("ProductElementPrice"),
                     Values.default_replacers("ProductElementPrice", "ERP")),
        ]
        assert_that(fac.create("ERP", "ProductElementPrice")).is_equal_to(expected)

    def test_create_crud(self):
        uriFac = WaWiUriFactory(Values.default_base_uri)
        fac = TemplateFactory(TemplateType.SEARCHABLE, Values.default_base_uri)
        expected = [
            Template(Templates.searchable_controller_template,
                     uriFac.controller("ERP", "ProductElementPrice"),
                     Values.default_replacers("ProductElementPrice", "ERP")),
            Template(Templates.isearchable_controller_template,
                     uriFac.i_controller("ERP", "ProductElementPrice"),
                     Values.default_replacers("ProductElementPrice", "ERP")),
            Template(Templates.searchable_repository_template,
                     uriFac.repo("ERP", "ProductElementPrice"),
                     Values.default_replacers("ProductElementPrice", "ERP")),
            Template(Templates.isearchable_repository_template,
                     uriFac.i_repo("ERP", "ProductElementPrice"),
                     Values.default_replacers("ProductElementPrice", "ERP")),
            Template(Templates.searchable_api_controller_template,
                     uriFac.admin_api_controller("ProductElementPrice"),
                     Values.default_replacers("ProductElementPrice", "ERP")),
        ]
        assert_that(fac.create("ERP", "ProductElementPrice")).is_equal_to(expected)
