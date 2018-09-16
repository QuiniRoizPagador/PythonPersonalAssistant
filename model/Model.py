from model import PersonalAssistant

class Model:
    def __init__(self):
        self.jarvis = PersonalAssistant()

    def set_name(self, name):
        self.jarvis.set_name(name)

    def jarvis(self, data):
        self.jarvis.assistant(data)

    def record_audio(self):
        return self.jarvis.record_audio

    def speak(self, data):
        return self.jarvis.speak(data)
