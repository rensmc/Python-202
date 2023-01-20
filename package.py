# Namespace for importing functions from modules
from pkg.mod_1 import func_1, func_2 
import pkg # importing mod_2 with a different method. see /pkg/__init__.py

print(func_1())
print(func_2())


print(pkg.mod_2.func_3())
print(pkg.mod_2.func_4())


print(pkg.URL)
print(pkg.mod_1.func_1()) # Example: Unnecesary reference