import os
import pickle

from Gestori.Helper import Helper


class GestoreLingue:

    def __init__(self):
        self.lingue = Helper.get_all_lingue()

    def __ricerca_lingua(self, curriculum_matricola, id):
        self.lingue = Helper.get_all_lingue()
        if self.lingue is not None and len(self.lingue) != 0:
            for lingua in self.lingue.values():
                if int(lingua.get_curriculum_matricola()) == int(curriculum_matricola) and int(lingua.get_id()) == int(id):
                    return lingua
        else:
            return None

    def salva_lingua(self, id, curriculum_matricola, nome, comprensione, lettura, scrittura):
        from Models.Lingua import Lingua
        self.lingue = Helper.get_all_lingue()
        lingua = Lingua()
        lingua.set_id(id)
        lingua.set_curriculum_matricola(curriculum_matricola)
        lingua.set_nome(nome)
        lingua.set_comprensione(comprensione)
        lingua.set_lettura(lettura)
        lingua.set_scrittura(scrittura)
        check_if_lingua_exixts = self.__ricerca_lingua(curriculum_matricola, id)
        if check_if_lingua_exixts is None:
            if self.lingue is None:
                self.lingue = {}
            self.lingue[lingua.get_curriculum_matricola(), lingua.get_id()] = lingua
            with open('Dati/Lingue.pickle', 'wb') as f:
                pickle.dump(self.lingue, f, pickle.HIGHEST_PROTOCOL)

    def modifica_lingua(self, id, curriculum_matricola, nome, comprensione, lettura, scrittura):
        from Models.Lingua import Lingua
        self.lingue = Helper.get_all_lingue()
        lingua = Lingua()
        lingua.set_id(id)
        lingua.set_curriculum_matricola(curriculum_matricola)
        lingua.set_nome(nome)
        lingua.set_comprensione(comprensione)
        lingua.set_lettura(lettura)
        lingua.set_scrittura(scrittura)
        check_if_lingua_exixts = self.__ricerca_lingua(curriculum_matricola, id)
        if check_if_lingua_exixts is not None:
            self.lingue[lingua.get_curriculum_matricola(), lingua.get_id()] = lingua
            with open('Dati/Lingue.pickle', 'wb') as f:
                pickle.dump(self.lingue, f, pickle.HIGHEST_PROTOCOL)

    def rimuovi_lingua(self, curriculum_matricola, id):
        self.lingue = Helper.get_all_lingue()
        check_if_lingua_exixts = self.__ricerca_lingua(curriculum_matricola, id)
        if check_if_lingua_exixts is not None:
            del self.lingue[curriculum_matricola, id]
            with open('Dati/Lingue.pickle', 'wb') as f:
                pickle.dump(self.lingue, f, pickle.HIGHEST_PROTOCOL)
