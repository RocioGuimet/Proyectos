

def calculadora():
    bienvenida()
def bienvenida():
    print('Bienvenido a tu calculadora simple:\n')
    
#Preguntar al usuario la acción a realizar 
    preguntar = True
    while preguntar:
        print('¿Qué operación deseas realizar?:')
        print('1) Suma:')
        print('2) Resta:')
        print('3) Multiplicación:')
        print('4) División:')
        print('5) Salir')

        try:
            opcion = int(input('Seleccione una opción: \n'))
        except ValueError:
            print("Debes ingresar un número del menú")
        match opcion:
            case 1:
                num1 = int(input('Ingresa el primer valor:'))
                num2 = int(input('Ingresa el segundo valor:'))
                print(f'La suma de {num1} + {num2} es igual a {num1 + num2}')

            case 2:
                num1 = int(input('Ingresa el primer valor:'))
                num2 = int(input('Ingresa el segundo valor:'))
                print(f'La resta de {num1} - {num2} es igual a {num1 - num2}')

            case 3:
                num1 = int(input('Ingresa el primer valor:'))
                num2 = int(input('Ingresa el segundo valor:'))
                print(f'La multiplicación de {num1} * {num2} es igual a {num1 * num2}')

            case 4:
                num1 = int(input('Ingresa el primer valor:'))
                num2 = int(input('Ingresa el segundo valor:'))
                print(f'La división de {num1} / {num2} es igual a {num1 / num2}')

            case 5:
                print ('Cerrando calculadora...') #Mensaje de despedida
                preguntar = False #Cierro el bucle

            case _: print ('Opción inválida')

        
calculadora()
