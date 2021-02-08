import socket

PORT = 5050
FORMAT = "utf-8"
IP = socket.gethostbyname(socket.gethostname())
SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER.bind((IP, PORT))
SERVER.listen(3) # receive maximum clients
print(f'waiting for connections at {IP}')

while True: 
    socc, addr = SERVER.accept()
    print(f"{addr} connected")
    socc.send(("successfully connected...").encode(FORMAT))
    socc.close()

