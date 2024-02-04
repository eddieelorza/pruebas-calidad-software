"""
word_frequency_counter.py

This script processes text files within a specified folder,
counts the frequency of distinct words in each file,
sorts the results based on word frequency, and
writes the sorted word frequency to an output file.

Author: Eddie Elorza
Date: February 3, 2024
"""

import os
import time
import string

FOLDER_PATH = "P3"
FILE_EXTENSION = ".txt"
OUTPUT_FILE_NAME = "WordCountResults.txt"


def count_word_frequency_in_file(file_path: str, output_file) -> None:
    """
    Count the frequency of distinct words in a file.

    :param file_path: Path to the file
    :param output_file: File object to write the results
    :return: None
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            output_file.write(f"\nCounting word frequency in file: {file_path}\n")

            # Create a dictionary to store word frequencies
            word_frequency = {}

            for line in file:
                # Remove punctuation and convert to lowercase
                line = line.translate(str.maketrans('', '', string.punctuation))
                words = line.lower().split()

                for word in words:
                    word_frequency[word] = word_frequency.get(word, 0) + 1

            # Sort the dictionary by values (word frequencies)
            sorted_word_frequency = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)

            # Write sorted results to the output file
            for word, frequency in sorted_word_frequency:
                result_line = f"{word}: {frequency}\n"
                print(result_line)
                output_file.write(result_line)

    except FileNotFoundError as e:
        print(f"File not found: {file_path} ({e})")
    except IOError as e:
        print(f"IOError: {e}")


def count_word_frequency_in_folder(folder_path: str) -> None:
    """
    Count the frequency of distinct words in all text files in a folder.

    :param folder_path: Path to the folder
    :return: None
    """
    with open(OUTPUT_FILE_NAME, 'w', encoding='utf-8') as output_file:
        # List all files in the folder with the specified extension
        file_list = [f for f in os.listdir(folder_path) if f.endswith(FILE_EXTENSION)]

        # Count word frequency in each file
        for file_name in file_list:
            file_path = os.path.join(folder_path, file_name)
            count_word_frequency_in_file(file_path, output_file)


if __name__ == "__main__":
    start_time = time.time()

    try:
        if not os.path.isdir(FOLDER_PATH):
            raise FileNotFoundError(f"Invalid folder path: {FOLDER_PATH}")

        count_word_frequency_in_folder(FOLDER_PATH)
        print(f"\nResults written to {OUTPUT_FILE_NAME}")

    finally:
        total_time = time.time() - start_time
        print(f"Total execution time: {total_time} seconds")
