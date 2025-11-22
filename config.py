import os
HOST = "127.0.0.1" # this is the ip address of the server (localhost because this is running locally)
PORT = int(os.getenv("PORT", 1984)) # literally 1984 # the port on which the server is running
debug = os.getenv("DEBUG", "False").lower() in ("1", "true", "yes") # set the debug mode
