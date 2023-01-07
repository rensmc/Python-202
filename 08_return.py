# funcions: return

sum = 0
for x in range(1, 10):
    sum += x
print(sum)
#1, 2, 3, 4, 5, 6


def sum_with_range(min, max):
    print(f"parameters: {min} - {max}")
    sum = 0
    for x in range(min, max):
        sum += x
    return sum

result = sum_with_range(1, 10)
print(f"return: {result}")
result_2 = sum_with_range(result, result + 10)
print(f"return: {result_2}")


print(sum_with_range(1, 100))

"""
sum_with_range(1, 10)
sum_with_range(20, 30)
sum_with_range(1, 100)
"""
