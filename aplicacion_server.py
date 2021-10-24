#!/usr/bin/env python3

import socket
PORT = 50001

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('', 50001))

while True:
    mensaje, dir_cli = s.recvfrom(1024)
    

    s.sendto(mensaje, dir_cli)
s.close()
