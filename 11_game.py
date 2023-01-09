# Juego de piedra, papel o tijera

import random

def choose_options():
    options = ('piedra', 'papel', 'tijera')
    user_option = input('Elige piedra, papel o tijera => ')
    user_option = user_option.lower()

    if not user_option in options:
        print('Esa opción no es válida 🚫')
        return None, None

    computer_option = random.choice(options)

    print(f"Tu rival ha elegido {computer_option}")
    return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print("Es un empate 😬")
        print(f'Rival: {computer_wins}pts - Tú {user_wins}pts')

    elif user_option == 'piedra':
        if computer_option == 'tijera':
            user_wins += 1
            print('Piedra gana a tijera')
            print('Has ganado! 🎉')
            print(f'Rival: {computer_wins}pts - Tú {user_wins}pts')
            
        else:
            computer_wins += 1
            print('Papel gana a piedra')
            print('Tu rival ha ganado 🫠')
            print(f'Rival: {computer_wins}pts - Tú {user_wins}pts')
            

    elif user_option == 'papel':
        if computer_option == 'piedra':
            user_wins += 1
            print('Papel gana a piedra')
            print('Has ganado! 🎉')
            print(f'Rival: {computer_wins}pts - Tú {user_wins}pts')
            
        else:
            computer_wins += 1
            print('Tijera gana a papel')
            print('Tu rival ha ganado 🫠')
            print(f'Rival: {computer_wins}pts - Tú {user_wins}pts')
            

    elif user_option == 'tijera':
        if computer_option == 'piedra':
            computer_wins += 1
            print('Piedra gana a tijera')
            print('Tu rival ha ganado 🫠')
            print(f'Rival: {computer_wins}pts - Tú {user_wins}pts')
            
        else:
            user_wins += 1
            print('Tijera gana a papel')
            print('Has ganado! 🎉')
            print(f'Rival: {computer_wins}pts - Tú {user_wins}pts')
            
    return user_wins, computer_wins

def run_game():
    computer_wins = 0
    user_wins = 0
    rounds = 1

    while True:

        print('-' * 20)
        print('ROUND ', rounds)
        print('-' * 20)

        rounds += 1

        user_option, computer_option = choose_options()
        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)

        if computer_wins == 3:
            print('-' * 20)
            print('Has perdido la partida 😥')
            break

        if user_wins == 3:
            print('-' * 20)
            print('Felicidades! Has ganado la partida! 🏆')
            break

run_game()