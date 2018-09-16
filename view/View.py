import threading
from tkinter import *


class View:

    def __init__(self):
        self.name = ""

    def put_controller(self, controller):
        self.c = controller

    def run(self):
        self.root = Tk()

        var = StringVar()
        label = Label(self.root, textvariable=var, relief=RAISED)

        var.set("Comencemos. ¿Cómo te llamas?")
        label.pack()

        self.name = Entry(self.root, bd=5)
        self.name.pack(side = LEFT)

        b = Button(self.root, text="ok", command = self.verify_name)
        b.pack()

        self.root.mainloop()

    def verify_name(self):
            if self.name.get() != "":
                threading.Thread(target =self.run_assistant).start()

    def run_assistant(self):
        self.root.withdraw()
        self.c.speak("Hola, " + self.name.get() + ". ¿Qué puedo hacer por ti?")
        data = ""
        while data != "salir":
            data = self.c.record_audio()
            if data != "salir" and data != "":
                self.c.jarvis(data)
            elif data == "salir":
                self.root.destroy()