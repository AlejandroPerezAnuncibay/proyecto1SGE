from termcolor import colored as color



def creacionDatos():
    global usuarios
    '''
    La logica que he seguido es que si esta lista fuera una base de datos, antes de insertar los datos
    siempre los transformaria a mayusculas para que a la hora de comparar los datos no de problema
    '''
    usuarios = ["ALEJANDRO", "EKAITZ", "JUAN", "MARIO"]
    inicio()

def inicio():
    print(color('Introduce el nombre de usuario que desees:', 'green'))
    nombre = input()
    if nombre.upper() in usuarios:
        print(color('El nombre de usuario ya existe, pruebe otra vez..', 'red'))
        inicio()
    else:
        usuarios.append(nombre.upper())
        print(color('Usuario añadido correctamente', 'green'))
        generadorContrasena()


def generadorContrasena():
    print(color('A continuación generaremos una contraseña..', 'green'))
    longitud = pedirLongitud()
    minusculas = pedirMinusculas()
    mayusculas = pedirMayusculas()
    simbolos = pedirSimbolos()
    numeros = pedirNumeros()
    seguridad = 0
    if int(longitud) < 8:
        resultado = contrasenaLongitud()
        if resultado:
            longitud = 8
            seguridad = seguridad + 1

    else:
        seguridad = seguridad + 1
    if minusculas:
        seguridad = seguridad + 1
    if mayusculas:
        seguridad = seguridad + 1
    if simbolos:
        seguridad = seguridad + 1
    if numeros:
        seguridad = seguridad + 1
    if seguridad <= 2:
        print(color('Su contraseña es poco segura', 'red'))
    elif seguridad <= 4:
        print(color('Su contraseña es de seguridad media', 'green'))
    else:
        print(color('Su contraseña es de seguridad alta', 'blue'))


    crearContrasena(longitud, minusculas, mayusculas, simbolos, numeros)


def crearContrasena(longitud, minusculas, mayusculas, simbolos, numeros):
    listaMinusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                       'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    #todo
    '''Tengo que importar simbolos, mayusculas y numeros. Despues hacer que genere la contaseña'''



def contrasenaLongitud():
    print(color('Su contraseña tiene menos de 8 caracteres, se recomienda por su seguridad que '
                'tenga más de 8 caracteres. ¿Quiere establecerla de 8 caracteres?', 'red'))
    print(color('1. Modificar\n2. Continuar'))
    opcion = input()
    if opcion == "1":
        return True
    elif opcion == "2":
        return False
    else:
        print(color('Por favor escoja una opción existente...', 'red'))
        contrasenaLongitud()


def pedirNumeros():
    print(color('¿Quieres que tu contraseña contenga números? (si o no)', 'green'))
    respuesta = input()
    if respuesta.lower() == "si":
        return True
    elif respuesta.lower() == "no":
        return False
    else:
        print(color('Por favor introduce si o no...', 'red'))
        pedirNumeros()



def pedirSimbolos():
    print(color('¿Quieres que tu contraseña contenga simbolos? (si o no)', 'green'))
    respuesta = input()
    if respuesta.lower() == "si":
        return True
    elif respuesta.lower() == "no":
        return False
    else:
        print(color('Por favor introduce si o no...', 'red'))
        pedirSimbolos()




def pedirMayusculas():
    print(color('¿Quieres que tu contraseña contenga mayusculas? (si o no)', 'green'))
    respuesta = input()
    if respuesta.lower() == "si":
        return True
    elif respuesta.lower() == "no":
        return False
    else:
        print(color('Por favor introduce si o no...', 'red'))
        pedirMayusculas()



def pedirMinusculas():
    print(color('¿Quieres que tu contraseña contenga minisuculas? (si o no)', 'green'))
    respuesta = input()
    if respuesta.lower() == "si":
        return True
    elif respuesta.lower() == "no":
        return False
    else:
        print(color('Por favor introduce si o no...', 'red'))
        pedirMinusculas()

def pedirLongitud():
    print(color('Introduce la longitud de la contraseña(tiene que ser un numero postivo y entero)', 'green'))
    longitud = input()
    if longitud.isnumeric:
        if int(longitud) > 0:
            return longitud
        else:
            print(color('El número introducido es incorrecto, por favor compruebe los requisitos...', 'red'))
            pedirLongitud()



if __name__ == '__main__':
    creacionDatos()