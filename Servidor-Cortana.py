#ANTONIO VÍLCHEZ GARCÍA#

import socket
import time

#Creamos un socket#
s2=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Enlazamos el socket a una dirección y puerto específico(solo en el servidor)#
s2.bind(('localhost', 2525))

while True:
   
    #Recibimos el mensaje y la direccion del cliente (que la usaremos para enviarle la IP)#
    informacion_cl, IPcliente = s2.recvfrom(2048)

    #Comparamos el mensaje que nos ha llegado y enviamos una respuesta#
    if informacion_cl==b'HOLA':
        respuesta='BUENOS DIAS'
        
    elif informacion_cl==b'HORA':
        respuesta=time.ctime()
        
    elif informacion_cl==b'IP_CLIENTE':
        #Le enviamos la IP#
        respuesta=IPcliente[0]
    
    #Si no es ninguno de los mensajes de arriba salta un error#
    else:
        respuesta=f'ERROR: {len(informacion_cl)}'

    #Enviamos la respuesta al cliente en bytes#
    s2.sendto(respuesta.encode(), IPcliente)

#Cerramos el socket#
s2.close()