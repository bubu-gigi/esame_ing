class FiltriProgetti:

    def __init__(self):
        self.__search = ""
        self.__stato = "tutti"
        self.__tipologia = "tutti"
        self.__ordinamento = "alfabetico ascendente"

    def get_search(self):
        return self.__search

    def get_stato(self):
        return self.__stato

    def get_tipologia(self):
        return self.__tipologia

    def get_ordinamento(self):
        return self.__ordinamento

    def set_search(self, search: str):
        self.__search = search

    def set_stato(self, stato: str):
        self.__stato = stato

    def set_tipologia(self, tipologia: str):
        self.__tipologia = tipologia

    def set_ordinamento(self, ordinamento: str):
        self.__ordinamento = ordinamento