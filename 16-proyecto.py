import os

#Carpeta de contactos
CARPETA = 'contactos/' #Mayúscula es una constante, NO modificar el valor de la capeta
EXTENSION = '.txt' #Extensión de archivos

#Contactos
class Contacto:
    def __init__(self, nombre, telefono, categoria):
        self.nombre = nombre
        self.telefono = telefono
        self.categoria = categoria

def app():
    crear_directorio()

#Preguntar al usuario la acción a realizar 
    preguntar = True
    while preguntar:
        mostrar_menu()
        try:
            opcion = int(input('Seleccione una opción: \r\n'))
        except ValueError:
            print("Debes ingresar un número del menú")


#Ejecutar las opciones
        if opcion == 1:
            agregar_contacto()
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contactos()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        elif opcion == 6:
            cerrar_agenda()
            preguntar = False
        else:
            print('Opción inválida, intente de nuevo')

def cerrar_agenda():
    print('Cerrando agenda de contactos...')

def eliminar_contacto():
    nombre = input('Escriba el contacto que desea eliminar: \r\n')

    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print ('¡Contacto eliminado correctamente!')
    except:
        print ('No pudimos encontrar ese contacto, prueba con otro nombre')

    app()

def buscar_contacto():
    nombre = input('Escriba el contacto que desea buscar: \r\n')

    try:
        with open (CARPETA + nombre + EXTENSION) as contacto:
            print ('Información del contacto: \r\n')
            for linea in contacto:
                print(linea.rstrip())
    except IOError:
        print('El contacto no existe')

    #Reiniciar la app
    app()

def mostrar_contactos():
    archivos = os.listdir(CARPETA)

    #Acá iría la consulta SQL en bases de datos
    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)] #Sólo archivos terminados en TXT
    if not archivos_txt:
        print("No hay contactos guardados")

    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                
                #Imprime los contenidos
                print(linea.rstrip(), end=" ")
                #Imprime un separador entre contactos (fuera del for)
            print('\r\n')
    app()

def editar_contacto():
    print('Vas a editar un contacto ya existente')
    nombre_anterior = input ('Nombre del contacto que desees editar: \r\n')

    #Revisar si existe antes de editarlo
    existe = os.path.isfile(CARPETA + nombre_anterior + EXTENSION)

    if existe: 
        with open (CARPETA + nombre_anterior + EXTENSION, 'w') as archivo:

            #Agregamos el resto de los campos
            nombre_contacto = input('Nuevo nombre: \r\n')
            telefono_contacto = input('Nuevo teléfono: \r\n')
            categoria_contacto = input('Nueva categoría: \r\n')

            #Instanciar
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            #Escribir en el archivo
            archivo.write('Nombre: '+ contacto.nombre + '\r\n')
            archivo.write('Telefono: '+ contacto.telefono + '\r\n')
            archivo.write('Categoria: '+ contacto.categoria + '\r\n')

        #Renombrar el archivo
        os.rename(CARPETA + nombre_anterior + EXTENSION, CARPETA + nombre_contacto + EXTENSION)
            
        #Mostrar mensaje de exito
        print('\r\n ¡Contacto modificado correctamente! \r\n')
    else:
        print ('Ese contacto no existe')

    #Reiniciar la app
    app()

def agregar_contacto():
    print('Ingresa los datos del nuevo contacto')
    nombre_contacto = input('Nombre: \r\n')

    #Revisar si el archivo existe
    existe = os.path.isfile(CARPETA + nombre_contacto + EXTENSION)

    if not existe:
        with open (CARPETA + nombre_contacto + EXTENSION, 'w') as archivo:  

            #Resto de campos
            telefono_contacto = input('Teléfono: \r\n')
            categoria_contacto = input('Categoría: \r\n')

            #Instanciar
            contacto = Contacto(nombre_contacto, telefono_contacto, categoria_contacto)

            #Escribir en el archivo
            archivo.write('Nombre: '+ contacto.nombre + '\r\n')
            archivo.write('Telefono: '+ contacto.telefono + '\r\n')
            archivo.write('Categoria: '+ contacto.categoria + '\r\n')

            #Mensaje de éxito
            print('\r\n ¡Contacto creado correctamente! \r\n')
    else:
        print('Nombre de contacto ya existente')

    app() #Reiniciar la app

def mostrar_menu():
    print('Selecciona una acción del menú:')
    print('1) Agregar nuevo contacto') #C
    print('2) Editar contacto') #U
    print('3) Ver contactos') #R
    print('4) Buscar contacto')
    print('5) Borrar contacto') #D
    print('6) Salir de la agenda')

def crear_directorio():
    if not os.path.exists(CARPETA): #Si la carpeta no existe, la crea
        os.makedirs(CARPETA)

def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)

app()
