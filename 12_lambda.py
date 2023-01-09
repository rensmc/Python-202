# anonimous functions: Lambda

def increment(x):
    return x + 1

result = increment(10)
print(result)

# Ex. Using Lambda:

increment_v2 = lambda x : x + 1
result = increment_v2(11)
print(result)

full_name = lambda name, last_name : f'Full name: {name.title()} {last_name.title()}'
text = full_name('rene', 'mejia')
print(text)