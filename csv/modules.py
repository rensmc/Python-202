import os
import pandas as pd

# Getting the filenames of our csv files in the current directory
def read_filenames(files):
    for file in os.listdir():
        if ".csv" in file:
            files.append(file)
        else:
            continue


def read_files(files):
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