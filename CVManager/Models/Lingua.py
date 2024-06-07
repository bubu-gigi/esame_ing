import os
import pickle


class Lingua:

    def __init__(self):
        self.__id = -1
        self.__curriculum_matricola = -1
        self.__nome = ""
        self.__comprensione = ""
        self.__lettura = ""
        self.__scrittura = ""

    def get_id(self):
        return self.__id

    def get_curriculum_matricola(self):
        return self.__curriculum_matricola

    def get_nome(self):
        return self.__nome

    def get_comprensione(self):
        return self.__comprensione

    def get_lettura(self):
        return self.__lettura

    def get_scrittura(self):
        return self.__scrittura

    def set_id(self, id: int):
        self.__id = id

    def set_curriculum_matricola(self, curriculum_matricola):
        self.__curriculum_matricola = curriculum_matricola

    def set_nome(self, nome: str):
        self.__nome = nome

    def set_comprensione(self, comprensione: str):
        self.__comprensione = comprensione

    def set_lettura(self, lettura: str):
        self.__lettura = lettura

    def set_scrittura(self, scrittura: str):
        self.__scrittura = scrittura