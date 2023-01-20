# Handling errors individually
try:
    print(0 / 0) # The error
except ZeroDivisionError as error:
    print(error)

try:
    assert 1 != 1, 'Not equal' # The error
except AssertionError as error:
    print(error)

try:
    age = 10
    if age < 18:
        raise Exception('Hey man, you are under age') # The error
except Exception as error:
    print(error)

print('Hello')


# Handling all errors at once
try:
    print(0 / 0) # The error
    assert 1 != 1, 'Not equal' # The error
    age = 10
    if age < 18:
        raise Exception('Hey man, you are under age') # The error
except ZeroDivisionError as error:
    print(error)
except AssertionError as error:
    print(error)
except Exception as error:
    print(error)