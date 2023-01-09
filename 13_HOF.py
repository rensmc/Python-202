# High Order Functions

def increment(x):
    return x +1

def high_order_func(x, func): # receiving parameters: x and a function
    return x + func(x)

result = high_order_func(2, increment)
# result = 2 + (2 + 1)
print(result)

# Ex. High Order Function using Anonimous Functions: Lambda

increment_v2 = lambda x: x + 1
high_order_func_v2 = lambda x, func: x + func(x)
result = high_order_func_v2(2, increment_v2)
print(result)