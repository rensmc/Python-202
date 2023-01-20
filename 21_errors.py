#print(0 / 0)
#print(result)
print('hello')

suma = lambda x, y: x + y
assert suma(2,2) == 4

print('hello again')

age = 10
if age < 18:
    raise Exception('Hey man, you are under age')

"""
Errors in Python:

SyntaxError
ZeroDivisionError
NameError
AssertionError

https://www.w3schools.com/python/python_ref_exceptions.asp

"""