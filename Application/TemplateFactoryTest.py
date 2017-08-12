from unittest import TestCase

from assertpy import assert_that

from Application import WaWiUriFactory, Templates
from Application.TemplateFactory import TemplateFactory
from Application.TemplateType import TemplateType
from Generator.Template import Template


class TestTemplateFactory(TestCase):
    def test_create(self):
        fac = TemplateFactory(TemplateType.CRUD)
        expected = [
            Template(Templates.crud_controller_template,
                     WaWiUriFactory.controller("ERP", "ProductElementPrice"),
                     Template.default_replacers("ProductElementPrice", "ERP")),
            Template(Templates.icrud_controller_template,
                     WaWiUriFactory.i_controller("ERP", "ProductElementPrice"),
                     Template.default_replacers("ProductElementPrice", "ERP")),
            Template(Templates.crud_repository_template,
                     WaWiUriFactory.repo("ERP", "ProductElementPrice"),
                     Template.default_replacers("ProductElementPrice", "ERP")),
            Template(Templates.icrud_repository_template,
                     WaWiUriFactory.i_repo("ERP", "ProductElementPrice"),
                     Template.default_replacers("ProductElementPrice", "ERP")),
            Template(Templates.crud_api_controller_template,
                     WaWiUriFactory.admin_api_controller("ProductElementPrice"),
                     Template.default_replacers("ProductElementPrice", "ERP")),
        ]
        assert_that(fac.create("ERP", "ProductElementPrice")).is_equal_to(expected)
