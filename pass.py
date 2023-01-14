# Secure Password Generator

import random

length = int(input("Please indicate the password's length => "))
mayus = ('ABCDEFGHIJKLMNÑOPQRSTUVXYZ')
minus = ('abcdefghijklmnñopqrstuvwxyz')
numbers = ('1234567890')
symbols = ('|@!#$%&/()=?¡^-*')
chars = mayus + minus + numbers + symbols

password = ''
password = password.join(random.sample(chars,length))
print(password)
