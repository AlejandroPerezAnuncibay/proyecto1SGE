# Imports de assets que utilizo en la aplicación
from termcolor import colored as color
import random
import re
import smtplib
import sys
import hashlib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import *






# Funcion que se encarga de generar los datos y comenzar la app
def creacionDatos():

    global usuarios  # Array de usuarios que voy a utilizar como base de datos
    global departamentos  # Array de departamentos que voy a utilizar como base de datos
    '''
    La logica que he seguido es que si esta lista fuera una base de datos, antes de insertar los datos
    siempre los transformaria a mayusculas para que a la hora de comparar los datos no de problema
    '''

    usuarios = [["ALEJANDRO", "A23441ASDF", "MARKETING", "alejandroperez@gmail.com"],
                ["EKAITZ", "ASEF432Q562ASDF", "VENTAS", "ekaitz@gmail.com"],
                ["JUAN", "ase4fm349", "COMPRAS", "juanfrancisco@gmail.com"]
        , ["MARIO", "AS34Rasrg", "ALMACEN", "mariozaton@gmail.com"]]
    departamentos = ["VENTAS", "COMPRAS", "MARKETING", "ALMACEN", "ADMINISTRACION"]

    global listaMinusculas
    global listaMayusculas
    global listaNumeros
    global listaSimbolos
    listaMinusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                          'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    listaMayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                       'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    listaNumeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    listaSimbolos = ['!', '@', '#', '*', '?']

    inicio()


# Funcion principal que se encarga de llamar al resto de funciones y de recoger los datos
def inicio():
    print(color('Introduce el nombre de usuario que desees:', 'green'))
    nombre = input()

    for x in usuarios:
        if x[0] == nombre.upper():
            print(color('El nombre de usuario ya existe, pruebe otra vez..', 'red'))
            inicio()

    if str.isspace(nombre) or len(nombre) == 0:
        print(color('El nombre no puede estar vacio, pruebe otra vez...', 'red'))
        inicio()

    contrasena = generadorContrasena()
    departamento = preguntarDpto()
    email = preguntarEmail()
    contrasenahash = hashlib.sha512(contrasena.encode())
    #Contraseña encriptada mediante el metodo sha512
    user = [nombre.upper(), contrasenahash.hexdigest(), departamento, email]
    print(color('Usuario añadido correctamente', 'blue'))

    usuarios.append(user)
    print(color('Sus datos son:\n'
                'Nombre: ' + nombre + '\n'
                'Contraseña: ' + contrasena+ '\n'
                'Departamento: ' + str(departamento) + '\n'
                'Email: ' + str(email), 'blue'))

    print(color('Ahora mismo hay ' + str(len(usuarios)) + ' usuarios', 'blue'))
    mandarCorreo(user)


# Funcion que se encarga de mandar el correo electronico con la informacion generada
def mandarCorreo(user):
    # Configuracion del servidor de correo electronico. En este caso he utilizado el de gmail
    server = smtplib.SMTP('smtp.gmail.com: 587')
    msg = MIMEMultipart()
    # Cuerpo del correo electronico
    message = "Usuario: " + str(user[0]) + "\nContraseña: " + str(user[1]) + "\nDepartamento: " + str(user[2])

    password = "Jm12345Jm"
    msg['From'] = "pruebapythonalejandro@gmail.com"
    msg['To'] = str(user[3])
    msg['Subject'] = "Informacion creación usuario"
    msg.attach(MIMEText(message, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login(msg['From'], password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    mensaje = "Se ha enviado correctamente el correo a %s" % (msg['To'])
    print(color(str(mensaje), 'red'))
    server.quit()
    sys.exit()


# Funcion que se encarga de recoger el correo electronico validado, se encarga de validarlo mediante un regex.

def preguntarEmail():
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    print(color('Introduzca su correo electronico', 'green'))
    email = input()
    if re.fullmatch(regex, email):
        print(color('Correo electronico insertado', 'blue'))
        return email
    else:
        print(color('Correo incorrecto, por favor compruebalo', 'red'))
        return preguntarEmail()

#Funcion que se encarga de pedir el departamento al que va a pertenecer el usuario
def preguntarDpto():
    print(color('Escoge tu nuevo departamento:', 'green'))

    for x in departamentos:
        print(color(str(departamentos.index(x)) + ": " + x, 'blue'))

    departamento = input()
    if departamento.isnumeric() and len(departamento) != 0 and str.isspace(departamento) is False:
        if 4 >= int(departamento) >= 0:
            return departamentos[int(departamento)]

    print(color("Por favor introduce un departamento valido", 'red'))
    return preguntarDpto()

#Funcion que se encarga de generar la contraseña

'''
En esta función lo que primero recojo es la longitud deseada por el usuario. No puede ser 0 ni vacio ni espacios
en blanco. En caso de que sea menor que 8 le aconsejare que ponga como minimo 8 caracteres. Tras ello le preguntaremos 
que tipo de caracteres va a querer que tenga su contraseña. Como minimo tendrá que aceptar uno. Depende de cuantos
tipos haya añadido, sumará 1 punto a seguridad, yendo de menos seguro a más.
'''

def generadorContrasena():
    print(color('1. Generar contraseña aleatoriamente\n'
          '2. Escoger opciones de contraseña', 'blue'))
    opcion = input()
    if opcion == "1":
        contrasena = generarRandom()
        return contrasena
    elif opcion == "2":
        contrasena = contrasenaOpciones()
        return contrasena
    else:
        print(color('Por favor introduce una opción valida...(1 o 2)', 'red'))
        return generadorContrasena()



def generarRandom():
    longitud = random.randint(8,32)
    listadelistas = [listaMayusculas, listaMinusculas, listaNumeros, listaSimbolos]
    contrasena = ""
    for x in range(0,longitud):
        numrandom = random.randint(0,3)
        numramdonlista = random.randint(0,len(listadelistas[numrandom]) -1)
        contrasena = contrasena + listadelistas[numrandom][numramdonlista]
        seguridad = 0
    print(color('Su nueva contraseña es: '+ contrasena, 'red'))
    minusculas = False
    mayusculas = False
    simbolos = False
    numeros = False
    for y in contrasena:
        if y in listaMinusculas:
            minusculas = True
        elif y in listaMayusculas:
            mayusculas = True
        elif y in listaSimbolos:
            simbolos = True
        elif y in listaNumeros:
            numeros = True
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
        print(color('Su contraseña es segura', 'green'))
    return contrasena



def contrasenaOpciones():
    print(color('A continuación generaremos una contraseña..', 'green'))
    longitud = pedirLongitud()
    minusculas = pedirdato('minusculas')
    mayusculas = pedirdato('mayusculas')
    simbolos = pedirdato('simbolos')
    numeros = pedirdato('numeros')
    seguridad = 0

    if longitud < 8:
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

    contrasena = crearContrasena(longitud, minusculas, mayusculas, simbolos, numeros)
    return contrasena

#Funcion que se encarga de generar la contraseña aleatoriamente
'''
Tengo un array con cada uno de los caracteres que se pueda utilizar. En caso de que el usuario diga que quiere usar
esos caracteres, se añadirá el array con esos caracteres a un array que los contendra todos, despues jugando
con los tamaños de los arrays. Primero se genera un número random con los arrays introducidos y despues uno con la
longitud del mismo, asi se escogera un array random y un caracter random.
'''
def crearContrasena(longitud, minusculas, mayusculas, simbolos, numeros):
    contrasena = ""
    listadelistas = []
    if minusculas:
        listadelistas.append(listaMinusculas)
    if mayusculas:
        listadelistas.append(listaMayusculas)
    if simbolos:
        listadelistas.append(listaSimbolos)
    if numeros:
        listadelistas.append(listaNumeros)
    x = 0
    if listadelistas == []:
        print(color('Su contraseña debe por lo menos contener un tipo de caracter, por favor escoja uno que si', 'red'))
        return generadorContrasena()
    else:
        while x < int(longitud):
            numeroRandom = random.randint(0, len(listadelistas) - 1)
            numerorandom2 = random.randint(0, len(listadelistas[numeroRandom]) - 1)
            contrasena = contrasena + listadelistas[numeroRandom][numerorandom2]
            x = x + 1

    print(color("Su nueva contraseña es = ", 'blue') + color(contrasena, 'red'))
    return contrasena

#Funcion encargada de comprobar que como minimo tenga 8 caracteres y en su defecto preguntar para cambiarlo.
def contrasenaLongitud():
    print(color('Su contraseña tiene menos de 8 caracteres, se recomienda por su seguridad que '
                'tenga más de 8 caracteres. ¿Quiere establecerla de 8 caracteres?', 'red'))
    print(color('1. Modificar\n2. Continuar', 'red'))
    opcion = input()
    if opcion == "1":
        return True
    elif opcion == "2":
        return False
    else:
        print(color('Por favor escoja una opción existente...', 'red'))
        return contrasenaLongitud()

#Funcion reutilizada para pedir los distintos tipos de caracteres que contendrá la contraseña.
def pedirdato(dato):
    print(color('¿Quieres que tu contraseña contenga ' + dato + '? (si o no)', 'green'))
    respuesta = input()
    if respuesta.lower() == "si":
        return True
    elif respuesta.lower() == "no":
        return False
    else:
        print(color('Por favor introduce si o no...', 'red'))
        return pedirdato(dato)

#Funcion encargada de comprobar la longitud introducida por el usuario para la contraseña
def pedirLongitud():
    print(color('Introduce la longitud de la contraseña(tiene que ser un numero postivo y entero)', 'green'))
    longitud = input()
    if len(longitud) != 0 and str.isdigit(longitud):
        if int(longitud) != 0:
            return int(longitud)

    print(color('El número introducido es incorrecto, por favor compruebe los requisitos...', 'red'))
    return pedirLongitud()


if __name__ == '__main__':
    creacionDatos()


