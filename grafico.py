
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



def main():
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
    window = Tk()

    window.title("Proyecto SGE")

    window.geometry('600x300')

    lblNombre = Label(window, text="Introduce aqui tu nombre")
    lblPass = Label(window, text="Contraseña:")
    lblPassCompleta = Label(window, text="")
    lblNombre.grid(column=0, row=0)
    lblPass.grid(column=0, row=1)
    lblPassCompleta.grid(column=0, row=2, columnspan = 2)
    nombrelbl = Entry(window, width=10)
    nombrelbl.focus()
    nombrelbl.grid(column=1, row=0)

    def show(self):
        self.update()
        self.deiconify()

    def hide(self):
        self.update()
        self.withdraw()

    def abrirVentanaContrasena():
        window.withdraw()
        window.deiconify()
        windowPass = Tk()
        windowPass.title("Contraseña personalizada")
        windowPass.geometry('600x275')
        lblNumeros = Label(windowPass, text="¿Quieres que tu contraseña contenga números?")
        lblSimbolos = Label(windowPass, text="¿Quieres que tu contraseña contenga simbolos?")
        lblMayusculas = Label(windowPass, text="¿Quieres que tu contraseña contenga mayusculas?")
        lblMinusculas = Label(windowPass, text="¿Quieres que tu contraseña contenga minusculas?")
        lblNumeros.grid(column=0, row=0)
        lblSimbolos.grid(column=0, row=1)
        lblMayusculas.grid(column=0, row=2)
        lblMinusculas.grid(column=0, row=3)

        btnVolver = Button(windowPass, text="Volver", command=windowPass.withdraw())
        btnVolver.grid(column=0, row=4)
        windowPass.mainloop()

    def generarContrasenaRandom():

        longitud = random.randint(8, 32)
        listadelistas = [listaMayusculas, listaMinusculas, listaNumeros, listaSimbolos]
        contrasena = ""
        for x in range(0, longitud):
            numrandom = random.randint(0, 3)
            numramdonlista = random.randint(0, len(listadelistas[numrandom]) - 1)
            contrasena = contrasena + listadelistas[numrandom][numramdonlista]
            seguridad = 0
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
        '''if seguridad <= 2:
            print(color('Su contraseña es poco segura', 'red'))
        elif seguridad <= 4:
            print(color('Su contraseña es segura', 'green'))'''


        res = "Hola " + nombrelbl.get()
        lblPassCompleta.configure(text=contrasena)

    btnPassRandom = Button(window, text="Generar contraseña aleatoria", command=generarContrasenaRandom)
    btnPassEscoger = Button(window, text="Contraseña personalizada", command=abrirVentanaContrasena)
    btnPassRandom.grid(column=4, row=1)
    btnPassEscoger.grid(column=5, row=1)

    window.mainloop()





if __name__ == '__main__':
    main()



