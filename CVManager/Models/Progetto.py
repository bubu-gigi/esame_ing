import datetime

class Progetto:

    def __init__(self):
        self.__id = -1
        self.__titolo = ""
        self.__descrizione = ""
        self.__pm_matricola = -1
        self.__tipologia = ""
        self.__data_inizio = datetime.datetime(1970, 1, 1)
        self.__data_fine = datetime.datetime(9999, 12, 31)
        self.__budget = 0.0
        self.__stato = ""
        self.__dipendenti = []

    def get_id(self):
        return self.__id

    def get_titolo(self):
        return self.__titolo

    def get_descrizione(self):
        return self.__descrizione

    def get_pm_matricola(self):
        return self.__pm_matricola

    def get_tipologia(self):
        return self.__tipologia

    def get_data_inizio(self):
        return self.__data_inizio

    def get_data_fine(self):
        return self.__data_fine

    def get_budget(self):
        return self.__budget

    def get_stato(self):
        return self.__stato

    def get_dipendenti(self):
        return self.__dipendenti

    def set_id(self, id: int):
        self.__id = id

    def set_titolo(self, titolo: str):
        self.__titolo = titolo

    def set_descrizione(self, descrizione: str):
        self.__descrizione = descrizione

    def set_pm_matricola(self, pm_matricola: int):
        self.__pm_matricola = pm_matricola

    def set_tipologia(self, tipologia: str):
        self.__tipologia = tipologia

    def set_data_inizio(self, data_inizio: datetime):
        self.__data_inizio = data_inizio

    def set_data_fine(self, data_fine: datetime):
        self.__data_fine = data_fine

    def set_budget(self, budget: float):
        self.__budget = budget

    def set_stato(self, stato: str):
        self.__stato = stato

    def aggiungi_dipendente(self, dipendente: int):
        self.__dipendenti.append(dipendente)

    def rimuovi_dipendente(self, dipendente: int):
        self.__dipendenti.remove(dipendente)