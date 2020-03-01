from tkinter import *
from tkinter import filedialog
import socket
from methods import get_host, binary_to_int

hostname = socket.gethostname()
IPAdr = socket.gethostbyname(hostname)

HOST = get_host()    # The server's hostname or IP address
PORT_TEXT = 65432    # The port used by the text server
PORT_FILE = 65431    # The port used by the file server

class UI():
    def __init__(self):
        self.__root = Tk()
        self.__root.configure(bg = "#111")
        self.__root.title("Mesagerie")
        self.__scrollbar = Scrollbar(self.__root)
        self.__scrollbar.config(bg = "#333", troughcolor = "#111")
        self.__scrollbar.grid(row = 0, column = 2, sticky = "ns")
        #self.__scrollbar.pack(side = RIGHT, fill = Y)
        self.__mainText = Text(self.__root, height = 30, width = 120, yscrollcommand = self.__scrollbar.set, bg = "black", fg = "green")
        self.__scrollbar.config(command = self.__mainText.yview)
        self.__mainText.config(state = "disabled")
        self.__mainText.grid(row = 0, column = 0, columnspan = 2)
        self.__secondaryText = Text(self.__root, height = 10, width = 40, bg = "black", fg = "green")
        self.__secondaryText.config(state = "normal")
        self.__secondaryText.grid(row = 1, column = 1, pady = 5, rowspan = 2)
        #self.__secondaryText.pack(side = BOTTOM)
        #self.__secondaryText.pack(side = RIGHT)
        self.__secondaryText.bind("<KeyRelease-Return>", self.__EnterEvent)

        self.__button = Button(self.__root, bg  = "black", fg = "yellow", text = "RequestServer")
        self.__button.grid(row = 1, column = 0)
        self.__button.bind("<Button-1>", self.__ButtonClickRequest)

        self.__button = Button(self.__root, bg = "black", fg = "yellow", text = "Selecteaza fisier")
        self.__button.grid(row = 2, column = 0)
        self.__button.bind("<Button-1>", self.__ButtonClickSelectFile)

        self.__data = ""
        self.__file_path = ''

    def __ButtonClickSelectFile(self, event):
        self.__file_path = filedialog.askopenfilename()
        if self.__file_path == "":
            return
        with open(self.__file_path,'rb') as f:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

                s.connect((HOST, 65431))
                l = f.read(1024*1024*10)
                #s.send(b'cod702 ')
                s.send(l)
                print(PORT_TEXT)
                s.close()
        print(self.__file_path)

    def __ButtonClickRequest(self, event):
        #text_request
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT_TEXT))
            s.sendall(b'error207b')
            data = s.recv(2097152)
            self.addText(data)
            s.shutdown(1)
            s.close()

        #file_request
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT_FILE))
            s.sendall(b'cod202')
            nr_fisiere = binary_to_int(s.recv(4))
            print(nr_fisiere)
            for i in range(0, nr_fisiere):
                data = s.recv(1024*1024*10)

                nume_fisier = self.__file_path.split('/')[-1]
                with open('files/'+nume_fisier,'wb') as f:
                    f.write(bytearray(data))
                    f.close()

                print(data)

    def __EnterEvent(self, event):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if self.__secondaryText.get("0.0", "2.0") == '\n':
                s.connect((HOST, PORT_TEXT))
                s.sendall(b'error207b')
            else:
                s.connect((HOST, PORT_TEXT))
                s.sendall((str(IPAdr) + ":\n" + self.__secondaryText.get("0.0", "2.0")+"\n").encode('utf-8'))
                data = s.recv(2097152)
                self.addText(data)
                s.shutdown(1)
                s.close()

        #self.addText(str(IPAdr) + ":\n" + self.__secondaryText.get("0.0", "2.0"))

        self.__secondaryText.delete("0.0", "2.0")
        #self.__secondaryText.insert(INSERT, "hello")




    def addText(self, text):
        self.__mainText.config(state = "normal")
        self.__mainText.insert(INSERT, text)
        self.__mainText.config(state = "disabled")
        #self.__mainText.pack()

    def run(self):
        self.__root.resizable(width = False, height = False)
        #self.__mainText.pack()
        while True:
            self.__root.update_idletasks()
            self.__root.update()


        #self.__root.mainloop()

ui = UI()
ui.addText("Welcome to Mesagerie!\n\n")

ui.run()
print("Hello there")
