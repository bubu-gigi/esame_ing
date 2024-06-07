import os.path
import pickle


class Helper:

    @staticmethod
    def get_all_lingue():
        if os.path.isfile('Dati/Lingue.pickle'):
            try:
                with open('Dati/Lingue.pickle', 'rb') as f:
                    current = dict(pickle.load(f))
                    return current
            except:
                return []

    @staticmethod
    def get_all_curriculum():
        if os.path.isfile('Dati/Curriculum.pickle'):
            try:
                with open('Dati/Curriculum.pickle', 'rb') as f:
                    current = dict(pickle.load(f))
                    return current
            except:
                return []

    @staticmethod
    def get_all_progetti():
        if os.path.isfile('Dati/Progetti.pickle'):
            try:
                with open('Dati/Progetti.pickle', 'rb') as f:
                    current = dict(pickle.load(f))
                    return current
            except:
                return []

    @staticmethod
    def get_all_dipendenti():
        if os.path.isfile('Dati/Dipendenti.pickle'):
            try:
                with open('Dati/Dipendenti.pickle', 'rb') as f:
                    current = dict(pickle.load(f))
                    return current
            except:
                return []

    @staticmethod
    def get_all_attivita():
        if os.path.isfile('Dati/Attivita.pickle'):
            try:
                with open('Dati/Attivita.pickle', 'rb') as f:
                    current = dict(pickle.load(f))
                    return current
            except:
                return []

    @staticmethod
    def get_all_users():
        if os.path.isfile('Dati/Users.pickle'):
            try:
                with open('Dati/Users.pickle', 'rb') as f:
                    current = dict(pickle.load(f))
                    return current
            except:
                return []

    @staticmethod
    def map_data_to_format(data):
        parts = data.split("-")
        return parts[2][:2] + "/" + parts[1] + "/" + parts[0]
