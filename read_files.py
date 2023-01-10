# Count the number of lines in a CSV

# import module
import pandas as pd

# List with the names of the files. The csv files and this file should be hosted on the same folder.
files = [
    'this_is_a_csv_file1.csv',
    'this_is_a_csv_file2.csv',
    'this_is_a_csv_file3.csv',
    'this_is_a_csv_file4.csv'
]

# Counts the numbers of rows on every file in files{}.
for file in files:
    results = pd.read_csv(str(file), sep=',', index_col=False, dtype='unicode', low_memory=False, on_bad_lines='skip')
    print(str(file)) # Prints the filename
    print(len(results)) # Prints the number of records it contains