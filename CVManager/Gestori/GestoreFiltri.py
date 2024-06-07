from Gestori.Helper import Helper
from Models.Filters.FiltriDipendenti import FiltriDipendenti
from Models.Filters.FiltriProgetti import FiltriProgetti

class GestoreFiltri:

    def handle_filtri_list_view_dipendenti(self, filtri: FiltriDipendenti):
        all_dipendenti_as_dict = Helper.get_all_dipendenti()
        all_dipendenti = []
        if all_dipendenti_as_dict is not None:
            all_dipendenti.extend(all_dipendenti_as_dict.values())

        if all_dipendenti == "ko" or all_dipendenti is None or len(all_dipendenti) == 0:
            return {}

        dipendenti_filtered = []
        for dipendente in all_dipendenti:
            if (dipendente.get_nome().lower().startswith(filtri.get_search().lower()) or
                    dipendente.get_cognome().lower().startswith(filtri.get_search().lower()) or
                    dipendente.get_codice_fiscale().lower().startswith(filtri.get_search().lower())):
                if filtri.get_ruolo() != "tutti":
                    if dipendente.get_ruolo().lower() == str(filtri.get_ruolo()):
                        if filtri.get_stato() != "tutti":
                            if dipendente.get_stato().lower() == filtri.get_stato():
                                dipendenti_filtered = self.__aggiungi_dipendente_alla_lista(dipendenti_filtered, dipendente)
                        else:
                            dipendenti_filtered = self.__aggiungi_dipendente_alla_lista(dipendenti_filtered, dipendente)
                else:
                    if filtri.get_stato() != "tutti":
                        if dipendente.get_stato().lower() == filtri.get_stato():
                            dipendenti_filtered = self.__aggiungi_dipendente_alla_lista(dipendenti_filtered, dipendente)
                    else:
                        dipendenti_filtered = self.__aggiungi_dipendente_alla_lista(dipendenti_filtered, dipendente)

        if dipendenti_filtered is not None:
            if len(dipendenti_filtered) > 1:
                dipendenti_sorted = self.__ordina_list_dipendenti(dipendenti_filtered, filtri.get_ordinamento())
                return dipendenti_sorted
            elif len(dipendenti_filtered) == 1:
                return dipendenti_filtered
            else:
                return  []
        else:
            return None

    def __aggiungi_dipendente_alla_lista(self, dipendenti_filtered, dipendente):
        dipendenti_filtered.append(dipendente)
        return dipendenti_filtered

    def __ordina_list_dipendenti(self, dipendenti_list, ordinamento):
        if ordinamento == "alfabetico ascendente":
            dipendenti_sorted = sorted(dipendenti_list, key=lambda x: x.get_cognome(), reverse=False)
            return dipendenti_sorted
        elif ordinamento == "alfabetico discendente":
            dipendenti_sorted = sorted(dipendenti_list, key=lambda x: x.get_cognome(), reverse=True)
            return dipendenti_sorted
        elif ordinamento == "matricola ascendente":
            dipendenti_sorted = sorted(dipendenti_list, key=lambda x: int(x.get_matricola()), reverse=False)
            return dipendenti_sorted
        elif ordinamento == "matricola discendente":
            dipendenti_sorted = sorted(dipendenti_list, key=lambda x: int(x.get_matricola()), reverse=True)
            return dipendenti_sorted
        else:
            return dipendenti_list

    def handle_filtri_list_view_progetti(self, filtri: FiltriProgetti):
        all_progetti_as_dict = Helper.get_all_progetti()
        all_progetti = []
        if all_progetti_as_dict is not None:
            all_progetti.extend(all_progetti_as_dict.values())
        progetti_filtered = []

        if all_progetti == "ko" or all_progetti is None or len(all_progetti) == 0:
            return {}

        for progetto in all_progetti:
            if progetto.get_titolo().lower().startswith(filtri.get_search()):
                if filtri.get_tipologia() == "tutti":
                    if filtri.get_stato() == "tutti":
                        progetti_filtered = self.__aggiungi_progetto_alla_lista(progetti_filtered, progetto)
                    else:
                        if filtri.get_stato() == progetto.get_stato():
                            progetti_filtered = self.__aggiungi_progetto_alla_lista(progetti_filtered,
                                                                                             progetto)
                else:
                    if filtri.get_tipologia() == progetto.get_tipologia():
                        if filtri.get_stato() == "tutti":
                            progetti_filtered = self.__aggiungi_progetto_alla_lista(progetti_filtered,
                                                                                             progetto)
                        else:
                            if filtri.get_stato() == progetto.get_stato():
                                progetti_filtered = self.__aggiungi_progetto_alla_lista(progetti_filtered,
                                                                                                 progetto)
        if progetti_filtered is not None:
            if len(progetti_filtered) > 1:
                progetti_sorted = self.__ordina_list_progetti(progetti_filtered, filtri.get_ordinamento())
                return progetti_sorted
            elif len(progetti_filtered) == 1:
                return progetti_filtered
            else:
                return []
        else:
            return None

    def __ordina_list_progetti(self, progetti_list, ordinamento):
        if ordinamento == "alfabetico ascendente":
            progetti_sorted= sorted(progetti_list, key=lambda x: x.get_titolo(), reverse=False)
            return progetti_sorted
        elif ordinamento == "alfabetico discendente":
            progetti_sorted = sorted(progetti_list, key=lambda x: x.get_titolo(), reverse=True)
            return progetti_sorted
        else:
            return progetti_list

    def __aggiungi_progetto_alla_lista(self, progetto_list, progetto):
        progetto_list.append(progetto)
        return progetto_list