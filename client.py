from time import sleep
import socket

HOST = '10.152.4.34'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b'Hello, boyz!')
        data = s.recv(1024)
        print(data)
        print(str(PORT))
        #sleep(3)
        #s.close()

print('Received', repr(data))
