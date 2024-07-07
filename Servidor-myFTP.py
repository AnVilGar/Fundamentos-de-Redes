#ANTONIO VÍLCHEZ GARCÍA#

import socket
import os

#Creamos un socket#
s4=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Enlazamos el socket a una dirección y puerto específico(solo en el servidor)#
s4.bind(('localhost', 5252))

while True:
    informacion_cl, IPcliente = s4.recvfrom(2048)

    #Comparamos el mensaje que nos ha llegado y enviamos una respuesta#
    if informacion_cl.decode()=='LS':
        #Devolvemos una lista con los nombres de los archivos que acaban en .txt#
        archivos_texto = list(filter(lambda x: x.endswith('.txt'), os.listdir()))
        #Enviamos los archivos al cliente#
        s4.sendto(' - '.join(archivos_texto).encode(), IPcliente)
        
        
    #Ponenmos .startswith('GET') para verificar si el mensaje recibido desde el cliente comienza con GET#
    elif informacion_cl.decode().startswith('GET'):
        #Devolvemos el segundo elemento de la lista resultante (el nombre del archivo se encuentra en la segunda posición de la lista, ya que ponemos GET nombre.txt)#
        arch=informacion_cl.split()[1]
        #Comprobamos si existe el archivo#
        if os.path.exists(arch):
            #Abrimos el archivo en modo de lectura binaria "rb"#
            archivo=open(arch, 'rb')
            try:
                #Enviamos el contenido del archivo al cliente#
                s4.sendto(archivo.read(), IPcliente)
            finally:
                #Cerramos el archivo#
                archivo.close()
        else:
            #Enviamos el mensaje de error al cliente#
            respuesta='Error: el archivo no se encuentra en este directorio o no existe'
            s4.sendto(respuesta.encode(), IPcliente)
          
          
    #Ponenmos .startswith('PUT') para verificar si el mensaje recibido desde el cliente comienza con PUT#
    elif informacion_cl.decode().startswith('PUT'):
        #Devolvemos el segundo elemento de la lista resultante (el nombre del archivo se encuentra en la segunda posición de la lista, ya que ponemos PUT nombre.txt)#
        arch1=informacion_cl.split()[1]
        #Abrimos el archivo en modo escritura binaria para quese puedan escribir datos en el archivo como una secuencia de bytes.
        archivo1=open(arch1,'wb')
        try:
            informacion, direccion_cl = s4.recvfrom(2048)
            archivo1.write(informacion)
        finally:
            archivo1.close()
    else:
        # Enviamos el mensaje de error al cliente#
        respuesta1='ERROR'
        s4.sendto(respuesta1.encode() , direccion_cl)

#Cerramos el socket#
s4.close()