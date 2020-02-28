import socket

fisier = {}
HOST = '192.168.43.109'  # Standard loopback interface address (localhost)
PORT = 65431      # Port to listen on (non-privileged ports are > 1023)

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        while True:
            s.listen()
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                data = conn.recv(2097152) #2mb
                print(data)
                if data != b'cod202':

                    ip = addr[0]

                    if ip not in fisier:
                        for i in fisier:
                            fisier[i].append(data)
                        fisier[ip] = [data]
                    else:
                        for i in fisier:
                            fisier[i].append(data)

                else:
                    nr_fisiere = len(fisier[ip])
                    for i in range(0,nr_fisiere):
                        conn.sendall(fisier[ip][i])
                        print(fisier[ip][i])
                    fisier[ip] = []
