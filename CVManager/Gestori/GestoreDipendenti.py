import pickle

from Gestori.Helper import Helper

class GestoreDipendenti:

    def __init__(self):
        self.dipendenti = None

    def ricerca_dipendente(self, matricola: int):
        self.dipendenti = Helper.get_all_dipendenti()
        if self.dipendenti is not None and len(self.dipendenti) != 0:
            for d in self.dipendenti.values():
                if int(d.get_matricola()) == int(matricola):
                    return d
        else:
            return None

    def salva_dipendente(self, matricola, nome, cognome, data_nascita, genere, citta_nascita, codice_fiscale,
                        indirizzo, cap, comune, provincia, titolo_studio, ruolo, funzione, email_aziendale,
                        telefono, stato):
        from Models.Dipendente import Dipendente
        self.dipendenti = Helper.get_all_dipendenti()
        dipendente = Dipendente()
        dipendente.set_matricola(matricola)
        dipendente.set_nome(nome)
        dipendente.set_cognome(cognome)
        dipendente.set_data_nascita(data_nascita)
        dipendente.set_genere(genere)
        dipendente.set_citta_nascita(citta_nascita)
        dipendente.set_codice_fiscale(codice_fiscale)
        dipendente.set_indirizzo(indirizzo)
        dipendente.set_cap(cap)
        dipendente.set_comune(comune)
        dipendente.set_provincia(provincia)
        dipendente.set_titolo_studio(titolo_studio)
        dipendente.set_ruolo(ruolo)
        dipendente.set_funzione(funzione)
        dipendente.set_email_aziendale(email_aziendale)
        dipendente.set_telefono(telefono)
        dipendente.set_stato(stato)
        check_if_dipendente_exists = self.ricerca_dipendente(matricola)
        if check_if_dipendente_exists is None:
            if self.dipendenti is None:
                self.dipendenti = {}
            self.dipendenti[int(dipendente.get_matricola())] = dipendente
            with open('Dati/Dipendenti.pickle', 'wb') as f:
                pickle.dump(self.dipendenti, f, pickle.HIGHEST_PROTOCOL)
    def modifica_dipendente(self, matricola, nome, cognome, data_nascita, genere, citta_nascita, codice_fiscale,
                            indirizzo, cap, comune, provincia, titolo_studio, ruolo, funzione, email_aziendale
                            ,telefono, stato):
        from Models.Dipendente import Dipendente
        self.dipendenti = Helper.get_all_dipendenti()
        dipendente = Dipendente()
        dipendente.set_matricola(matricola)
        dipendente.set_nome(nome)
        dipendente.set_cognome(cognome)
        dipendente.set_data_nascita(data_nascita)
        dipendente.set_genere(genere)
        dipendente.set_citta_nascita(citta_nascita)
        dipendente.set_codice_fiscale(codice_fiscale)
        dipendente.set_indirizzo(indirizzo)
        dipendente.set_cap(cap)
        dipendente.set_comune(comune)
        dipendente.set_provincia(provincia)
        dipendente.set_titolo_studio(titolo_studio)
        dipendente.set_ruolo(ruolo)
        dipendente.set_funzione(funzione)
        dipendente.set_email_aziendale(email_aziendale)
        dipendente.set_telefono(telefono)
        dipendente.set_stato(stato)
        check_if_dipendente_exists = self.ricerca_dipendente(matricola)
        if check_if_dipendente_exists is not None:
            self.dipendenti[int(dipendente.get_matricola())] = dipendente
            with open('Dati/Dipendenti.pickle', 'wb') as f:
                pickle.dump(self.dipendenti, f, pickle.HIGHEST_PROTOCOL)

    def rimuovi_dipendente(self, matricola: int):
        self.dipendenti = Helper.get_all_dipendenti()
        check_if_dipendente_exists = self.ricerca_dipendente(matricola)
        if check_if_dipendente_exists is not None:
            del self.dipendenti[matricola]
            with open('Dati/Dipendenti.pickle', 'wb') as f:
                pickle.dump(self.dipendenti, f, pickle.HIGHEST_PROTOCOL)
