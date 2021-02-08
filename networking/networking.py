import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = socket.gethostbyname("localhost")

# default port for socket
port = 80

try:    
    host_ip = socket.gethostbyname("www.google.com")
except socket.gaierror:
    print("there was an error resolving the host")
    sys.exit()

s.connect((host_ip, port))
print("the socket has successfully connected to google")

  