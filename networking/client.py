import socket

HEADER = 64
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("169.254.160.15", 5050))

def send(msg):
    message = msg.encode(FORMAT) # encode the string into a byte format
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))# byte space
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))
    
send("HELLO WORLD!")






