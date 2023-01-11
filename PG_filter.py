"""
To solve this challenge, your challenge is to use the Python filter function and a lambda function to filter a list of words, returning a list of only those that meet the condition of having 4 or more letters.

The filter_by_length function will receive as input a list of words. Finally, the function will return the filtered list.

Example 1:

Input: ['amor', 'sol', 'piedra', 'día']
Output: [ 'amor', 'piedra' ]

Example 2:

Input: ['rosa', 'gol', 'pez', 'día', 'gafas']
Output: [ 'rosa', 'gafas' ]

Code:

def filter_by_length(words):
   # Escribe tu solución 👇
   return []

words = ['amor', 'sol', 'piedra', 'día']
response = filter_by_length(words)
print(response)
"""

def filter_by_length(words):
   # Escribe tu solución 👇
   result = filter(lambda words: len(words) >= 4, words)
   return list(result)

words = ['amor', 'sol', 'piedra', 'día']
response = filter_by_length(words)
print(response)