from unittest import TestCase

from assertpy import assert_that

from Application import WaWiUriFactory


class TestFilename(TestCase):
    def test_controller(self):
        fac = WaWiUriFactory
        uri = fac.controller("CRM", "Customer")
        expected = "C:\\Users\\Marius\\Source\\Repos\\WaWi_Backend\\CRM\\Controllers\\CustomerController.cs"
        assert_that(uri).is_equal_to(expected)

    def test_i_controller(self):
        fac = WaWiUriFactory
        uri = fac.i_controller("CRM", "Customer")
        expected = "C:\\Users\\Marius\\Source\\Repos\\WaWi_Backend\\CRM\\ICustomerController.cs"
        assert_that(uri).is_equal_to(expected)

    def test_repo(self):
        fac = WaWiUriFactory
        uri = fac.repo("CRM", "Customer")
        expected = "C:\\Users\\Marius\\Source\\Repos\\WaWi_Backend\\PersistenceCRM\\Repositories\\CustomerRepository.cs"
        assert_that(uri).is_equal_to(expected)

    def test_i_repo(self):
        fac = WaWiUriFactory
        uri = fac.i_repo("CRM", "Customer")
        expected = "C:\\Users\\Marius\\Source\\Repos\\WaWi_Backend\\PersistenceCRM\\ICustomerRepository.cs"
        assert_that(uri).is_equal_to(expected)

    def test_api_controller(self):
        fac = WaWiUriFactory
        uri = fac.admin_api_controller("Customer")
        expected = "C:\\Users\\Marius\\Source\\Repos\\WaWi_Backend\\AdminApi\\Controllers\\CustomerApiController.cs"
        assert_that(uri).is_equal_to(expected)
