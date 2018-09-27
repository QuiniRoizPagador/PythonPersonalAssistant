import model.PersonalAssistant as Pa


class Model(object):

    def __init__(self):
        self.__jarvis = Pa.PersonalAssistant()

    def set_name(self, name):
        self.__jarvis.set_name(name)

    def assistant(self, data):
        self.__jarvis.assistant(data)

    def record_audio(self):
        return self.__jarvis.record_audio()

    def speak(self, data):
        return self.__jarvis.speak(data)
