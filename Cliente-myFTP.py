#ANTONIO VÍLCHEZ GARCÍA#

import socket

#Creamos un socket#
s3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    mensaje = input('Introduzca un mensaje que se enviara al servidor: ')

     #Si el mensaje es FIN_CONEXION salimos del bucle#
    if mensaje == 'FIN_CONEXION':
        break
    else:
    
        #Enviamos un mensaje al servidor con sendto (usamos encode() para#
        #pasar el mensaje a bytes (por defecto es utf-8)#
        s3.sendto(mensaje.encode(), ("localhost", 5252))
    
        respuesta, IPservidor = s3.recvfrom(2048)
        print(f'La respuesta del servidor es: {respuesta.decode()}')

#Cerramos el socket#
s3.close()