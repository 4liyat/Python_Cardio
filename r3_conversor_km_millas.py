menu ='''
Bienvenido al conversor de kilometros a millas y vicerveras
¿Que unidades quieres convertir?:

1- Kilometros
2- Millas

Selecciona una opcion. 1 o 2: '''

def run():
    option = int(input(menu))
    if option == 1:
        km = float(input('¿Cuantos kilometros quieres convertir: '))
        convertion = km / 1.609344
        convertion = round(convertion,3)
        print('Son ' +str(convertion)+ ' millas')
    elif option == 2:
        miles = float(input('¿Cuantas millas quieres convertir: '))
        convertion = miles * 1.609344
        convertion = round(convertion,3)
        print('Son ' +str(convertion)+ ' millas')
    else:
        print('Opcion incorrecta, adios')


if __name__ == '__main__':
    run()