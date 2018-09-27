import model.Memory as Memory
import controller.Controller as Controller
import threading
from tkinter import *


class View(object):

    def __init__(self):
        self.__controller = Controller.Controller()
        self.__name = None
        self.__root = None

    def run(self):
        self.__root = Tk()

        var = StringVar()
        label = Label(self.__root, textvariable=var, relief=RAISED)

        var.set("Comencemos. ¿Cómo te llamas?")
        label.pack()

        self.__name = Entry(self.__root, bd=5)
        self.__name.pack(side=LEFT)

        b = Button(self.__root, text="ok", command = self.verify_name)
        b.pack()

        self.__root.mainloop()

    def verify_name(self):
            if self.__name.get() != "":
                threading.Thread(target=self.run_assistant(self.__name.get())).start()

    def run_assistant(self, name):
        self.__root.withdraw()
        Memory.Memory()
        self.__controller.set_name(name)
        self.__controller.speak("Hola, " + name + ". ¿Qué puedo hacer por ti?")

        data = ""
        while data != "salir":
            data = self.__controller.record_audio()
            if data != "salir" and data != "":
                self.__controller.assistant(data)
            elif data == "salir":
                self.__root.destroy()
