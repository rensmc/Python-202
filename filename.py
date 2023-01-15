import os

files = []

# Getting the filenames of our csv files in the current directory

def read_filenames():
    for file in os.listdir():
        if ".csv" in file:
            files.append(file)
        else:
            continue

#print(os.listdir())
read_filenames()
print(files)