# r+ = adding read and also write permissions.
# w+ = overwriting the file you are working with.
with open('./text.txt', 'r+') as file: 
    for line in file: 
        print(line)
    file.write('\nWriting new stuff on the file')

