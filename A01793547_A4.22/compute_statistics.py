"""
statistics_processor.py

This script processes numerical data from text files within a specified folder, 
calculates various statistical metrics for each file, and displays the results in a tabular format.

Author: Eddie Elorza
Date: February 3, 2024
"""

import os
import math
import time
from tabulate import tabulate

FOLDER_PATH = "P1"
FILE_EXTENSION = ".txt"
OUTPUT_FILE_NAME = "StatisticsResults.txt"


def process_file(file_path: str) -> list:
    """
    Process a file and calculate statistics.

    :param file_path: Path to the file
    :return: List of statistics [count, non-zero count,
    mean, median, mode, variance, std deviation, elapsed time]
    """
    try:
        start_time = time.time()
        with open(file_path, 'r', encoding='utf-8') as file:
            data = []
            for line in file:
                try:
                    data.append(float(line.strip()))
                except ValueError:
                    print(f"Invalid data in {file_path}. Skipping line: {line.strip()}")

            if not data:
                print(f"The file {file_path} does not contain valid numerical data.")
                return []

            count = len(data)
            mean = round(sum(data) / count, 2)
            sorted_data = sorted(data)
            median = sorted_data[count // 2] if count % 2 != 0 else (sorted_data[count // 2 - 1]
                                                                     + sorted_data[count // 2]) / 2

            try:
                mode = max(set(data), key=data.count)
            except ValueError:
                mode = "#N/A"

            std_deviation = round(math.sqrt(sum((x - mean) ** 2 for x in data) / count), 2)
            variance = round(sum((x - mean) ** 2 for x in data) / count,2)

            end_time = time.time()
            elapsed_time = round(end_time - start_time,2)

            return [count, count - data.count(0), mean, median,
                    mode, variance, std_deviation, elapsed_time]

    except FileNotFoundError as e:
        print(f"File not found: {file_path} ({e})")
    except IOError as e:
        print(f"IOError: {e}")
    return []


def process_files_in_folder(folder_path: str) -> list:
    """
    Process all text files in a folder and display statistics.

    :param folder_path: Path to the folder
    :return: List of lists containing statistics
    """
    results_table = []

    # List all files in the folder with the specified extension
    file_list = [f for f in os.listdir(folder_path) if f.endswith(FILE_EXTENSION)]

    # Process each file
    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)
        results = process_file(file_path)
        if results:
            results_table.append([file_name] + results)

    return results_table


def display_results(results_table: list) -> None:
    """
    Display the computed statistics in a table.

    :param results_table: List of lists containing statistics
    :return: None
    """
    headers = ["File", "Count", "Non-Zero Count", "Mean", "Median",
               "Mode", "Variance", "Std Deviation", "Elapsed Time"]
    print(tabulate(results_table, headers=headers, tablefmt="pretty"))


def write_results_to_file(results_table: list) -> None:
    """
    Write the computed statistics to an output file.

    :param results_table: List of lists containing statistics
    :return: None
    """
    with open(OUTPUT_FILE_NAME, 'w', encoding='utf-8') as output_file:
        headers = ["File"] + ["Count", "Non-Zero Count", "Mean", "Median",
                              "Mode", "Variance", "Std Deviation", "Elapsed Time"]
        output_file.write(tabulate(results_table, headers=headers, tablefmt="pretty"))


if __name__ == "__main__":
    if not os.path.isdir(FOLDER_PATH):
        print("Invalid folder path. Exiting.")
    else:
        total_start_time = time.time()
        results_table_doc = process_files_in_folder(FOLDER_PATH)
        total_end_time = time.time()

        if results_table_doc:
            display_results(results_table_doc)
            write_results_to_file(results_table_doc)
            print(f"Results written to {OUTPUT_FILE_NAME}")
            total_time = total_end_time - total_start_time
            print('Total time: ', total_time)