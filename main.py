from tkinter import *
from tkinter import filedialog
import socket

hostname = socket.gethostname()
IPAdr = socket.gethostbyname(hostname)

HOST = '10.152.4.34'  # The server's hostname or IP address
PORT = 65432    # The port used by the server


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

        self.__button = Button(self.__root, bg  = "black", fg = "yellow", text = "RequestServerText")
        self.__button.grid(row = 1, column = 0)
        self.__button.bind("<Button-1>", self.__ButtonClickRequest)

        self.__button = Button(self.__root, bg = "black", fg = "yellow", text = "Selecteaza fisier")
        self.__button.grid(row = 2, column = 0)
        self.__button.bind("<Button-1>", self.__ButtonClickSelectFile)

        self.__data = ""

    def __ButtonClickSelectFile(self, event):
        file_path = filedialog.askopenfilename()
        if file_path == "":
            return
        print(file_path)

    def __ButtonClickRequest(self, event):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(b'')
            data = s.recv(2097152)
            self.addText(data)
            s.shutdown(1)
            s.close()

    def __EnterEvent(self, event):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if self.__secondaryText.get("0.0", "2.0") == '\n':
                s.connect((HOST, PORT))
                s.sendall(b'')
            else:
                s.connect((HOST, PORT))
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
