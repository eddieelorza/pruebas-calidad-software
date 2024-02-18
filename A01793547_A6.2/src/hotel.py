"""
Module for managing hotel information and reservations.

Uses JSON file for data storage.

Libraries:
- json: Provides functions for reading and writing JSON data.
- os: Provides functions for interacting with the operating system.
"""

import json
import os


class Hotel:
    """
    A class to represent a hotel and manage its information and reservations.

    Attributes:
    - reservation_counter (int): A class attribute to keep track of the
    reservation count.
    - filename (str): The filename for storing hotel data in JSON format.

    Methods:
    - create_hotel: Creates a new hotel entry in the JSON file.
    - get_customer_id: Retrieves the ID of a customer from the hotel's
    customer list.
    - delete_hotel: Deletes a hotel entry from the JSON file.
    - display_hotel_info: Displays information about a specific hotel.
    - modify_hotel_info: Modifies information about a specific hotel.
    - reserve_room: Reserves a room in a specific hotel for a customer.
    - cancel_reservation: Cancels a reservation for a customer in a specific
    hotel.
    """
    # Class attribute to keep track of the reservation count
    reservation_counter = 0

    def __init__(self, filename: str = 'hotels.json'):
        # Initializes a Hotel object with the specified hotel data filename
        self.filename = filename
        # Check if the filename has a JSON extension
        if not self.filename.endswith('.json'):
            self.filename += '.json'

    def create_hotel(self, name: str, location: str, rooms: dict):
        """
        Creates a new hotel entry in the JSON file.

        Parameters:
        - name: The name of the hotel.
        - location: The location of the hotel.
        - rooms: A dictionary containing room types and their quantities.

        Returns:
        A string indicating the success of the operation.
        """
        # Check if the file exists
        if os.path.exists(self.filename):
            # Open the hotel data file
            with open(self.filename, 'r', encoding='UTF-8') as file:
                hotels_data = json.load(file)
        else:
            # Create a new file if it doesn't exist
            hotels_data = []

        # Create a new hotel ID
        hotel_id = len(hotels_data) + 1
        # Create a dictionary for the new hotel
        hotel_info = {'hotel_id': hotel_id, 'name': name, 'location': location,
                      'rooms': rooms, 'reservations': [], 'customers': []}
        # Append the new hotel to the list of hotels
        hotels_data.append(hotel_info)

        # Write the updated hotel data to the file
        with open(self.filename, 'w', encoding='UTF-8') as file:
            json.dump(hotels_data, file, indent=4)

        # Return a success message
        return 'Hotel created'

    def get_customer_id(self, hotel_name: str, customer_name: str):
        """
        Retrieves the ID of a customer from the hotel's customer list.

        Parameters:
        - hotel_name: The name of the hotel.
        - customer_name: The name of the customer.

        Returns:
        The ID of the customer if found, otherwise None.
        """
        # Check if the file exists
        if os.path.exists(self.filename):
            # Open the hotel data file
            with open(self.filename, 'r', encoding='UTF-8') as file:
                hotels_data = json.load(file)
                # Iterate through each hotel in the data
                for hotel in hotels_data:
                    # Check if the hotel name matches the specified hotel
                    if hotel['name'] == hotel_name:
                        customers = hotel['customers']
                        # Iterate through each customer in the hotel
                        for customer in customers:
                            # Check if the customer name matches the specified
                            if customer['customer_name'] == customer_name:
                                # Return the customer ID
                                return customer['customer_id']
                        # If the customer is not found, create a new customer
                        customer_id = len(customers) + 1
                        # Append the new customer to the list of customers
                        customers.append({'customer_id': customer_id,
                                          'customer_name': customer_name})
                        # Write the updated hotel data to the file
                        with open(self.filename, 'w',
                                  encoding='UTF-8') as file:
                            json.dump(hotels_data, file, indent=4)
                        # Return the new customer ID
                        return customer_id
                return None
        return None

    def delete_hotel(self, hotel_name: str):
        """
        Deletes a hotel entry from the JSON file.

        Parameters:
        - hotel_name: The name of the hotel to delete.

        Returns:
        A string indicating the success of the operation.
        """
        # Check if the file exists
        if os.path.exists(self.filename):
            # Open the hotel data file
            with open(self.filename, 'r', encoding='UTF-8') as file:
                hotels_data = json.load(file)
                # Iterate through each hotel in the data
                for hotel in hotels_data:
                    # Check if the hotel name matches the specified hotel
                    if hotel['name'] == hotel_name:
                        hotels_data.remove(hotel)
                        # Write the updated hotel data to the file
                        with open(self.filename, 'w',
                                  encoding='UTF-8') as file:
                            json.dump(hotels_data, file, indent=4)
                        # Return a success message
                        return 'Hotel deleted'
                # If the specified hotel is not found, return an error message
                return 'Hotel not found'
        # If the file does not exist, return an error message
        return 'Hotel information not found'

    def display_hotel_info(self, hotel_name: str):
        """
        Displays information about a specific hotel.

        Parameters:
        - hotel_name: The name of the hotel to display information for.

        Returns:
        The information of the hotel if found, otherwise a message indicating
        the hotel was not found.
        """
        # Check if the file exists
        if os.path.exists(self.filename):
            # Open the hotel data file
            with open(self.filename, 'r', encoding='UTF-8') as file:
                hotels_data = json.load(file)
                # Iterate through each hotel in the data
                for hotel in hotels_data:
                    if hotel['name'] == hotel_name:
                        # Return the hotel information
                        return hotel
            # If the specified hotel is not found, return an error message
            return 'Hotel not found'
        # If the file does not exist, return an error message
        return 'Hotel information file not found, please verify'

    def modify_hotel_info(self, hotel_name: str, new_name: str = '',
                          new_location: str = ''):
        """
        Modifies information about a specific hotel.

        Parameters:
        - hotel_name: The name of the hotel to modify.
        - new_name: The new name for the hotel (optional).
        - new_location: The new location for the hotel (optional).

        Returns:
        A string indicating the success of the operation or a message if the
        hotel was not found.
        """
        # Check if the file exists
        if os.path.exists(self.filename):
            # Open the hotel data file
            with open(self.filename, 'r', encoding='UTF-8') as file:
                hotels_data = json.load(file)

            # Iterate through each hotel in the data
            hotel_found = False
            # Check if the hotel name matches the specified hotel
            for hotel in hotels_data:
                # Check if the hotel name matches the specified hotel
                if hotel['name'] == hotel_name:
                    # If the hotel is found, modify the hotel information
                    if new_name:
                        hotel['name'] = new_name
                    # If the hotel is found, modify the hotel information
                    if new_location:
                        hotel['location'] = new_location
                    # Set the hotel_found flag to True
                    hotel_found = True
                    break

            # If the hotel is found, write the updated hotel data to the file
            if hotel_found:
                # Write the updated hotel data to the file
                with open(self.filename, 'w', encoding='UTF-8') as file:
                    json.dump(hotels_data, file, indent=4)
                # Return a success message
                return 'Hotel information modified'
            # If the specified hotel is not found, return an error message
            return f'{hotel_name} not found'
        # If the file does not exist, return an error message
        return 'Hotel information not found, please verify the file name'

    def reserve_room(self, hotel_name: int, customer_name: str,
                     reservation_date: str, room_type: str = 'single'):
        """
        Reserves a room in a specific hotel for a customer.

        Parameters:
        - hotel_name: The name of the hotel to reserve a room in.
        - customer_name: The name of the customer making the reservation.
        - reservation_date: The date of the reservation.
        - room_type: The type of room to reserve (default is 'single').

        Returns:
        A string indicating the success of the reservation or a message if the
        room type or hotel was not found.
        """
        # Check if the file exists
        if os.path.exists(self.filename):
            # Open the hotel data file
            with open(self.filename, 'r', encoding='UTF-8') as file:
                hotels_data = json.load(file)

            # Iterate through each hotel in the data
            hotel_found = False
            # Check if the hotel name matches the specified hotel
            for hotel in hotels_data:
                # Check if the hotel name matches the specified hotel
                if hotel['name'] == hotel_name:
                    # If the hotel is found, retrieve the list of customers
                    customer_id = self.get_customer_id(hotel_name,
                                                       customer_name)
                    # If the customer is not found, return an error message
                    if customer_id is None:
                        # If the customer is not found, return an error message
                        return 'Customer not found or could not be created'
                    # If the customer is found, check if the room type exists
                    if room_type in hotel['rooms']:
                        # If the room type exists, check if there are available
                        if hotel['rooms'][room_type] > 0:
                            # If there are available rooms, create a new
                            self.__class__.reservation_counter += 1
                            # reservation and update the hotel data
                            reservation_id = self.__class__.reservation_counter
                            # Create a new reservation
                            hotel['rooms'][room_type] -= 1
                            # Append the new reservation to the list of
                            # reservations
                            hotel['reservations'].append({
                                'id': reservation_id,
                                'customer_id': customer_id,
                                'customer_name': customer_name,
                                'room_type': room_type,
                                'date': reservation_date})
                            # Set the hotel_found flag to True
                            hotel_found = True
                            break
                        # If there are no available rooms of the specified type
                        # return no rooms available message
                        return f'No {room_type} rooms available'
                    # If the room type does not exist, return an error message
                    return f'{room_type} room type not found.'
            # If the specified hotel is not found, return an error message
            if hotel_found:
                # Write the updated hotel data to the file
                with open(self.filename, 'w', encoding='UTF-8') as file:
                    json.dump(hotels_data, file, indent=4)
                # Return a success message
                return f'{room_type} room reserved for {customer_name}'
            # If the specified hotel is not found, return an error message
            return f'{hotel_name} not found'
        # If the file does not exist, return an error message
        return 'Hotel information not found, please verify'

    def cancel_reservation(self, hotel_name: str, customer_name: str):
        """
        Cancels a reservation for a customer in a specific hotel.

        Parameters:
        - hotel_name: The name of the hotel where the reservation is made.
        - customer_name: The name of the customer whose reservation is to be
        canceled.

        Returns:
        A string indicating the success of the operation or a message if the
        reservation or hotel was not found.
        """
        # Check if the file exists
        if os.path.exists(self.filename):
            # Open the hotel data file
            with open(self.filename, 'r', encoding='UTF-8') as file:
                hotels_data = json.load(file)

            # Iterate through each hotel in the data
            for hotel in hotels_data:
                # Check if the hotel name matches the specified hotel
                if hotel['name'] == hotel_name:
                    # If the hotel is found, retrieve the list of reservations
                    for reservation in hotel['reservations']:
                        # Check if the customer name matches the specified
                        if reservation['customer_name'] == customer_name:
                            # If the reservation is found, update the hotel
                            # data
                            room_type = reservation['room_type']
                            # Update the room count for the specified room type
                            hotel['rooms'][room_type] += 1
                            # Remove the reservation from the list of
                            # reservations
                            hotel['reservations'].remove(reservation)
                            # Write the updated hotel data to the file
                            with open(self.filename, 'w',
                                      encoding='UTF-8') as file:
                                json.dump(hotels_data, file, indent=4)
                            # Return a success message
                            return f'Reservation canceled for {customer_name}'
                    # If the specified reservation is not found, return an
                    # error
                    return f'No reservation found for {customer_name}'
            # If the specified hotel is not found, return an error message
            return f'Hotel {hotel_name} not found'
        # If the file does not exist, return an error message
        return 'Hotel information not found, please verify'
