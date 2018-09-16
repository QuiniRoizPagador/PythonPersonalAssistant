from model.personalAssistant.PersonalAssistant import Jarvis


class Model:
    def __init__(self):
        self.jarvis = Jarvis()

    def jarvis(self, data):
        self.jarvis.jarvis(data)

    def record_audio(self):
        return self.jarvis.record_audio()

    def speak(self, data):
        return self.jarvis.speak(data)
