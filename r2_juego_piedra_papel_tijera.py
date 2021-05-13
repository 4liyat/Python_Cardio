def user_choices():
    option = input('Ingrese su opcion: ')
    if option == 'piedra':
        choice_user = 'a'
    elif option == 'tijeras':
        choice_user = 'b'
    elif option == 'papel':
        choice_user = 'c'
    return choice_user

def game():
    machine = 'a'
    user = user_choices()
    new_game = user + machine
    if new_game == 'c'+'a':
        print('Ganaste esta ronda')
    elif new_game == 'b'+'a':
        print('Perdiste esta ronda')
    else: 
        print('Empate')

intro = '''
Bienvenido ✨✨✨

Vamos a jugar piedra, papel o tijera

Tienes 3 intentos para ganarle a la maquina
Buena suerte~! 🎉
'''

def run():
    print(intro)
    game()    


if __name__ == '__main__':
    run()