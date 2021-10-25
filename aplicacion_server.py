#!/usr/bin/env python3

import socket

from Calefaccion import Calefaccion
from funciones import OnOf

PORT = 50001

# Creacion de las diferentes calefacciones
calefaccion1 = Calefaccion('1', 'sala', False, 25)
calefaccion2 = Calefaccion('2', 'cocina', False, 18)
calefaccion3 = Calefaccion('3', 'habitacion', False, 30)
calefaccion4 = Calefaccion('4', 'baño', False, 27)
# Lista de las calefacciones
calefacciones = [calefaccion1, calefaccion2, calefaccion3, calefaccion4]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('', 50001))

# Lista de comandos
commands = ["ONN", "OFF", "NAM", "NOW", "GET", "SET"]
ids = []
for calefaccion in calefacciones:
    ids.append(calefaccion.id)


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
        print("ha usado el comando OFF")
        sol = OnOf(parametros, calefacciones, True, '-11')

    if comando == "OFF":
        print("ha usado el comando OFF")
        sol = OnOf(parametros, calefacciones, False, '-12')

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

    if comando == "NOW":
        print("ha usado el comando NOW")
        if parametros == ['']:
            for calefaccion in calefacciones:
                print('id:', calefaccion.id, 'temperatura:',
                      calefaccion.temperatura)
        else:
            for calefaccion in calefacciones:
                for parametro in parametros:
                    if parametro == calefaccion.id:
                        print('id:', calefaccion.id, 'temperatura:',
                              calefaccion.temperatura)

    if comando == "GET":
        print("ha usado el comando GET")
    if comando == "SET":
        print("ha usado el comando SET")

    s.sendto(sol.encode(), dir_cli)
s.close()


def errorHandling(command):
    if not command in commnads:
        sol = "-1"
        return sol

    else:
        if command == "SET":
            if len(parametros) == 2:
                if parametro[0] == "":
                    sol = -3
                    return sol
                else:
                    if not len(parametros[0]) == 3 and not checkId(parametros[0]):
                        sol = "-4"
                        return sol

                    else:
                        try:
                            temperatura = int(parametros[1])
                        except:
                            sol = "-4"
                            return sol

        if command == "GET":
            if len(parametros) > 0:
                if not checkId(parametros[0]):
                    sol = "-4"
                    return sol

        if command == "NAM":
            if len(parametros):
                sol = "-2"
                return sol

        if command == "OFF" or command == "ONN" or command == "NOW":
            for parametro in parametros:
                if not checkId(parametro):
                    sol = "-4"
                    return sol
                    break


def checkId(id):
    if id in ids:
        return True
    else:
        return False
