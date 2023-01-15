# Count the number of lines in a CSV,
# add the number to each dictionary as row_count 
# and create a csv file with the results

# import module
import pandas as pd

# List of dictionaries with the names of the files. 
# The csv files and this file should be hosted on the same folder.
files = [
    {'filename': 'this_is_a_csv_file1.csv'},
    {'filename': 'this_is_a_csv_file2.csv'},
    {'filename': 'this_is_a_csv_file3.csv'},
    {'filename': 'this_is_a_csv_file4.csv'}
]

file_list = files.copy()
print("Reading files, please wait... ☕️")

# Counts the numbers of rows on every file in files{}. Adds it to the dictionary list as row_count
for file in file_list:
    results = pd.read_csv(str(file['filename']), sep=',', index_col=False, dtype='unicode', low_memory=False, on_bad_lines='skip')
    file['row_count'] = len(results)

# Saving results to a csv file.
df = pd.DataFrame(file_list) # declare dataframe
output = input("Name your file => ") # Ask the user for desired filename
df.to_csv(output + ".csv", sep=',', encoding='utf-8', index=False) # Creating csv file
#print(files)
print(f'Results have been succesfully saved on file: {output}.csv \nDone ✅')