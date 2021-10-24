#!/usr/bin/env python3

import socket

from Calefaccion import Calefaccion
PORT = 50001



calefaccion1=Calefaccion('1',False)
calefaccion2=Calefaccion('2',False)
calefaccion3=Calefaccion('3',False)
calefaccion4=Calefaccion('4',False)
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
        if(len(parametros)==1):
            for calefaccion in calefacciones:
                calefaccion.status=True
        else:
            print("else")
            for calefaccion in calefacciones:
                for parametro in parametros:
                    if(parametro==calefaccion.id):
                        calefaccion.status=True
        for calefaccion in calefacciones: 
            print(calefaccion.status)
    if(comando=="OFF"):
        print("ha usado el comando OFF")
    if(comando=="NAM"):
        print("ha usado el comando NAM")
    if(comando=="NOW"):
        print("ha usado el comando NOW")
    if(comando=="GET"):
        print("ha usado el comando GET")
    if(comando=="SET"):
        print("ha usado el comando SET")
    
    s.sendto(mensaje, dir_cli)
s.close()
