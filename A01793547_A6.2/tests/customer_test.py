""""
This module contains the tests for the Customer class.
"""
import unittest
import os
from src.hotel import Hotel
from src.customer import Customer


class TestCustomer(unittest.TestCase):
    """
    A class to test customer operations.
    """

    @classmethod
    def setUpClass(cls):
        """
        Sets up the test environment by creating an instance of the Customer
        class and creating a hotel with customers.
        """
        cls.hotel = Hotel('hotels.json')
        cls.hotel.create_hotel(
            'Best Western',
            'Houston, Texas',
            {'single': 2, 'double': 1,
             'suite': 3}
             )
        cls.customer = Customer('hotels.json')
        cls.customer.create_customer('Best Western', 'John Doe')
        cls.customer.create_customer('Best Western', 'Jane Doe')

    @classmethod
    def tearDownClass(cls):
        """
        Cleans up the test environment by deleting the JSON file if it exists.
        """
        if os.path.exists('hotels.json'):
            os.remove('hotels.json')

    def setUp(self):
        """
        Sets up the test environment.
        """
        self.teardown_called = False

    def tearDown(self):
        """
        Marks that teardown has been called.
        """
        self.teardown_called = True

    def test_create_customer(self):
        """
        Tests creating a new customer.
        """
        self.assertEqual(self.customer.create_customer(
            'Best Western', 'Alice Smith'),
            'Customer Alice Smith created for Best Western')

    def test_create_customer_hotel_not_found(self):
        """
        Tests creating a customer for a hotel that does not exist.
        """
        self.assertEqual(self.customer.create_customer(
            'St. Adams Hotel', 'Bob Johnson'),
            'Customer Bob Johnson not created. '
            'Hotel St. Adams Hotel not found')

    def test_delete_customer(self):
        """
        Tests deleting a customer.
        """
        self.assertEqual(self.customer.delete_customer(
            'Best Western', 'John Doe'),
            'Customer John Doe deleted')

    def test_delete_customer_not_found(self):
        """
        Tests deleting a customer that does not exist.
        """
        self.assertEqual(self.customer.delete_customer(
            'Best Western', 'Juan Perez'),
            'Customer Juan Perez not found in Best Western')

    def test_display_customer_info(self):
        """
        Tests displaying customer information.
        """
        self.assertEqual(self.customer.display_customer_info(
            'Best Western', 'Jane Doe'),
            {'customer_id': 2, 'customer_name': 'Jane Doe'})

    def test_display_customer_info_not_found(self):
        """
        Tests displaying information of a customer that does not exist.
        """
        self.assertEqual(self.customer.display_customer_info(
            'Best Western', 'Juan Perez'),
            'Customer Juan Perez not found in Best Western')

    def test_modify_customer_info(self):
        """
        Tests modifying customer information.
        """
        self.assertEqual(self.customer.modify_customer_info(
            'Best Western', 'Jane Doe', 'Jane Smith'),
            'Customer name updated from Jane Doe to Jane Smith')

    def test_modify_customer_info_not_found(self):
        """
        Tests modifying information of a customer that does not exist.
        """
        self.assertEqual(self.customer.modify_customer_info(
            'Best Western', 'Juan Perez', 'John Smith'),
            'Customer Juan Perez not found in Best Western')
