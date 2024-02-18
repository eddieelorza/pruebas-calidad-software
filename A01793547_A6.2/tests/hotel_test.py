""""
This module contains the tests for the Hotel class.
"""
import unittest
import os
from src.hotel import Hotel


class TestHotelCreation(unittest.TestCase):
    """
    A class to test the Hotel class.
    """
    def setUp(self):
        """
        Sets up the test environment by creating an instance of the Hotel
        class.
        """
        self.hotel = Hotel('hotels.json')
        self.teardown_called = False

    def tearDown(self):
        """
        Cleans up the test environment by deleting the JSON file if it exists.
        """
        if self.teardown_called and os.path.exists('hotels.json'):
            os.remove('hotels.json')

    def test_json_creation(self):
        """
        Tests that the JSON file is created when the Hotel class is invoked.
        """
        self.assertEqual(self.hotel.filename, 'hotels.json')

    def test_create_hotel(self):
        """
        Tests that the create_hotel method creates a hotel.
        """
        self.assertEqual(self.hotel.create_hotel(
            'St. George Hotel',
            'Tucson Arizona',
            {'single': 2, 'double': 5,
             'suite': 3}), 'Hotel created')
        self.teardown_called = True


class TestHotelDeletion(unittest.TestCase):
    """
    A class to test the deletion of a hotel.
    """
    def setUp(self):
        """
        Sets up the test environment by creating an instance of the Hotel
        class and creating a hotel.
        """
        self.hotel = Hotel('hotel.json')
        self.hotel.create_hotel(
            'St. George Hotel',
            'Tucson Arizona',
            {'single': 2, 'double': 5,
             'suite': 3})
        self.teardown_called = False

    def tearDown(self):
        """
        Cleans up the test environment by deleting the JSON file if it exists.
        """
        if self.teardown_called and os.path.exists('hotel.json'):
            os.remove('hotel.json')

    def test_delete_hotel(self):
        """
        Tests that the delete_hotel method deletes a hotel.
        """
        self.assertEqual(self.hotel.delete_hotel('St. George Hotel'),
                         'Hotel deleted')

    def test_delete_hotel_not_found(self):
        """
        Test delete_hotel method if the hotel doesn't exist.
        """
        self.assertEqual(self.hotel.delete_hotel('St. Adams Hotel'),
                         'Hotel not found')
        self.teardown_called = True


class TestHotelInfo(unittest.TestCase):
    """
    A class to test the info of a hotel.
    """
    def setUp(self):
        """
        Sets up the test environment by creating an instance of the Hotel
        class and creating a hotel.
        """
        self.hotel = Hotel('texas.json')
        self.hotel.create_hotel(
            'Marriot',
            'Houston Texas',
            {'single': 4, 'double': 5,
             'suite': 2})
        self.teardown_called = False

    def tearDown(self):
        """
        Cleans up the test environment by deleting the JSON file if it exists.
        """
        if self.teardown_called and os.path.exists('texas.json'):
            os.remove('texas.json')

    def test_hotel_info(self):
        """
        Tests that the info method returns the hotel information.
        """
        self.assertEqual(self.hotel.display_hotel_info('Marriot'),
                         {'hotel_id': 1, 'name': 'Marriot',
                          'location': 'Houston Texas',
                          'rooms': {'single': 4, 'double': 5, 'suite': 2},
                          'reservations': [], 'customers': []})

    def test_hotel_info_not_found(self):
        """
        Tests the info method if the hotel is not found.
        """
        self.assertEqual(self.hotel.display_hotel_info('St. Adams Hotel'),
                         'Hotel not found')
        self.teardown_called = True


class TestHotelModification(unittest.TestCase):
    """
    A class to test the modification of the hotel information.
    """
    def setUp(self):
        """
        Sets up the test environment by creating an instance of the Hotel
        class and creating a hotel.
        """
        self.hotel = Hotel('hotels.json')
        self.hotel.create_hotel(
            'Best Western',
            'San Antonio Texas',
            {'single': 10, 'double': 7,
             'suite': 3})
        self.teardown_called = False

    def tearDown(self):
        """
        Cleans up the test environment by deleting the JSON file if it exists.
        """
        if self.teardown_called and os.path.exists('hotels.json'):
            os.remove('hotels.json')

    def test_modify_hotel(self):
        """
        Tests that the modify_hotel method modifies a hotel
        and the display info is still correct.
        """
        self.assertEqual(self.hotel.modify_hotel_info(
            'Best Western',
            'Best Western Hotel',
            'San Antonio, Texas'),
            'Hotel information modified')

        self.assertEqual(
            self.hotel.display_hotel_info('Best Western Hotel'),
            {'hotel_id': 1, 'name': 'Best Western Hotel',
             'location': 'San Antonio, Texas',
             'rooms': {'single': 10, 'double': 7, 'suite': 3},
             'reservations': [], 'customers': []})

    def test_modify_hotel_not_found(self):
        """
        Tests the modify_hotel method if the hotel is not found.
        """
        self.assertEqual(self.hotel.modify_hotel_info(
            'St. Adams Hotel',
            'St. Adams Hotel',
            'Tucson, Arizona'),
            'St. Adams Hotel not found')
        self.teardown_called = True


class TestHotelReservation(unittest.TestCase):
    """
    A class to test the reservation of a hotel.
    """
    @classmethod
    def setUpClass(cls):
        """
        Sets up the test environment by creating an instance of the Hotel
        class and creating a hotel.
        """
        cls.hotel = Hotel('hotels.json')
        cls.hotel.create_hotel(
            'Best Western',
            'San Antonio Texas',
            {'single': 1, 'double': 7,
             'suite': 3})

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

    def test_reserve_room(self):
        """
        Tests that the reserve_room method reserves a room.
        """
        self.assertEqual(self.hotel.reserve_room(
            hotel_name='Best Western',
            room_type='single',
            reservation_date='2019-12-24',
            customer_name='John Doe'),
            'single room reserved for John Doe'
        )

    def test_reserve_room_no_single_available(self):
        """
        Test that the reserve_room method returns a message if no single
        rooms are available.
        """
        self.assertEqual(self.hotel.reserve_room(
            hotel_name='Best Western',
            room_type='single',
            reservation_date='2019-12-24',
            customer_name='Jane Doe'),
            'No single rooms available'
        )

    def test_reserve_room_hotel_not_exist(self):
        """
        Test that the reserve_room method returns a message if the hotel
        does not exist.
        """
        self.assertEqual(self.hotel.reserve_room(
            hotel_name='St. Adams Hotel',
            room_type='single',
            reservation_date='2019-12-24',
            customer_name='Jane Doe'),
            'St. Adams Hotel not found'
        )


class TestHotelCancelReservation(unittest.TestCase):
    """
    A class to test canceling a reservation in a hotel.
    """

    @classmethod
    def setUpClass(cls):
        """
        Sets up the test environment by creating an instance of the Hotel
        class and creating a hotel.
        """
        cls.hotel = Hotel('hotels.json')
        cls.hotel.create_hotel(
            'Best Western',
            'San Antonio Texas',
            {'single': 1, 'double': 7,
             'suite': 3})
        cls.hotel.reserve_room(
            hotel_name='Best Western',
            room_type='single',
            reservation_date='2019-12-24',
            customer_name='John Doe')

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

    def test_cancel_reservation_success(self):
        """
        Tests canceling a reservation successfully.
        """
        self.assertEqual(self.hotel.cancel_reservation(
            hotel_name='Best Western',
            customer_name='John Doe'),
            'Reservation canceled for John Doe'
        )

    def test_cancel_reservation_not_found(self):
        """
        Tests canceling a reservation that does not exist.
        """
        self.assertEqual(self.hotel.cancel_reservation(
            hotel_name='Best Western',
            customer_name='Jane Doe'),
            'No reservation found for Jane Doe'
        )

    def test_cancel_reservation_hotel_not_found(self):
        """
        Tests canceling a reservation in a hotel that does not exist.
        """
        self.assertEqual(self.hotel.cancel_reservation(
            hotel_name='St. Adams Hotel',
            customer_name='John Doe'),
            'Hotel St. Adams Hotel not found'
        )
