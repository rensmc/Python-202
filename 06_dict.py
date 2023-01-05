# Dictionary Comprehension: Conditions


import random
countries = ['col', 'mex', 'bol', 'pe']

population_v2 = {country: random.randint(1, 100) for country in countries}
print(population_v2) # Dictionary Comprehension

result = {country: population for (country, population) in population_v2.items() if population > 20 }
print(result) # Dictionary Comprehension with Condition

text = 'Hola, soy Rene'
unique = { c: c.upper() for c in text if c in 'aeiou' }
print(unique)