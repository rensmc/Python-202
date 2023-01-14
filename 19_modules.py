import sys # Allows us to know about the state of the OS
print(sys.path[0])

import re # Regular expressions
text = "My phone number is 555 555555, country code is 55 and my lucky number is also 5"
result = re.findall("[0-9]+", text) # Find every number in the string.
print(result)

import time # Date and time
timestamp = time.time() # Time in Unix format
print(timestamp)

local = time.localtime() # Local time
result = time.asctime(local) # Formats the date
print(result)

import collections # Mainly for managing lists
numbers = [1, 1, 2, 1, 2, 1, 4, 5, 3, 3, 21]
counter = collections.Counter(numbers) # Creates a dictionary with the frecuency of each number
print(counter)