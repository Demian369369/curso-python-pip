import random 
print("""
      [juego de Piedra, Papel o Tijera]
                  >>> Elige un objeto <<<
      """)
def choose_options():
    options = ('piedra', 'papel', 'tijera')
    user_option = input('>>> Piedra, Papel o Tijera => ').lower()
    if not user_option in options:
        print('Esa opción no es valida')
        return None, None 
    computer_option = random.choice(options)
    print('¡Usuario option => ', user_option)
    print('Computer option => ', computer_option)
    return user_option, computer_option
def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print('Empate!\n')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('🪨  >  ✂️')
            print('¡Usuario gana!\n')
            user_wins += 1
        else:
            print('📄  >  🪨')
            print('¡Computer gana!\n')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('📄  >  🪨')
            print('¡Usuario gana!\n')
            user_wins += 1
        else:
            print('✂️  >  📄')
            print('¡Computadora gana!\n')
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('✂️  >  📄')
            print('¡Usuario gana!\n')
            user_wins += 1
        else:
            print('🪨  >  ✂️')
            print('¡Computadora gana!\n')
            computer_wins += 1
    return user_wins, computer_wins

def check_winner(user_wins, computer_wins):
    print(f'''
    computadora: {computer_wins}
    Usuario: {user_wins}
            ''')
    if user_wins == 3:
        print('El ganador es Usuario')
        exit()
    if computer_wins == 3:
        print('El ganador es Computadora')
        exit()

def run_game():
    computer_wins = 0 
    user_wins = 0
    rounds = 1

    while True:
        print('***' * 10)
        print('Round ', rounds)
        print('***' * 10)
        rounds += 1
        user_option, computer_option = choose_options()
        user_wins, computer_wins = check_rules(user_option, computer_option,user_wins, computer_wins)
        check_winner(user_wins, computer_wins)         
run_game()