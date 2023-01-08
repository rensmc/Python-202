
"""
________________________________________
_____________________________           |
____________________         |          |
________            |        |          |
Local   | Enclosing | Global | Built-in |
Scope   | Scope     | Scope  |          |
________|           |        |          |
____________________|        |          |
_____________________________|          |
________________________________________|

"""


price = 100 # global

def increment():
    price = 200 # Local varible
    result = price + 10 # Local varible
    return result
    print(result)

print(price)
increment()
#print(result) # Error: Result is a local varible and is out of scope.
