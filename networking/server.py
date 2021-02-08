import socket
import threading # separate code out, no need to wait

DISCONNECT_MESSAGE = "!DISCONNECT"
FORMAT = "utf-8"
HEADER = 64
PORT = 5050
# statically assign ip address
# SERVER = "192.168.110" 

# dynamically get ip address
SERVER = socket.gethostbyname(socket.gethostname()) 

# must be in a tuple
ADDR = (SERVER, PORT)

# list of commands:
# 1. socket.gethostname() = computer name
# 2. 

# socket.AF = type of IP address for specific connections 
# 1. INET = IPv4
# 2. INET_6 = IPv6
# 3. SOCK_STREAM = sending data via socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTIONS] {addr} connected.")
    connected = True
    while connected:    
        
        # how many bytes to receive, receive msg from this client from this socket
        msg_length = conn.recv(HEADER).decode(FORMAT)
        
        # checks if message length is not null, if not null, returns true
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
                
            if msg == DISCONNECT_MESSAGE:
                connected = False    
            
            print(f"[{addr}] {msg}")
            conn.send("Msg Received".encode(FORMAT))
    
    conn.close()

# starts the socket for us
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        # what port what ip address
        conn, addr = server.accept()
        
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        
        # 1 active connections when there are 2 threads running
        print(f"\n[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
    
print("[STARTING] server is starting...")
start()


