"""
This script contains all functions

The following guidelines must be implemented for best practices:

-> Include Comment after declaring a function, this will act as
docstring when this functions is called
-> Run Flake8 after every commit
-> Run black after every commit

TODO : Log errors

"""
import csv


def write_to_csv(new_row):
    """
    This functions takes a new row and appends it onto data.csv file that already exists.
    """
    with open('data/csv_dumps/data.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(new_row)
