from unittest import TestCase

from assertpy import assert_that

from gen.application.wawi_uri_factory import WaWiUriFactory
from gen.utils import values


class TestFilename(TestCase):
    def test_controller(self):
        fac = WaWiUriFactory(values.default_base_uri)
        uri = fac.controller("CRM", "Customer")
        expected = f"{values.default_base_uri}CRM\\Controllers\\CustomerController.cs"
        assert_that(uri).is_equal_to(expected)

    def test_i_controller(self):
        fac = WaWiUriFactory(values.default_base_uri)
        uri = fac.i_controller("CRM", "Customer")
        expected = f"{values.default_base_uri}CRM\\ICustomerController.cs"
        assert_that(uri).is_equal_to(expected)

    def test_repo(self):
        fac = WaWiUriFactory(values.default_base_uri)
        uri = fac.repo("CRM", "Customer")
        expected = f"{values.default_base_uri}PersistenceCRM\\Repositories\\CustomerRepository.cs"
        assert_that(uri).is_equal_to(expected)

    def test_i_repo(self):
        fac = WaWiUriFactory(values.default_base_uri)
        uri = fac.i_repo("CRM", "Customer")
        expected = f"{values.default_base_uri}PersistenceCRM\\ICustomerRepository.cs"
        assert_that(uri).is_equal_to(expected)

    def test_api_controller(self):
        fac = WaWiUriFactory(values.default_base_uri)
        uri = fac.admin_api_controller("Customer")
        expected = f"{values.default_base_uri}AdminApi\\Controllers\\CRM\\CustomerApiController.cs"
        assert_that(uri).is_equal_to(expected)
