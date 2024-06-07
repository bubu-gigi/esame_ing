from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QMessageBox, QDesktopWidget
from PyQt5.uic import loadUi

from Gestori.GestoreUsers import GestoreUsers
from Models.Dipendente import Dipendente
from View.Dipendenti.DipendenteForm import DipendenteForm
from View.Dipendenti.DipendentiTable import DipendentiTable
from View.Users.ReimpostaPassword import ReimpostaPassword

class Login(QWidget):

    def __init__(self):
        super(Login, self).__init__()

        self.reimposta_password = None
        self.dipendente_form = None
        self.dipendenti_table = None
        loadUi("./GUILayout/login.ui", self)

        self.center()
        self.setWindowTitle("Login")

        self.line_username = self.findChild(QLineEdit, "line_username")
        self.line_password = self.findChild(QLineEdit, "line_password")
        self.button_login = self.findChild(QPushButton, "button_login")
        self.button_login.clicked.connect(self.handle_login_click)
        self.button_reimposta_password = self.findChild(QPushButton, "button_reimposta_password")
        self.button_reimposta_password.clicked.connect(self.handle_reimposta_password_click)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    #R01mkWgY
    def handle_login_click(self):
        gestore_users = GestoreUsers()
        feedback = gestore_users.login(self.line_username.text(), self.line_password.text())
        if type(feedback) is Dipendente:
            self.dipendente_form = DipendenteForm(dipendente=feedback)
            self.close()
            return self.dipendente_form.show()
        elif feedback == "dip first login":
            self.reimposta_password = ReimpostaPassword()
            self.close()
            return self.reimposta_password.show()
        elif feedback == "admin":
            self.dipenenti_table = DipendentiTable()
            self.close()
            return self.dipenenti_table.show()
        else:
            QMessageBox.critical(self, 'Errore', "Errore durante il login. Riprova", QMessageBox.Ok, QMessageBox.Ok)


    def handle_reimposta_password_click(self):
        self.reimposta_password = ReimpostaPassword()
        self.close()
        return self.reimposta_password.show()



