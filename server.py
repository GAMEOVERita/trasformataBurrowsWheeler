import socket, bwt, json, keyboard, threading

# define host address and port (all local)
HOST = "127.0.0.1"
PORT = 1984 # literaly 1984 
shutdown_flag = False #flag to check whether or not to shut down the server 

# function to shut down the server if the user presses ctrl+z (might change later)
def key_listener():
    global shutdown_flag
    print("Press CTRL+Z to stop the server safely.")
    keyboard.wait("ctrl+z")
    shutdown_flag = True

# Start keyboard listener in background on a separate thread to permit the server to run
threading.Thread(target=key_listener, daemon=True).start()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # create the socket 
    s.bind((HOST,PORT)) #assign to the socket the ip address and the door
    
    # socket listenting for connections and prints some info
    s.listen()
    print(f"Server listening {HOST}:{PORT}")

    while not shutdown_flag:

        conn, addr = s.accept() # socket accept the request for a connection and prints some info
        print(f"connected with {addr}")
        with conn:
            
            while not shutdown_flag:
                data = conn.recv(1024) # allows only a max of 1024 Byte at a time
                if not data: # closes the connection if no data is being exchanged
                    break

                input_json = json.loads(data.decode()) #decodes the data into a json bc i needed to transfer more than a string 
                isDeTRSF = input_json["isDeTRSF"] #flag to check whether the user wants to use btw() or reverse_btw()
                input_str = input_json["input_str"]
                
                # calls btw() or reverse_btw() based on the flag
                if isDeTRSF :
                    output_str = bwt.reverse_bwt(input_str)
                else:
                    output_str = bwt.bwt(input_str)

                conn.sendall(output_str.encode()) # sends the result of the transform to the client

print("Server stopped")