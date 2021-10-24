import socket, sys
PORT = 50001
# Comprueba que se ha pasado un argumento.
if len( sys.argv ) != 2:
    print( "Uso: {} <servidor>".format( sys.argv[0] ) )
    exit( 1 )

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print( "Introduce el mensaje que quieres enviar (mensaje vacío paraterminar):" )

dir_serv = (sys.argv[1], 50001)

while True:
    mensaje = input()
    if not mensaje:
        break
    s.sendto(mensaje.encode(), dir_serv)

    mensaje_echo= s.recv(1024)
    print(mensaje_echo.decode())

s.close()