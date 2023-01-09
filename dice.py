# Roll the dice

import random

roll = 'y'
while roll == 'y':
    roll = input("Do you want to roll the dice? y/n => ")
    roll = roll[0].lower()
    if roll == 'y':
        sides = int(input("How many sides? => "))
        dice = random.randint(1,sides)
        print(f"The dice is rolling... you got a {dice}")
    else:
        print('Bye bye')