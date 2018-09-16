class Controller:

    def __init__(self, model):
        self.Mod = model

    def speak(self, data):
        self.Mod.speak(data)

    def record_audio(self):
        return self.Mod.record_audio

    def jarvis(self, data):
        return self.Mod.jarvis(data)
