dict = {}
for i in range(1, 5):
    dict[i] = i * 2
print(dict)

dict_v2 = { i: i * 2 for i in range(1, 5)} # Dictionary Comprehension
print(dict_v2) 

print('-' * 20)

import random
countries = ['col', 'mex', 'bol', 'pe']
population = {}
for country in countries:
    population[country] = random.randint(1, 100)
print(population)

population_v2 = {country: random.randint(1, 100) for country in countries}
print(population_v2) # Dictionary Comprehension

print('-' * 20)

names = ['nico', 'zule', 'santi']
ages = [12, 56, 98]
print(list(zip(names, ages))) #Join both lists

new_dict = {name: age for (name, age) in zip(names, ages)}
print(new_dict)


'''
{
    'nico': 12,
    'zule': 56,
    'santi': 98
}
'''
