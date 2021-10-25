#!/usr/bin/env python3

import socket

from Calefaccion import Calefaccion
PORT = 50001



calefaccion1=Calefaccion('1','sala',False,25)
calefaccion2=Calefaccion('2','cocina',False,18)
calefaccion3=Calefaccion('3','habitacion',False,30)
calefaccion4=Calefaccion('4','baño',False,27)
calefacciones=[calefaccion1,calefaccion2,calefaccion3,calefaccion4]


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('', 50001))

while True:
    mensaje, dir_cli = s.recvfrom(1024)
    mensaje= mensaje.decode()
    comando=mensaje[0:3]

    parametros=mensaje[3:len(mensaje)].split(':')
    if(comando=="ONN"):
        print("ha usado el comando ONN")
        print(parametros)
        if(parametros==['']):
            for calefaccion in calefacciones:
                calefaccion.status=True
        else:
            for calefaccion in calefacciones:
                for parametro in parametros:
                    if(parametro==calefaccion.id):
                        calefaccion.status=True
        for calefaccion in calefacciones: 
            print(calefaccion.status)
    if(comando=="OFF"):
        print("ha usado el comando OFF")
        if(parametros==['']):
            for calefaccion in calefacciones:
                calefaccion.status=False
        else:
            for calefaccion in calefacciones:
                for parametro in parametros:
                    if(parametro==calefaccion.id):
                        calefaccion.status=False
        for calefaccion in calefacciones: 
            print(calefaccion.status)
    if(comando=="NAM"):
        print("ha usado el comando NAM")
        if(parametros==['']):
            sol="{}".format(calefacciones[0].toString())
            for i in range(1,len(calefacciones)):
                sol="{}:{}".format(sol,calefacciones[i].toString())
                print(sol)
    if(comando=="NOW"):
        print("ha usado el comando NOW")
        if(parametros==['']):
            for calefaccion in calefacciones:
                print('id:',calefaccion.id,'temperatura:',calefaccion.temperatura)
        else:
            for calefaccion in calefacciones:
                for parametro in parametros:
                    if(parametro==calefaccion.id):
                        print('id:',calefaccion.id,'temperatura:',calefaccion.temperatura)

    if(comando=="GET"):
        print("ha usado el comando GET")
    if(comando=="SET"):
        print("ha usado el comando SET")
    
    s.sendto(sol.encode(), dir_cli)
s.close()
