def triangle_area():
    base = int(input('Ingrese el valor de la base del triangulo?: '))
    height = int(input('Ingrese el valor de la altura del triangulo: '))
    area = (base * height)/2
    print('El area del triangulo es: ' + str(area))

def type_triangle2():
    sides = int(input('¿Cuantos de los lados tienen la misma longitud?: '))
    if sides == 0:
        print('Es un triangulo Escaleno')
    elif sides == 2:
        print('Es un triangulo Isoceles')
    elif sides == 3:
        print('Es un triangulo equilatero')
    else:
        print('Numero de lados erroneo')
        type_triangle2()

def type_triangle():
    angles = input('¿El triangulo tiene algun angulo recto, Si o No: ')
    angles = angles.lower()
    if angles == 'si':
        print('Es un triangulo rectangulo')
    else:
        type_triangle2()

introduction = '''
Hola

Este programa te ayudara a saber el area de un triangulo 
y su tipo, solamente tienes que saber su base y altura,
ademas de saber cuantos lados son iguales.

Comencemos!
'''

midpoint = '''
Bien
Ya sabemos su area, ahora solo nos falta
saber que tipo de triangulo es.

¿Listo?
'''

def run():
    print(introduction)
    triangle_area()
    print(midpoint)
    type_triangle()


if __name__ == '__main__':
    run()