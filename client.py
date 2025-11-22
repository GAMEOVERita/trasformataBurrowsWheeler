import socket, json

HOST = "127.0.0.1" # this is the ip address of the server (localhost because this is running locally)
PORT = 1984 # the port on which the server is running

def clientConnection(isDeTRSF : bool, input_str : str):
    # creates the json to transfer the needed data
    input_json = {
        "isDeTRSF": isDeTRSF,
        "input_str": input_str
    }

    # creates the socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect( (HOST, PORT) ) # connection to the server

        #the client sends to the server the encoded json
        s.sendall(json.dumps(input_json).encode())
        
        data = s.recv(1024) #recieves the server response and returns it decodified

    return data.decode()