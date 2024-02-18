""""
This module contains the tests for the Reservation class.
"""
import unittest
import os
from src.customer import Customer
from src.reservation import Reservation
from src.hotel import Hotel


class TestReservation(unittest.TestCase):
    """
    A class to test reservation operations.
    """

    @classmethod
    def setUpClass(cls):
        """
        Sets up the test environment by creating an instance of the Reservation
        class, Customer class, and creating a hotel with customers and
        reservations.
        """
        cls.hotel = Hotel('hotels.json')
        cls.hotel.create_hotel(
            'Best Western',
            'Houston, Texas',
            {'single': 1, 'double': 1,
             'suite': 3}
             )
        cls.reservation = Reservation('hotels.json')
        cls.customer = Customer('hotels.json')
        cls.customer.create_customer('Best Western', 'John Doe')
        cls.customer.create_customer('Best Western', 'Alice Smith')
        cls.customer.create_customer('Best Western', 'Bob Johnson')

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

    def test_create_reservation(self):
        """
        Tests creating a new reservation.
        """
        self.assertEqual(self.reservation.create_reservation(
            'Best Western', 'Alice Smith', '2024-02-15', 'single'),
            'Reservation for Alice Smith created at Best Western')

    def test_create_reservation_no_room_available(self):
        """
        Tests creating a reservation when no rooms of the specified type are
        available.
        """
        self.assertEqual(self.reservation.create_reservation(
            'Best Western', 'Bob Johnson', '2024-02-15', 'single'),
            'No single rooms available')

    def test_create_reservation_hotel_not_found(self):
        """
        Tests creating a reservation for a hotel that does not exist.
        """
        self.assertEqual(self.reservation.create_reservation(
            'St. Adams Hotel', 'Alice Smith', '2024-02-15', 'single'),
            'Customer Alice Smith not found in St. Adams Hotel')

    def test_cancel_reservation_success(self):
        """
        Tests canceling a reservation successfully.
        """
        self.reservation.create_reservation('Best Western',
                                            'John Doe',
                                            '2024-02-14',
                                            'single')
        self.assertEqual(self.reservation.cancel_reservation(
            'Best Western', 'John Doe'),
            'Reservation for John Doe cancelled at Best Western')

    def test_cancel_reservation_not_found(self):
        """
        Tests canceling a reservation that does not exist.
        """
        self.assertEqual(self.reservation.cancel_reservation(
            'Best Western', 'Alice Smith'),
            'No reservation found for Alice Smith in Best Western')

    def test_cancel_reservation_hotel_not_found(self):
        """
        Tests canceling a reservation in a hotel that does not exist.
        """
        self.assertEqual(self.reservation.cancel_reservation(
            'St. Adams Hotel', 'John Doe'),
            'Hotel St. Adams Hotel not found')
