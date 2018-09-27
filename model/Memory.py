import random
import datetime


class Memory(object):
    __instance = None

    def __new__(cls):
        if Memory.__instance is None:
            Memory.__instance = object.__new__(cls)
        return Memory.__instance

    def __init__(self):
        self.__questions = {}
        self.add_question("cómo estás", "Genial, gracias")

        self.add_question("qué hora es", "Son las " + str(datetime.datetime.now()))

        self.add_question("quién eres", "Hola, soy tu asistente personal.")

    def add_question(self, question="", value=""):
        if question in self.__questions:
            self.__questions[question].append(value)
        else:
            self.__questions[question] = [value]

    def get_response(self, question=""):
        if question in self.__questions:
            return random.choice(self.__questions[question])
        raise Exception

    def get_questions(self):
        return self.__questions

    questions = property(get_questions)





