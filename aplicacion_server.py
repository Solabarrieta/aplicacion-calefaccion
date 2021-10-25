#!/usr/bin/env python3

import socket

from Radiador import Radiador
from funciones import OnOf,checkId

PORT = 50001

# Creacion de las diferentes calefacciones
radiador1 = Radiador('1', 'sala', False, 25.4)
radiador2 = Radiador('2', 'cocina', False, 18.3)
radiador3 = Radiador('3', 'habitacion', False, 25.2)
radiador4 = Radiador('4', 'bano', False, 10.4)
# Lista de las calefacciones
radiadores = [radiador1, radiador2, radiador3, radiador4]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('', 50001))

# Lista de comandos
commands = ["ONN", "OFF", "NAM", "NOW", "GET", "SET"]
ids = []
for radiador in radiadores:
    ids.append(radiador.id)


while True:
    mensaje, dir_cli = s.recvfrom(1024)

    # Guarda el valor de el metodo connect() de la clase calefaccion
    connect = True

    # La cadena que se enviara al cliente
    sol = ""

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
        #errorHandling()
        print("ha usado el comando ONN")
        sol=OnOf(parametros, radiadores, True, '-11')

    if comando == "OFF":
        print("ha usado el comando OFF")
        sol = OnOf(parametros, radiadores, False, '-12')

    if comando == "NAM":
        print("ha usado el comando NAM")
        if parametros == ['']:
            sol = "{}".format(radiadores[0].toString())
            err = radiadores[0].connect
            i = 1
            while i < len(radiadores) and connect == True:
                sol = "{}:{}".format(sol, radiadores[i].toString())
                print(sol)
                connect = radiadores[i].connect()
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
            sol = ":".join([str(x.temperatura).replace('.', '')
                            for x in radiadores])
            sol="+{}".format(sol)
        elif len(parametros) > 1:
            sol = "-2"
        else:
            t = []
            for radiador in radiadores:
                for parametro in parametros:
                    if parametro == radiador.id:
                        print(parametro)
                        t.append(radiador.temperatura)
            if(checkId(parametros[0],ids)):
                sol = ":".join([str(x).replace('.', '') for x in t])
                sol="+{}".format(sol)
            else:
                sol="-14"

    if comando == "GET":
        print("ha usado el comando GET")
    if comando == "SET":
        print("ha usado el comando SET")
        cpRadiadores = radiadores
        if parametros == ['']:
            sol = "-3"
        elif len(parametros[0]) != 3:
            sol = "-4"
        elif len(parametros) == 1:
            if int(parametros[0]) >= 0:
                for radiador in radiadores:
                    radiador.temperatura = parametros[0]
                sol="+"
            else:
                sol="-4"
        elif len(parametros) == 2:
            for radiador in radiadores:
                if int(parametros[0]) >= 0:
                    if radiador.id == parametros[1]:
                        radiador.temperatura = parametros[0]
                        sol="+"
                else:
                    sol="-4"
        elif len(parametros) > 2:
            sol = "-2"
        else:
            radiadores = cpRadiadores
            sol = "-16"

    s.sendto(sol.encode('ascii'), dir_cli)
s.close()