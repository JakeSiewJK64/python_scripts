import socket

s = socket.socket()
port = 80
s.connect(('localhost', port))
print(s.recv(1024))
s.close()