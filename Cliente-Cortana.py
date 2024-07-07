#ANTONIO VÍLCHEZ GARCÍA#

import socket

#Creamos un socket#
s1=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    mensaje=input('Introduzca un mensaje que se enviara al servidor: ')
    
    #Si el mensaje es FIN_CONEXION salimos del bucle#
    if mensaje=='FIN_CONEXION':
        break
    else:

        #Enviamos un mensaje al servidor con sendto (usamos encode() para#
        #pasar el mensaje a bytes (por defecto es utf-8)#
        s1.sendto(mensaje.encode(), ('localhost', 2525))
    
        #Recibimos una respuesta del servidor con recvfrom(tamaño del buffer)#
        respuesta, IPservidor=s1.recvfrom(2048)
        
        #Usamos respuesta.decode() ya que el mensaje del servidor nos llega en bytes y lo queremos en caracteres#
        print(f'La respuesta del servidor es: {respuesta.decode()}')

#Cerramos el socket#
s1.close()

