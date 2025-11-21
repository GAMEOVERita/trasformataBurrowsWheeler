import socket
import bwt
import threading
#TCP

HOST = "127.0.0.1"
PORT = 1984 # letteralmente 1984

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind( (HOST,PORT) ) #assegno al socket l'ip e la porta
    
    s.listen(1) #in ascolto per connessioni
    print(f"Server in ascolto su {HOST}:{PORT}")

    conn, addr = s.accept() # conn oggetto che rasppresenta la connessione, addr è l'indirizzo del client che si connette
    # conn è una risorsa, posso aprirla, chiuderla e gestirla
    with conn:
        print(f"connesso con {addr}")
        
        while True:
            data = conn.recv(1024) #riceve max 1024 Byte
            #se data è vuoto il client ha interrotto la connessione inaspettatamente
            if not data:
                break

            stringaDaTrasformare = data.decode() #traduce e decodifica il messaggio ricevuto
            #tip -> messaggio sarà convertito in trasformata

            trasformata = bwt.trasformata(stringaDaTrasformare)


            conn.sendall(trasformata.encode()) # converte il messaggio in byte per inviarlo tramite socket

            


#https://www.geeksforgeeks.org/python/command-line-arguments-in-python/