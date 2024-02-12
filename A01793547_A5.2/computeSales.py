import json
import time

"""
Sales Computation Script

This script is designed to compute total sales amounts
based on product catalog and sales data stored in JSON files.
It calculates the total sales amount and writes the results to a text file.

Usage:
Run the script with Python 3: python3 computeSales.py TC

Dependencies:
- Python 3
- Required Python modules: json, time, sys

Input:
- priceCatalogue.json (str): Path to the JSON file
containing product catalog information.
- salesRecord.json (str): Path to the JSON file containing sales information.

Output:
- Prints total sales amount and elapsed time.
- Writes total sales and elapsed time information
to the "salesResult.txt" file.

Example:
python3 computeSales.py TC

Student: Eddie Guadalupe Elorza Ruiz
Student ID: A01794404
Date: February 11, 2024
"""


# Function to load JSON data from a file
def load_json(filename):
    """
    Read data from a JSON file.
    Args:
        filename (str): The path to the JSON file.
    Returns:
        list: The data read from the JSON file.
    """
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{filename}'.")
        return None


# Function to compute the total cost of sales
def compute_total_cost(price_catalogue, sales_record):
    """
    Compute the total cost of sales.
    Args:
        price_catalogue (list): Product catalog information.
        sales_record (list): Sales information.
    Returns:
        float: The total cost of sales.
    """
    total_cost = 0
    for sale in sales_record:
        product_name = sale["Product"]
        quantity = sale["Quantity"]
        found = False
        for product in price_catalogue:
            if product["title"] == product_name:
                total_cost += product["price"] * quantity
                found = True
                break
        if not found:
            print(f"Warning: Product '{product_name}'"
                  f" not found in the price catalogue.")
    return total_cost


# Function to print and save the results
def print_and_save_results(total_cost, elapsed_time, result_index):
    """
    Print and save the results.
    Args:
        total_cost (float): The total cost of sales.
        elapsed_time (float): The elapsed time.
        result_index (int): The index of the result.
    """
    print(f"TOTAL TC{result_index}: {total_cost:.2f},"
          f"Time: {elapsed_time:.4f} seconds")
    with open("salesResult.txt", "a") as file:
        file.write(f"TC{result_index} Total Cost: {total_cost:.2f},"
                   f" Time: {elapsed_time:.4f} seconds\n")


if __name__ == "__main__":
    with open("salesResult.txt", "w") as file:
        file.write("")  # Clearing the contents of the file

    for i in range(1, 4):
        start_time = time.time()

        price_catalogue_file = f"TC{i}/priceCatalogue.json"
        sales_record_file = f"TC{i}/salesRecord.json"

        price_catalogue = load_json(price_catalogue_file)
        sales_record = load_json(sales_record_file)

        if price_catalogue is None or sales_record is None:
            continue

        total_cost = compute_total_cost(price_catalogue, sales_record)
        elapsed_time = time.time() - start_time

        print_and_save_results(total_cost, elapsed_time, i)
