def run():
    t_limit = int(input('Ingrese el limite superior: '))
    b_limit = int(input('Ingrese el limite inferior: '))
    choice = int(input('Escoja un valor: '))
    start = True

    while start:
        if choice in range(b_limit, t_limit):
            print('el valor ' + str(choice) + ' se encuentra dentro del rango')
            start = False
        elif choice in range(t_limit, b_limit):
            print('el valor ' + str(choice) + ' se encuentra dentro del rango')
            start = False
        else:
            print('el valor ' + str(choice) + ' se encuentra fuera de los limites')
            choice = int(input('Escoja un valor: '))
   

if __name__ == '__main__':
    run()