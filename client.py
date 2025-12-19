import socket, json, config

HOST = config.HOST
PORT = config.PORT

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
        
        data = s.recv(1024) #receives the server response and returns it decodified


    return data.decode()
