#!/usr/bin/env python3

import socket
from methods import get_host

mesaj = {}
HOST = get_host()  # Standard loopback interface address (localhost)
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
                # print(ascii(data))
                data = data.encode("utf-8")
                conn.sendall(data)
                print(data)
                mesaj[ip] = ''

