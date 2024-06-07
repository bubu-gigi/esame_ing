from PyQt5.QtWidgets import QDialog, QLineEdit, QPushButton, QMessageBox, QDesktopWidget
from PyQt5.uic import loadUi

from Gestori.GestoreUsers import GestoreUsers
from Gestori.Helper import Helper


class ReimpostaPassword(QDialog):
    def __init__(self):
        super(ReimpostaPassword, self).__init__()
        self.login = None
        loadUi("./GUILayout/reimposta_password.ui", self)
        self.gestore_users = GestoreUsers()

        self.setWindowTitle("Reimposta Password")
        self.center()

        self.line_username = self.findChild(QLineEdit, "username")
        self.line_vecchia_password = self.findChild(QLineEdit, "vecchia_password")
        self.line_nuova_password = self.findChild(QLineEdit, "nuova_password")
        self.line_conferma_password = self.findChild(QLineEdit, "conferma_password")

        self.button_save_password = self.findChild(QPushButton, "button_save_password")
        self.button_cancel = self.findChild(QPushButton, "button_cancel")

        self.button_save_password.clicked.connect(self.handle_save_password_click)
        self.button_cancel.clicked.connect(self.handle_cancel_click)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def handle_cancel_click(self):
        from View.Users.Login import Login
        self.login = Login()
        self.close()
        return self.login.show()

    def handle_save_password_click(self):
        feedback = self.gestore_users.reimposta_password(self.line_username.text(), self.line_vecchia_password.text(), self.line_nuova_password.text(), self.line_conferma_password.text())
        if feedback == "user not found":
            QMessageBox.critical(self, 'Errore', "Nessun user trovato con questo username", QMessageBox.Ok, QMessageBox.Ok)
        elif feedback == "password not validated":
            QMessageBox.critical(self, 'Errore', "La nuova password deve essere di almeno 8 caratteri", QMessageBox.Ok, QMessageBox.Ok)
        elif feedback == "old password wrong":
            QMessageBox.critical(self, 'Errore', "La vecchia password non è corretta.", QMessageBox.Ok, QMessageBox.Ok)
        elif feedback == "new password not the same":
            QMessageBox.critical(self, 'Errore', "La conferma della nuova password non combiacia", QMessageBox.Ok, QMessageBox.Ok)
        else:
            from View.Users.Login import Login
            self.login = Login()
            self.close()
            return self.login.show()


