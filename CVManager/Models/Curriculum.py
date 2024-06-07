from Models.Attivita import Attivita
from Models.Lingua import Lingua

class Curriculum:

    def __init__(self):
        self.__dipendente_matricola = -1
        self.__funzione = ""
        self.__esperienza = ""
        self.__sintesi = ""
        self.__competenze = ""
        self.__formazione = ""

    def get_dipendente_matricola(self):
        return self.__dipendente_matricola

    def get_funzione(self):
        return self.__funzione

    def get_esperienza(self):
        return self.__esperienza

    def get_sintesi(self):
        return self.__sintesi

    def get_competenze(self):
        return self.__competenze

    def get_formazione(self):
        return self.__formazione

    def set_dipendente_matricola(self, dipendente_matricola: int):
        self.__dipendente_matricola = dipendente_matricola

    def set_funzione(self, funzione: str):
        self.__funzione = funzione

    def set_esperienza(self, esperienza: str):
        self.__esperienza = esperienza

    def set_sintesi(self, sintesi: str):
        self.__sintesi = sintesi

    def set_competenze(self, competenze: str):
        self.__competenze = competenze

    def set_formazione(self, formazione: str):
        self.__formazione = formazione
