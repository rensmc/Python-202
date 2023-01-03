set_countries = {'col', 'mex', 'bol'}
print(set_countries)
print(type(set_countries))

set_numbers = {1, 2, 2, 3, 443, 23} #2 is ignored. can't have duplicates.
print(set_numbers)

set_types = {1, "hola", False, 12.12}
print(set_types)

set_from_string = set('hola')
print(set_from_string)

set_from_tuple = set(('abc', 'cbv', 'as', 'abc'))
print(set_from_tuple)

numbers = [1, 2, 3, 1, 2, 3, 4]
set_numbers = set(numbers)
print(set_numbers)

unique_numbers = list(set_numbers)
print(unique_numbers)

#sets can be modified
#sets do not have an order
#sets can't have duplicates
#Set in spanish = Conjuntos