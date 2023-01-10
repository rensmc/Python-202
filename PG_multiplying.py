"""
Your challenge is to use Python's map function and a lambda function to transform a list of numbers. You must return a list in which each number in the original list is multiplied by two.

The function multiply_numbers will receive as input a list with numbers. Finally, the function will return the transformed list.

Example 1:

Input: [2, 4, 5, 6, 8]
Output: [4, 8, 10, 12, 16]

Example 2:

Input: [1, 1, -2, -3]
Output: [2, 2, -4, -6]
-------------------------------------------------------

def multiply_numbers(numbers):
    # Write your solution 👇
    return []

numbers = [1, 2, 3, 4]
response = multiply_numbers(numbers)
print(response)
"""

def multiply_numbers(numbers):
    # Write your solution 👇
    result = list(map(lambda x: x * 2, numbers))
    return result

numbers = [1, 2, 3, 4]
response = multiply_numbers(numbers)
print(response)