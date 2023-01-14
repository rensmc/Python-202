import os

files = []

# Getting the filenames of our cdv files in the current directory
for file in os.listdir():
    if ".py" in file:
        continue
    if os.path.isfile(file):
        files.append(file)
print(files)
#print(os.listdir())