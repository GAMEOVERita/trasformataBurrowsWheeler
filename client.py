import socket

HOST = "127.0.0.1" #uguale al server
PORT = 1984 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect( (HOST, PORT) )# connessione al server

    #ilclient scrive al server
    s.sendall(input("scrivi la stringa che vuoi trasformare: ").encode())
    
    data = s.recv(1024) #ricevo eventuale posta dal server

    print (f"Stringa trasformata: {data.decode()}")