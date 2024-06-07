import pickle
from Gestori.Helper import Helper

class GestoreProgetti:

    def __init__(self):
        self.progetti = Helper.get_all_progetti()

    def ricerca_progetto(self, id: int):
        self.progetti = Helper.get_all_progetti()
        if self.progetti is not None and len(self.progetti) != 0:
            for p in self.progetti.values():
                if int(p.get_id()) == int(id):
                    return p
        else:
            return None

    def salva_progetto(self, id, titolo, descrizione, pm_matricola, tipologia, data_inizio, data_fine, budget, stato, dipendenti):
        from Models.Progetto import Progetto
        self.progetti = Helper.get_all_progetti()
        progetto = Progetto()
        progetto.set_id(id)
        progetto.set_titolo(titolo)
        progetto.set_descrizione(descrizione)
        progetto.set_pm_matricola(pm_matricola)
        progetto.set_tipologia(tipologia)
        progetto.set_data_inizio(data_inizio)
        progetto.set_data_fine(data_fine)
        progetto.set_budget(budget)
        progetto.set_stato(stato)
        for dip in dipendenti:
            progetto.aggiungi_dipendente(dip)
        check_if_progetto_exists = self.ricerca_progetto(id)
        if check_if_progetto_exists is None:
            if self.progetti is None:
                self.progetti = {}
            self.progetti[progetto.get_id()] = progetto
            with open('Dati/Progetti.pickle', 'wb') as f:
                pickle.dump(self.progetti, f, pickle.HIGHEST_PROTOCOL)

    def modifica_progetto(self, id, titolo, descrizione, pm_matricola, tipologia, data_inizio, data_fine, budget, stato, dipendenti):
        from Models.Progetto import Progetto
        self.progetti = Helper.get_all_progetti()
        progetto = Progetto()
        progetto.set_id(id)
        progetto.set_titolo(titolo)
        progetto.set_descrizione(descrizione)
        progetto.set_pm_matricola(pm_matricola)
        progetto.set_tipologia(tipologia)
        progetto.set_data_inizio(data_inizio)
        progetto.set_data_fine(data_fine)
        progetto.set_budget(budget)
        progetto.set_stato(stato)
        for dip in dipendenti:
            progetto.aggiungi_dipendente(dip)
        check_if_progetto_exists = self.ricerca_progetto(id)
        if check_if_progetto_exists is not None:
            self.progetti[progetto.get_id()] = progetto
            with open('Dati/Progetti.pickle', 'wb') as f:
                pickle.dump(self.progetti, f, pickle.HIGHEST_PROTOCOL)

    def rimuovi_progetto(self, id: int):
        self.progetti = Helper.get_all_progetti()
        check_if_progetto_exists = self.ricerca_progetto(id)
        if check_if_progetto_exists is not None:
            del self.progetti[id]
            with open('Dati/Progetti.pickle', 'wb') as f:
                pickle.dump(self.progetti, f, pickle.HIGHEST_PROTOCOL)