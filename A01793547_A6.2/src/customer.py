"""
Module for managing customer information within hotels.

Uses JSON file for data storage.

Libraries:
- json: Provides functions for reading and writing JSON data.
- Hotel: Class for managing hotel information and reservations.
"""
import json
from src.hotel import Hotel


class Customer:
    """
    A class to represent a customer and manage customer-related operations
    within hotels.

    Attributes:
    - hotel_filename (str): The filename for storing hotel data in JSON format.

    Methods:
    - create_customer: Creates a new customer for a specified hotel.
    - delete_customer: Deletes a customer from a specified hotel.
    - display_customer_info: Displays information about a specified customer
    in a specified hotel.
    - modify_customer_info: Modifies the name of a specified customer in a
    specified hotel.
    """
    def __init__(self, hotel_filename: str = 'hotels.json'):
        """
        Initializes a Customer object with the specified hotel data filename.

        Parameters:
        - hotel_filename: The filename for storing hotel data in JSON format.
                          Defaults to 'hotels.json'.
        """
        self.hotel_filename = hotel_filename

    def create_customer(self, hotel_name: str, customer_name: str):
        """
        Creates a new customer for a specified hotel.

        Parameters:
        - hotel_name: The name of the hotel.
        - customer_name: The name of the customer to create.

        Returns:
        A string indicating the success of the operation or a message if the
        hotel or customer was not found.
        """
        # Create a Hotel object
        hotel = Hotel(self.hotel_filename)
        # Open the hotel data file
        with open(hotel.filename, 'r', encoding='UTF-8') as file:
            hotels_data = json.load(file)

        # Iterate through each hotel in the data
        for hotel_data in hotels_data:
            # Check if the hotel name matches the specified hotel
            if hotel_data['name'] == hotel_name:
                # If the hotel is found, retrieve the list of customers
                customers = hotel_data['customers']
                # Create a new customer ID
                customer_id = len(customers) + 1
                # Append the new customer to the list of customers
                customers.append({'customer_id': customer_id,
                                  'customer_name': customer_name})
                # Write the updated hotel data to the file
                with open(hotel.filename, 'w', encoding='UTF-8') as file:
                    json.dump(hotels_data, file, indent=4)
                # Return a success message
                return f'Customer {customer_name} created for {hotel_name}'

        # If the specified hotel is not found, return an error message
        return (
            f'Customer {customer_name} not created. Hotel {hotel_name} '
            'not found'
            )

    def delete_customer(self, hotel_name: str, customer_name: str):
        """
        Deletes a customer from a specified hotel.

        Parameters:
        - hotel_name: The name of the hotel.
        - customer_name: The name of the customer to delete.

        Returns:
        A string indicating the success of the operation or a message if the
        hotel or customer was not found.
        """
        # Create a Hotel object
        hotel = Hotel(self.hotel_filename)

        # Open the hotel data file
        with open(hotel.filename, 'r', encoding='UTF-8') as file:
            hotels_data = json.load(file)

        # Iterate through each hotel in the data
        for hotel_data in hotels_data:
            # Check if the current hotel matches the specified hotel name
            if hotel_data['name'] == hotel_name:
                # If the hotel is found, retrieve the list of customers
                customers = hotel_data['customers']
                # Iterate through each customer in the list
                for customer in customers:
                    # Check if the current customer matches the specified
                    if customer['customer_name'] == customer_name:
                        # If the customer is found, remove it from the list
                        customers.remove(customer)
                        # Write the updated hotel data to the file
                        with open(hotel.filename, 'w',
                                  encoding='UTF-8') as file:
                            json.dump(hotels_data, file, indent=4)
                        # Return a success message
                        return f'Customer {customer_name} deleted'
        # If the specified hotel or customer is not found, return an error
        return f'Customer {customer_name} not found in {hotel_name}'

    def display_customer_info(self, hotel_name: str, customer_name: str):
        """
        Displays information about a specified customer in a specified hotel.

        Parameters:
        - hotel_name: The name of the hotel.
        - customer_name: The name of the customer.

        Returns:
        The information of the customer if found, otherwise a message
        indicating the customer was not found in the specified hotel.
        """
        # Create a Hotel object
        hotel = Hotel(self.hotel_filename)
        # Open the hotel data file
        with open(hotel.filename, 'r', encoding='UTF-8') as file:
            hotels_data = json.load(file)

        # Iterate through each hotel in the data
        for hotel_data in hotels_data:
            # Check if the current hotel matches the specified hotel name
            if hotel_data['name'] == hotel_name:
                # If the hotel is found, retrieve the list of customers
                customers = hotel_data['customers']
                # Iterate through each customer in the list
                for customer in customers:
                    # Check if the current customer matches the specified
                    if customer['customer_name'] == customer_name:
                        # If the customer is found, return the customer info
                        return customer
        # If the specified hotel or customer is not found, return an error
        return f'Customer {customer_name} not found in {hotel_name}'

    def modify_customer_info(self, hotel_name: str,
                             customer_name: str, new_customer_name: str):
        """
        Modifies the name of a specified customer in a specified hotel.

        Parameters:
        - hotel_name: The name of the hotel.
        - customer_name: The current name of the customer.
        - new_customer_name: The new name for the customer.

        Returns:
        A string indicating the success of the operation or a message if the
        hotel or customer was not found.
        """
        # Create a Hotel object
        hotel = Hotel(self.hotel_filename)
        # Open the hotel data file
        with open(hotel.filename, 'r', encoding='UTF-8') as file:
            hotels_data = json.load(file)

        # Iterate through each hotel in the data
        for hotel_data in hotels_data:
            # Check if the current hotel matches the specified hotel name
            if hotel_data['name'] == hotel_name:
                # If the hotel is found, retrieve the list of customers
                customers = hotel_data['customers']
                # Iterate through each customer in the list
                for customer in customers:
                    # Check if the current customer matches the specified
                    if customer['customer_name'] == customer_name:
                        # If the customer is found, update the customer name
                        customer['customer_name'] = new_customer_name
                        # Write the updated hotel data to the file
                        with open(hotel.filename,
                                  'w', encoding='UTF-8') as file:
                            json.dump(hotels_data, file, indent=4)
                        # Return a success message
                        return (
                            f'Customer name updated from {customer_name} to '
                            f'{new_customer_name}')
        # If the specified hotel or customer is not found, return an error
        return f'Customer {customer_name} not found in {hotel_name}'
