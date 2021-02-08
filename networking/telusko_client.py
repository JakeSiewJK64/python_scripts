import socket

FORMAT = "UTF-8"
IP = "169.254.160.15"
PORT = 5050

SOCKET = socket.socket()

ADDR = (IP, PORT)
SOCKET.connect(ADDR)

print((SOCKET.recv(1024)).decode(FORMAT))