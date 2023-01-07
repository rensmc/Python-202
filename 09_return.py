# funcions: default parameters and multiple returns

def find_volume(length=1, width=1, depth=1): # length=1 - default parameter: 1.
    return length * width * depth

print(f"find_volume() => {find_volume()}")
print(f"find_volume(10, 20, 3) => {find_volume(10, 20, 3)}")
print(f"find_volume(width=10) => {find_volume(width=10)}")

print("-" * 25)

def find_volume(length=1, width=1, depth=1): # length=1 - default parameter: 1.
    return length * width * depth, width, 'hola'

result, width, text = find_volume(width=10)
print(result)
print(width)
print(text)