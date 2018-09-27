import model.Model as Model


class Controller(object):

    def __init__(self):
        self.__mod = Model.Model()
        self.__name = ""

    def set_name(self, name):
        self.__name = name

    def speak(self, data):
        self.__mod.speak(data)

    def record_audio(self):
        return self.__mod.record_audio()

    def assistant(self, data):
        return self.__mod.assistant(data)
