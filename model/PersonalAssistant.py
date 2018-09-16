import datetime
import os
import speech_recognition as sr
from gtts import gTTS


class Jarvis:

    def __init__(self):
        super()

    def __init__(self, name):
        self.set_name(name)

    def set_name(self, name):
        self.name = name

    def record_audio(self):
        """
        Se grabará un audio a través del micrófono disponible en el dispositivo.
        Tras esto, se etraducirá con la API de Google a String y se devolverá lo
        reconocido.
        :return: El contenido de la escucha.
        """
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Te escucho, " + self.name + "...")
            audio = r.listen(source, timeout=100)
        data = ""
        try:
            data = r.recognize_google(audio, language="es_ES")
            print("Has dicho: " + data)
        except sr.UnknownValueError:
            print("Lo siento, no te entiendo...")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition Service: {0}".format(e))
        return data

    def speak(self, audio_string):
        """
        Recibirá la frase a pronunciar y la ejecutará con el sistema de audio que proporcione
        el dispositivo en el que se ejecute la aplicación.
        :param audio_string: audio a reproducir.
        """
        print(audio_string)
        tts = gTTS(text=audio_string, lang='es-es')
        tts.save("audio.mp3")
        res = os.popen("start audio.mp3")
        res.close()

    def assistant(self, data):
        if "cómo estás" in data:
            self.speak("Genial, gracias.")
        if "qué hora es" in data:
            now = datetime.datetime.now()
            self.peak("Son las " + now.hour + " " + now.minute)
        if "quién eres" in data:
            self.speak("hola, soy tu asistente personal.")
