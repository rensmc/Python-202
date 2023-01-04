set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

# Union

set_c = set_a.union(set_b)
print(set_c)
print(set_a | set_b) #Does the union on the go. operator: |

# Intersection

set_c = set_a.intersection(set_b)
print(set_c) #Result: bol
print(set_a & set_b) #does the intersection on the go. operator: &

# Difference

set_c = set_a.difference(set_b)
print(set_c)
print(set_a - set_b) #does the differenciation on the go. operator: -

# Symmetric difference

set_c = set_a.symmetric_difference(set_b)
print(set_c)
print(set_a ^ set_b) #operator: ^