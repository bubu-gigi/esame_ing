from datetime import datetime

class Dipendente:

    def __init__(self):
        self.__matricola = -1
        self.__nome = ""
        self.__cognome = ""
        self.__data_nascita = datetime(1970, 1, 1)
        self.__genere = ""
        self.__citta_nascita = ""
        self.__codice_fiscale = ""
        self.__indirizzo = ""
        self.__cap = ""
        self.__comune = ""
        self.__provincia = ""
        self.__titolo_studio = ""
        self.__ruolo = ""
        self.__funzione = ""
        self.__email_aziendale = ""
        self.__telefono = ""
        self.__stato = ""

    def get_matricola(self):
        return self.__matricola

    def get_nome(self):
        return self.__nome

    def get_cognome(self):
        return self.__cognome

    def get_data_nascita(self):
        return self.__data_nascita

    def get_genere(self):
        return self.__genere

    def get_citta_nascita(self):
        return self.__citta_nascita

    def get_codice_fiscale(self):
        return self.__codice_fiscale

    def get_indirizzo(self):
        return self.__indirizzo

    def get_cap(self):
        return self.__cap

    def get_comune(self):
        return self.__comune

    def get_provincia(self):
        return self.__provincia

    def get_titolo_studio(self):
        return self.__titolo_studio

    def get_ruolo(self):
        return self.__ruolo

    def get_funzione(self):
        return self.__funzione

    def get_email_aziendale(self):
        return self.__email_aziendale

    def get_telefono(self):
        return self.__telefono

    def get_stato(self):
        return self.__stato

    def set_matricola(self, matricola: int):
        self.__matricola = matricola

    def set_nome(self, nome: str):
        self.__nome = nome

    def set_cognome(self, cognome: str):
        self.__cognome = cognome

    def set_data_nascita(self, data_nascita: datetime):
        self.__data_nascita = data_nascita

    def set_genere(self, genere: str):
        self.__genere = genere

    def set_citta_nascita(self, citta_nascita: str):
        self.__citta_nascita = citta_nascita

    def set_codice_fiscale(self, codice_fiscale: str):
        self.__codice_fiscale = codice_fiscale

    def set_indirizzo(self, indirizzo: str):
        self.__indirizzo = indirizzo

    def set_cap(self, cap: str):
        self.__cap = cap

    def set_comune(self, comune: str):
        self.__comune = comune

    def set_provincia(self, provincia: str):
        self.__provincia = provincia

    def set_titolo_studio(self, titolo_studio: str):
        self.__titolo_studio = titolo_studio

    def set_ruolo(self, ruolo: str):
        self.__ruolo = ruolo

    def set_funzione(self, funzione: str):
        self.__funzione = funzione

    def set_email_aziendale(self, email_aziendale: str):
        self.__email_aziendale = email_aziendale

    def set_telefono(self, telefono: str):
        self.__telefono = telefono

    def set_stato(self, stato: str):
        self.__stato = stato