
import os
import speech_recognition as sr
from gtts import gTTS
import model.Memory as Memory


class PersonalAssistant(object):

    def __init__(self):
        self.__name = ""
        self._memory = Memory.Memory()

    def set_name(self, n):
        self.__name = n

    def record_audio(self):
        """
        Se grabará un audio a través del micrófono disponible en el dispositivo.
        Tras esto, se etraducirá con la API de Google a String y se devolverá lo
        reconocido.
        :return: El contenido de la escucha.
        """
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Te escucho, " + self.__name + "...")
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
        try:
            print(audio_string)
            tts = gTTS(text=audio_string, lang='es-es')
            tts.save("audio.mp3")
            res = os.popen("start audio.mp3")
            res.close()
        except Exception as e:
            print(e)

    def assistant(self, data):
        str = self._memory.get_response(data)
        self.speak(str)

