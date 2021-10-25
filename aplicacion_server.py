#!/usr/bin/env python3

import socket

from Calefaccion import Calefaccion
from funciones import OnOf

PORT = 50001

# Creacion de las diferentes calefacciones
calefaccion1 = Calefaccion('1', 'sala', False, 25.4)
calefaccion2 = Calefaccion('2', 'cocina', False, 18.3)
calefaccion3 = Calefaccion('3', 'habitacion', False, 25.2)
calefaccion4 = Calefaccion('4', 'baño', False, 10.4)
# Lista de las calefacciones
calefacciones = [calefaccion1, calefaccion2, calefaccion3, calefaccion4]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('', 50001))

# Lista de comandos
commands = ["ONN", "OFF", "NAM", "NOW", "GET", "SET"];

while True:
    mensaje, dir_cli = s.recvfrom(1024)

    # Guarda el valor de el metodo connect() de la clase calefaccion
    connect = True;

    # La cadena que se enviara al cliente
    sol = "";

    mensaje = mensaje.decode()

    # Comando que inserta el cliente
    comando = mensaje[0:3]

    # Array de los parametros que inserta el usuario
    parametros = mensaje[3:len(mensaje)].split(':')

    # Comprobar si el comando introducido es correcto
    if comando not in commands:
        sol = "-1"

    # Ejecucion de los comandos:
    if comando == "ONN":
        print("ha usado el comando ONN")
        sol=OnOf(parametros, calefacciones, True, '-11')

    if comando == "OFF":
        print("ha usado el comando OFF")
        sol=OnOf(parametros, calefacciones, False, '-12')

    if comando == "NAM":
        print("ha usado el comando NAM")
        if parametros == ['']:
            sol = "{}".format(calefacciones[0].toString())
            err = calefacciones[0].connect
            i = 1
            while i < len(calefacciones) and connect == True:
                sol = "{}:{}".format(sol, calefacciones[i].toString())
                print(sol)
                connect = calefacciones[i].connect()
                i = i + 1
            if connect:
                sol = "+{}".format(sol)
            else:
                sol = "-13"
        else: 
            sol="-2"

    if comando == "NOW":
        print("ha usado el comando NOW")
        if parametros == ['']:
            sol=":".join([str(x.temperatura).replace('.','') for x in calefacciones])
        elif len(parametros)>1:
            sol="-2"
        else:
            t=[]
            for calefaccion in calefacciones:
                for parametro in parametros:
                    if(parametro==calefaccion.id):
                        print(parametro)
                        t.append(calefaccion.temperatura)
                
            sol=":".join([str(x).replace('.','') for x in t])
        


    if comando == "GET":
        print("ha usado el comando GET")
    if comando == "SET":
        print("ha usado el comando SET")
        cpCalefacciones=calefacciones
        if parametros == ['']:
            sol="-3"
        elif len(parametros[0])!=3:
            sol="-4"
        elif len(parametros)==1:
            for calefaccion in calefacciones:
                calefaccion.temperatura=parametros[0]
        elif len(parametros)==2:
            for calefaccion in calefacciones:
                if calefaccion.id==parametros[1]:
                    calefaccion.temperatura=parametros[0]
        elif len(parametros)>2:
            sol ="-2"
        else:
            calefacciones=cpCalefacciones
            sol="-16"

    s.sendto(sol.encode(), dir_cli)
s.close()
