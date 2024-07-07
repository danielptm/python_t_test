# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import csv
import numpy as np
from scipy import stats

csv_file1 = 'data1.csv'
csv_file2 = 'data2.csv'


def read_csv(file):
    all_rows = []
    with open(file, 'r') as file:
        # Create a CSV reader
        csv_reader = csv.reader(file)

        # Initialize an empty list to store all rows

        # Iterate over each row in the CSV file
        for row in csv_reader:
            # Append the current row to the list of all rows
            all_rows.append(row)

        # Now all_rows is a list of lists, where each inner list represents a row from the CSV file
        # Print the entire list of rows
    return all_rows

def create_np_array_for_column(col, data):
    new_arr = []
    for d in data:
        new_arr.append(int(d[col]))
    return np.array(new_arr)

def do_test_for_groups(group1, group2):
    t_stat, p_value = stats.ttest_ind(group1, group2)

    # Interpret the results:
    alpha = 0.05
    print("pvalue: ")
    print(p_value)
    if p_value < alpha:
        print(
            "Reject the null hypothesis")
    else:
        print(
            "Fail to reject the null hypothesis")


def print_hi(name):
    rows1 = read_csv(csv_file1)
    rows2 = read_csv(csv_file2)

    # First question
    np1 = create_np_array_for_column(4, rows1)
    np2 = create_np_array_for_column(4, rows2)
    do_test_for_groups(np1, np2)

    # Second question
    np1 = create_np_array_for_column(5, rows1)
    np2 = create_np_array_for_column(5, rows2)
    do_test_for_groups(np1, np2)

    # Third question
    np1 = create_np_array_for_column(6, rows1)
    np2 = create_np_array_for_column(6, rows2)
    do_test_for_groups(np1, np2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
