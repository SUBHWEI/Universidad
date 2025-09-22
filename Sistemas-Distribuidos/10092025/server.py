#Servidor de sockets simple en Python
import socket

HOST = '127.0.0.1'   #Dirección IP local
PORT = 65432         #pUERTO DE ESCUCHA

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Servidor escuchando en {HOST}:{PORT}")
    conn, addr = s.accept()
    with conn:
        print('Conectado por', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Recibido: {data.decode()}")
            respuesta = f"Servidor recibió: {data.decode()}"
            conn.sendall(respuesta.encode())