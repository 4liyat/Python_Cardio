def cilinder_volume():
    radius = float(input('Especifique el radio del cilindro: '))
    height = float(input('Especifique la altura del mismo: '))
    volume = 3.14159 * (radius ** 2) * height
    volume = round(volume,2)
    print('El volumen es ' + str(volume) + 'cm³')

def cube_volume():
    side = float(input('Especifique el largo del lado: '))
    volume = side ** 3
    volume = round(volume,2)
    print('El volumen es ' + str(volume) + 'cm³')

def sphere_volume():
    radius = float(input('Especifique el radio de la esfera: '))
    volume = (3.14159 * (radius ** 3)) * (4/3)
    volume = round(volume,2)
    print('El volumen es ' + str(volume) + 'cm³')

menu = '''
Bienvenido

Este programa te ayudara a calcular el volumen de unas figuras geometricas

🎁El programa solo funciona con centimetros, por lo que todos los datos que
se usan deben ser centimetros🎁

Selecciona una opcion para continuar:

1- Volumen de un cilindro
2- Volumen de un cubo
3- Volumen de una esfera

: '''

def run():
    choice = input(menu)
    if choice == '1':
        cilinder_volume()
    if choice == '2':
        cube_volume()
    if choice == '3':
        sphere_volume()
    else:
        print('Opcion incorecta, adios😘')


if __name__ == '__main__':
    run()