file = open('./text.txt')
#print(file.read()) # Reads the whole file.
#print(file.readline()) # Reads one line at a time.
#print(file.readline())
#print(file.readline())
#print(file.readline())
#print(file.readline())
#print(file.readline())

# Using a for loop instead of hardcoding each readline().
for line in file: 
  print(line)

file.close() # Stops reading file. Memory optimization.


with open('./text.txt') as file: # Same action. No close() needed.
  for line in file: 
    print(line)