#Cliente de sockets simple en python
import socket

HOST = '127.0.0.1'  #Dirección IP del servidor
PORT = 65432        #Puerto del servidor

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        mensaje = input("Ingrese un mensaje para enviar al servidor (o 'salir' para terminar): ")
        if mensaje.lower() == 'salir':
            break
        s.sendall(mensaje.encode())
        data = s.recv(1024)
        print(f"Respuesta del servidor: {data.decode()}")