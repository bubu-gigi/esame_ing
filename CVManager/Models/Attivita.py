class Attivita:

    def __init__(self):
        self.__id = -1
        self.__curriculum_matricola = -1
        self.__azienda = ""
        self.__progetto = ""
        self.__descrizione = ""
        self.__periodo = ""

    def get_id(self):
        return self.__id

    def get_curriculum_matricola(self):
        return self.__curriculum_matricola

    def get_azienda(self):
        return self.__azienda

    def get_progetto(self):
        return self.__progetto

    def get_descrizione(self):
        return self.__descrizione

    def get_periodo(self):
        return self.__periodo

    def set_id(self, id: int):
        self.__id = id

    def set_curriculum_matricola(self, curriculum_matricola):
        self.__curriculum_matricola = curriculum_matricola

    def set_azienda(self, azienda: str):
        self.__azienda = azienda

    def set_progetto(self, progetto: str):
        self.__progetto = progetto

    def set_descrizione(self, descrizione: str):
        self.__descrizione = descrizione

    def set_periodo(self, periodo: str):
        self.__periodo = periodo




