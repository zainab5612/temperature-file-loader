"""
Assignment 9: Reading and using the contents of a file
Submitted by Zainab Abdulhasan
Submitted: November 24, 2024

This program processes temperature data collected at the STEM Center. It includes functionalities
like loading a dataset, naming it, and verifying its contents.

Assignment History:
- Assignment 8: Dataset Class
- Assignment 7: Filter List
- Assignment 6: Bubble Sort using Recursion
- Assignment 5: Reverse a List using Recursion
- Assignment 4: Creating a Sensor List and Filter List
- Assignment 3: Implementing a Menu
- Assignment 2: Converting Celsius to another temperature unit
- Assignment 1: Printing lines of text to the screen
"""

import math


class TempDataset:
    """
    A class that manages temperature data for the STEM Center.

    Features:
    - Load temperature data from a file.
    - Count the number of loaded temperature samples.
    - Provide specific samples for debugging.
    """
    _num_objects = 0  # Tracks how many TempDataset objects are created

    def __init__(self):
        # Initialize attributes for the dataset and its name
        self._data_set = None
        self._name = "Unnamed"  # Default dataset name
        TempDataset._num_objects += 1  # Increment object count

    @property
    def name(self):
        # Get the name of the dataset
        return self._name

    @name.setter
    def name(self, value):
        # Update the dataset name, but ensure it's valid (3-20 characters)
        if isinstance(value, str) and 3 <= len(value) <= 20:
            self._name = value
        else:
            raise ValueError("Name must be a string between 3 and 20 characters.")

    @classmethod
    def get_num_objects(cls):
        # Return the number of TempDataset objects created
        return cls._num_objects

    def process_file(self, filename):
        """
        Load and process a temperature dataset from a CSV file.

        Args:
        filename (str): Name of the file to load.

        Returns:
        bool: True if the file loads successfully, False otherwise.
        """
        try:
            # Try opening and reading the file
            with open(filename, 'r') as file:
                self._data_set = []  # Start fresh with an empty dataset
                for line in file:
                    # Split the line into parts and check if it's a temperature reading
                    parts = line.strip().split(",")
                    if parts[3] != "TEMP":
                        continue  # Skip if it's not a temperature reading

                    # Convert parts to the appropriate data types
                    day = int(parts[0])
                    time = math.floor(float(parts[1]) * 24)  # Convert time to an hour (0-23)
                    sensor = int(parts[2])
                    temp = float(parts[4])

                    # Add the processed data as a tuple to the dataset
                    self._data_set.append((day, time, sensor, temp))
            return True  # File loaded successfully
        except FileNotFoundError:
            print("Error: The file was not found. Please check the filename.")
            return False
        except ValueError:
            print("Error: The file contains invalid data.")
            return False

    def get_loaded_temps(self):
        """
        Check if the dataset is loaded and return the number of samples.

        Returns:
        int or None: Number of loaded samples, or None if no data is loaded.
        """
        if self._data_set is None:
            return None
        return len(self._data_set)

    def get_sample_data(self, sample_indices):
        """
        Get specific samples from the dataset for debugging.

        Args:
        sample_indices (iterable): Indices of the samples to retrieve.

        Returns:
        list or None: List of samples, or None if no data is loaded.
        """
        if self._data_set is None:
            return None
        return [self._data_set[i] for i in sample_indices]


def print_header():
    """
    Display the project title and the author's name.
    """
    print("STEM Center Temperature Project")
    print("Zainab Abdulhasan")


def print_menu():
    """
    Display the main menu options for the program.
    """
    print("""
Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit
""")


def new_file(current_set):
    """
    Load a new dataset into the program.

    Args:
    current_set (TempDataset): The dataset object to load data into.
    """
    filename = input("Please enter the filename of the new dataset: ")
    if not current_set.process_file(filename):
        print("Unable to load the file. Please try again.")
        return

    # Confirm the number of samples loaded
    print(f"Loaded {current_set.get_loaded_temps()} samples")

    # Prompt the user for a valid dataset name
    while True:
        try:
            dataset_name = input("Please provide a 3 to 20 character name for the dataset: ")
            current_set.name = dataset_name
            break
        except ValueError as e:
            print(e)


def main():
    """
    The main function that drives the program.
    """
    current_set = TempDataset()  # Create a TempDataset object

    print_header()

    while True:
        print_menu()

        # If the dataset is loaded, display sample data for debugging
        if current_set.get_loaded_temps() is not None:
            print(current_set.get_sample_data(range(0, 5000, 1000)))

        try:
            choice = int(input("What is your choice? "))
            if choice == 1:
                new_file(current_set)
            elif choice == 7:
                print("Thank you for using the STEM Center Temperature Project")
                break
            else:
                print("Feature not implemented yet.")
        except ValueError:
            print("*** Please enter a number only ***")
        print()


if __name__ == "__main__":
    main()



"""
"C:\\Users\\zandu\\python projects\\assignment-9.py\\.venv\\Scripts\\python.exe" "C:\\Users\\zandu\\python projects\\assignment-9.py\\Assignment-9.py" 
STEM Center Temperature Project
Zainab Abdulhasan

Main Menu
---------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by date and time
6 - Show histogram of temperatures
7 - Quit

What is your choice? 1
Please enter the filename of the new dataset: Temperatures2022-03-07.csv
Loaded 11724 samples
Please provide a 3 to 20 character name for the dataset: 
"""