from tkinter import *
import socket

hostname = socket.gethostname()
IPAdr = socket.gethostbyname(hostname)

class UI():
    def __init__(self):
        self.__root = Tk()
        self.__scrollbar = Scrollbar(self.__root)
        self.__scrollbar.pack(side = RIGHT, fill = Y)
        self.__mainText = Text(self.__root, height = 20, width = 15, yscrollcommand = self.__scrollbar.set)
        self.__scrollbar.config(command = self.__mainText.yview)
        self.__mainText.config(state = "disabled")
        self.__secondaryText = Text(self.__root, height = 10, width = 40)
        self.__secondaryText.config(state = "normal")
        self.__secondaryText.pack(side = BOTTOM)
        self.__secondaryText.bind('<KeyRelease-Return>', self.__EnterEvent)

    def __EnterEvent(self, event):
        self.addText(str(IPAdr) + ":\n" + self.__secondaryText.get("0.0", "2.0"))
        self.__secondaryText.delete("0.0", "2.0")
        #self.__secondaryText.insert(INSERT, "hello")

    def addText(self, text):
        self.__mainText.config(state = "normal")
        self.__mainText.insert(INSERT, text)
        self.__mainText.config(state = "disabled")
        self.__mainText.pack()

    def run(self):
        self.__mainText.pack()
        self.__root.mainloop()

ui = UI()
ui.addText("Hello world!")
ui.addText("Ana are mere")

ui.run()
print("Hello there")
