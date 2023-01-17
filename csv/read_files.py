import os
import sys
# Local imports
import modules as mdls

files = []

mdls.read_filenames(files)
print(files)

files = [
    {'filename': 'this_is_a_csv_file1.csv'},
    {'filename': 'this_is_a_csv_file2.csv'},
    {'filename': 'this_is_a_csv_file3.csv'},
    {'filename': 'this_is_a_csv_file4.csv'}
]

mdls.read_files(files)
print(files)