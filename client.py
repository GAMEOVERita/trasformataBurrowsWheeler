import socket, json

HOST = "127.0.0.1" # this is the ip address of the server (localhost because this is running locally)
PORT = 1984 # the port on which the server is running

def clientConnection(isDeTRSF : bool, userInput : str):
    input_json = {
        "isDeTRSF": isDeTRSF,
        "userInput": userInput
    }

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect( (HOST, PORT) )# connessione al server

        #il client manda al server il file json
        s.sendall(json.dumps(input_json).encode())
        
        data = s.recv(1024) #ricevo eventuale posta dal server

    return data.decode()