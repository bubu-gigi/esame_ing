import pickle

from PyQt5.QtWidgets import QMessageBox

from Gestori.Helper import Helper

class GestoreUsers:

    def __init__(self):
        self.users = Helper.get_all_users()

    def ricerca_user(self, username: str):
        self.users = Helper.get_all_users()
        if self.users is not None and len(self.users) is not 0:
            for u in self.users.values():
                if u.get_username() == username:
                    return u
        else:
            return None

    def salva_user(self, username: str, password: str, role: str):
        from Models.User import User
        self.users = Helper.get_all_users()
        user = User()
        user.set_username(username)
        user.set_password(password)
        user.set_role(role)
        check_if_user_exists = self.ricerca_user(username)
        if check_if_user_exists is None:
            if self.users is None:
                self.users = {}
            self.users[user.get_username()] = user
            with open('Dati/Users.pickle', 'wb') as f:
                pickle.dump(self.users, f, pickle.HIGHEST_PROTOCOL)

    def modifica_user(self, username: str, password: str, role: str):
        from Models.User import User
        self.users = Helper.get_all_users()
        user = User()
        user.set_username(username)
        user.set_password(password)
        user.set_role(role)
        check_if_user_exists = self.ricerca_user(username)
        if check_if_user_exists is not None:
            self.users[user.get_username()] = user
            with open('Dati/Users.pickle', 'wb') as f:
                pickle.dump(self.users, f, pickle.HIGHEST_PROTOCOL)

    def rimuovi_user(self, username: str):
        self.users = Helper.get_all_users()
        check_if_user_exists = self.ricerca_user(username)
        if check_if_user_exists is not None:
            del self.users[username]
            with open('Dati/Users.pickle', 'wb') as f:
                pickle.dump(self.users, f, pickle.HIGHEST_PROTOCOL)

    def reimposta_password(self, username, vecchia_password, nuova_password, conferma_password):
        user = self.ricerca_user(username)
        if user is None:
            return "user not found"
        if user.get_password() != vecchia_password:
            return "old password wrong"
        if len(nuova_password) < 8:
            return "password not validated"
        if nuova_password != conferma_password:
            return "new password not the same"
        user.set_password(nuova_password)
        self.modifica_user(user.get_username(), user.get_password(), user.get_role())
        return "ok"

    def login(self, username, password):
        self.users = Helper.get_all_users()
        self.dipendenti = Helper.get_all_dipendenti()

        if username == "admin" and password == "R01mkWgY":
            return "admin"
        if self.users is None or len(self.users) <= 0 or len(self.dipendenti) <= 0 or self.dipendenti is None:
            return "ko"
        else:
            for user in self.users.values():
                u = user.get_username()
                p = user.get_password()
                if u == username and p == password:
                    if user.get_role() == "admin":
                        return "admin"
                    else:
                        matricola = username[-3:]
                        while matricola.startswith("0"):
                            matricola = matricola[1:]
                        if username == password:
                            return "dip first login"
                        for dipendente in self.dipendenti.values():
                            if int(dipendente.get_matricola()) == int(matricola):
                                return dipendente
            return "ko"



