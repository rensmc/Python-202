import csv

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter= ',')
        header = next(reader) # Using an iterable to identify the first column and use it as key.
        data = []
        #print(header)
        for row in reader:
            iterable = zip(header, row) # Joining header and row in the same tuple.
            #print(list(iterable))
            #Converting tuple into a dictionary with dictionary comprehension.
            country_dict = {key: value for key, value in iterable} 
            data.append(country_dict) # Creating a list of all the dictionaries.
            #print(data)
        return data

if __name__ == '__main__':
    data = read_csv('./app/data.csv')
    #print(data) # The whole file, organized into a list of dictionaries.
    print(data[0]) # Just the first record of the file.
    print(f'\nRecords in the list = {len(data)}') #Printing the number of records in the list.