from termcolor import colored as color
import random
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



def creacionDatos():
    global usuarios
    global departamentos
    '''
    La logica que he seguido es que si esta lista fuera una base de datos, antes de insertar los datos
    siempre los transformaria a mayusculas para que a la hora de comparar los datos no de problema
    '''
    usuarios = [["ALEJANDRO", "A23441ASDF", "MARKETING", "alejandroperez@gmail.com"], ["EKAITZ", "ASEF432Q562ASDF", "VENTAS", "ekaitz@gmail.com"], ["JUAN", "ase4fm349", "COMPRAS", "juanfrancisco@gmail.com"]
        , ["MARIO", "AS34Rasrg", "ALMACEN", "mariozaton@gmail.com"]]
    departamentos = ["VENTAS", "COMPRAS", "MARKETING", "ALMACEN", "ADMINISTRACION"]
    inicio()

def inicio():
    print(color('Introduce el nombre de usuario que desees:', 'green'))
    nombre = input()
    if nombre.upper() in usuarios:
        print(color('El nombre de usuario ya existe, pruebe otra vez..', 'red'))
        inicio()
    else:
        contrasena = generadorContrasena()
    departamento = preguntarDpto()
    email = preguntarEmail()
    user = [nombre, contrasena, departamento, email]
    print(color('Usuario añadido correctamente', 'green'))

    usuarios.append(user)
    print(color('Sus datos son:\n'
                'Nombre: '+ nombre+'\n'
                'Contraseña: '+str(contrasena)+'\n'
                'Departamento: '+str(departamento)+'\n'
                'Email: '+ str(email), 'yellow'))

    print(color('Ahora mismo hay '+str(len(usuarios))+' usuarios', 'white'))
    mandarCorreo(user)

def mandarCorreo(user):
    server = smtplib.SMTP('smtp.gmail.com: 587')
    msg = MIMEMultipart()

    message = "Usuario: "+str(user[0])+"\nContraseña: "+str(user[1])+"\nDepartamento: "+str(user[2])

    password = "Jm12345Jm"
    msg['From'] = "pruebapythonalejandro@gmail.com"
    msg['To'] = str(user[3])
    msg['Subject'] = "Informacion creacion usuario"
    msg.attach(MIMEText(message, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login(msg['From'], password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    print("Se ha enviado correctamente el correo %s:" % (msg['To']))
    server.quit()


def preguntarEmail():
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    print(color('Introduzca su correo electronico', 'green'))
    email = input()
    if re.fullmatch(regex, email):
        print(color('Correo electronico insertado', 'blue'))
        return email
    else:
        print(color('Correo incorrecto, por favor compruebalo', 'red'))
        preguntarEmail()


def preguntarDpto():
    print(color('Escoge tu nuevo departamento:', 'green'))

    for x in departamentos:
        print(color(str(departamentos.index(x))+": "+x,'yellow'))

    departamento = input()
    if departamento.isnumeric():
        if 4 >= int(departamento) >= 0:
            return departamentos[int(departamento)]
        else:
            print(color("Por favor introduce un departamento valido", 'red'))
            preguntarDpto()





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


    contrasena = crearContrasena(longitud, minusculas, mayusculas, simbolos, numeros)
    return contrasena



def crearContrasena(longitud, minusculas, mayusculas, simbolos, numeros):
    contrasena = ""
    listaMinusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                       'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    listaMayusculas = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    listaNumeros = ['1','2','3','4','5','6','7','8','9','0']
    listaSimbolos = ['!','@','#','*','?']
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
    while x < int(longitud):
        numeroRandom = random.randint(0, len(listadelistas)-1)
        numerorandom2 = random.randint(0,len(listadelistas[numeroRandom])-1)
        contrasena = contrasena + listadelistas[numeroRandom][numerorandom2]
        x = x +1

    print(color("Su nueva contraseña es = ", 'blue')+color(contrasena, 'red'))
    return contrasena











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