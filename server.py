#!/usr/bin/env python3

import socket

mesaj = {}
HOST = '10.152.4.34'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        while True:
            s.listen()
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                data = conn.recv(2097152) #2mb

                #print("hello")
                #if not data:
                #    continue

                data = data.decode("utf-8")
                if data == 'error207b':
                    data = ""
                ip = addr[0]
                if ip in mesaj:
                    for i in mesaj:
                        mesaj[i] += data
                else:
                    for i in mesaj:
                        mesaj[i] += data
                    mesaj[ip] = data

                data = mesaj[ip]
                #print(ascii(data))
                data = data.encode("utf-8")
                print(data)
                conn.sendall(data)
                mesaj[ip] = ''
