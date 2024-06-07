class FiltriDipendenti:

    def __init__(self):
        self.__search = ""
        self.__ruolo = "tutti"
        self.__stato = "tutti"
        self.__ordinamento = "alfabetico ascendente"

    def get_search(self):
        return self.__search

    def get_ruolo(self):
        return self.__ruolo

    def get_stato(self):
        return self.__stato

    def get_ordinamento(self):
        return self.__ordinamento

    def set_search(self, search: str):
        self.__search = search

    def set_ruolo(self, ruolo: str):
        self.__ruolo = ruolo

    def set_stato(self, stato: str):
        self.__stato = stato

    def set_ordinamento(self, ordinamento: str):
        self.__ordinamento = ordinamento
