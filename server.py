import socket, bwt, json, keyboard, threading, sys
#TCP

HOST = "127.0.0.1"
PORT = 1984 # letteralmente 1984
shutdown_flag = False

def key_listener():
    global shutdown_flag
    print("Press CTRL+Z to stop the server safely.")
    keyboard.wait("ctrl+z")
    shutdown_flag = True

# Start keyboard listener in background
threading.Thread(target=key_listener, daemon=True).start()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT)) #assegno al socket l'ip e la porta
    
    s.listen() #in ascolto per connessioni
    print(f"Server listening {HOST}:{PORT}")

    while not shutdown_flag:

        conn, addr = s.accept() # conn oggetto che rasppresenta la connessione, addr è l'indirizzo del client che si connette
        # conn è una risorsa, posso aprirla, chiuderla e gestirla
        print(f"connesso con {addr}")
        with conn:
            
            while not shutdown_flag:
                data = conn.recv(1024) #riceve max 1024 Byte
                #se data è vuoto il client ha interrotto la connessione inaspettatamente
                if not data:
                    break

                input_json = json.loads(data.decode()) #traduce e decodifica il messaggio ricevuto
                isDeTRSF = input_json["isDeTRSF"]
                input_str = input_json["userInput"]
                #tip -> messaggio sarà convertito in trasformata

                if isDeTRSF :
                    output_str = bwt.reverse_bwt(input_str)
                else:
                    output_str = bwt.bwt(input_str)

                conn.sendall(output_str.encode()) # converte il messaggio in byte per inviarlo tramite socket


print("Server stopped")
sys.exit(0)