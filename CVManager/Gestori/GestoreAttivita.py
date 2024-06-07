import pickle

from Models.Attivita import Attivita
from Gestori.Helper import Helper

class GestoreAttivita:

    def __init__(self):
        self.attivita = []

    def ricerca_attivita(self, curriculum_matricola: int, id: int):
        self.attivita = Helper.get_all_attivita()
        if self.attivita is not None and len(self.attivita) != 0:
            for att in self.attivita.values():
                if int(att.get_curriculum_matricola()) == int(curriculum_matricola) and int(att.get_id()) == int(id):
                    return att
        else:
            return None

    def salva_attivita(self, id, curriculum_matricola, azienda, progetto, descrizione, periodo):
        self.attivita = Helper.get_all_attivita()
        attivita = Attivita()
        attivita.set_id(id)
        attivita.set_curriculum_matricola(curriculum_matricola)
        attivita.set_azienda(azienda)
        attivita.set_progetto(progetto)
        attivita.set_descrizione(descrizione)
        attivita.set_periodo(periodo)
        check_if_attivita_exixsts = self.ricerca_attivita(curriculum_matricola, id)
        if check_if_attivita_exixsts is None:
            if self.attivita is None:
                self.attivita = {}
            self.attivita[attivita.get_curriculum_matricola(), attivita.get_id()] = attivita
            with open('Dati/Attivita.pickle', 'wb') as f:
                pickle.dump(self.attivita, f, pickle.HIGHEST_PROTOCOL)

    def modifica_attivita(self, id, curriculum_matricola, azienda, progetto, descrizione, periodo):
        self.attivita = Helper.get_all_attivita()
        attivita = Attivita()
        attivita.set_id(id)
        attivita.set_curriculum_matricola(curriculum_matricola)
        attivita.set_azienda(azienda)
        attivita.set_progetto(progetto)
        attivita.set_descrizione(descrizione)
        attivita.set_periodo(periodo)
        check_if_attivita_exixsts = self.ricerca_attivita(curriculum_matricola, id)
        if check_if_attivita_exixsts is not None:
            self.attivita[attivita.get_curriculum_matricola(), attivita.get_id()] = attivita
            with open('Dati/Attivita.pickle', 'wb') as f:
                pickle.dump(self.attivita, f, pickle.HIGHEST_PROTOCOL)

    def rimuovi_attivita(self, curriculum_matricola, id):
        self.attivita = Helper.get_all_attivita()
        check_if_attivita_exixsts = self.ricerca_attivita(curriculum_matricola, id)
        if check_if_attivita_exixsts is not None:
            del self.attivita[curriculum_matricola, id]
            with open('Dati/Attivita.pickle', 'wb') as f:
                pickle.dump(self.attivita, f, pickle.HIGHEST_PROTOCOL)
