# Secure Password Generator

import random

length = int(input("Please indicate the password's length => "))
mayus = ('ABCDEFGHIJKLMNOPQRSTUVXYZ')
minus = ('abcdefghijklmnopqrstuvwxyz')
numbers = ('1234567890')
symbols = ('|@!#$%&/()=?¡^-*')
chars = mayus + minus + numbers + symbols

password = "".join(random.sample(chars,length))
print(password)