"""
number_converter.py

This script processes numerical data from text files within a specified folder,
converts each number to binary and hexadecimal bases,
displays the results, writes the results to a text file,
and shows encountered exceptions and total execution time at the end.

Author: Eddie Elorza
Date: February 3, 2024
"""

import os
import time

FOLDER_PATH = "P2"
FILE_EXTENSION = ".txt"
OUTPUT_FILE_NAME = "ConversionResults.txt"


def convert_number_to_bases(number: int) -> tuple:
    """
    Convert a number to binary and hexadecimal bases.

    :param number: The number to be converted
    :return: A tuple containing the binary and hexadecimal representations
    """
    binary_representation = format(number, 'b')
    hexadecimal_representation = format(number, '02X')
    return binary_representation, hexadecimal_representation


def convert_numbers_in_file(file_path: str, output_file, error_list) -> None:
    """
    Convert numbers in a file to binary and hexadecimal bases.

    :param file_path: Path to the file
    :param output_file: File object to write the results
    :param error_list: List to store encountered exceptions
    :return: None
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            output_file.write(f"\nConverting numbers in file: {file_path}\n")
            for line in file:
                try:
                    num = int(line.strip())
                    binary, hexadecimal = convert_number_to_bases(num)
                    result_line = f"Original: {num}\tBinary: {binary}\tHexadecimal: {hexadecimal}\n"
                    print(result_line)
                    output_file.write(result_line)

                except ValueError as ve:
                    error_list.append(f"Invalid data in {file_path}. Skipping line: {line.strip()}. Error: {ve}")

    except FileNotFoundError as e:
        print(f"File not found: {file_path} ({e})")
    except IOError as e:
        print(f"IOError: {e}")


def convert_numbers_in_folder(folder_path: str) -> list:
    """
    Convert numbers in all text files in a folder to binary and hexadecimal bases.

    :param folder_path: Path to the folder
    :return: List of encountered exceptions
    """
    error_list = []
    with open(OUTPUT_FILE_NAME, 'w', encoding='utf-8') as output_file:
        file_list = [f for f in os.listdir(folder_path) if f.endswith(FILE_EXTENSION)]

        for file_name in file_list:
            file_path = os.path.join(folder_path, file_name)
            convert_numbers_in_file(file_path, output_file, error_list)

    return error_list


if __name__ == "__main__":
    start_time = time.time()

    try:
        if not os.path.isdir(FOLDER_PATH):
            raise FileNotFoundError(f"Invalid folder path: {FOLDER_PATH}")

        errors = convert_numbers_in_folder(FOLDER_PATH)
        print(f"\nResults written to {OUTPUT_FILE_NAME}")

        if errors:
            print("\nEncountered exceptions:")
            for error in errors:
                print(error)

    finally:
        total_time = time.time() - start_time
        print(f"Total execution time: {total_time} seconds")
