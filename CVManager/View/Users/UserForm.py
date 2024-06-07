
from PyQt5.QtWidgets import QLineEdit, QPushButton, QMessageBox, QDialog, QDesktopWidget, QComboBox
from PyQt5.uic import loadUi

from Gestori.GestoreUsers import GestoreUsers

class UserForm(QDialog):
    def __init__(self, user=None):
        super(UserForm, self).__init__()

        loadUi("./GUILayout/crea_user.ui", self)
        self.gestore_users = GestoreUsers()
        self.user = user

        self.line_username = self.findChild(QLineEdit, "username")
        self.line_password = self.findChild(QLineEdit, "password")
        self.line_role = self.findChild(QComboBox, "combobox_role")

        roles_list = ["dipendente", "admin"]
        self.line_role.addItems(roles_list)

        self.setWindowTitle("Edit User")
        self.center()

        self.button_cancel = self.findChild(QPushButton, "button_cancel_user")
        self.button_delete = self.findChild(QPushButton, "button_delete_user")
        self.button_save = self.findChild(QPushButton, "button_save_user")

        if user is None:
            self.button_delete.hide()

        if user is not None:
            self.line_username.setText(user.get_username())
            self.line_password.setText(user.get_password())
            self.line_role.setCurrentText(user.get_role())

        self.button_cancel.clicked.connect(self.handle_cancel_click)
        self.button_delete.clicked.connect(self.handle_delete_click)
        self.button_save.clicked.connect(self.handle_save_click)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def handle_cancel_click(self):
        self.close()

    def handle_delete_click(self):
        self.gestore_users.rimuovi_user(self.line_username.text())
        self.close()

    def handle_save_click(self):
        children = self.findChildren(QLineEdit)
        for c in children:
            if (c.text() == ""):
                QMessageBox.critical(self, 'Errore', "Compila tutti i campi", QMessageBox.Ok, QMessageBox.Ok)
                return
        if self.line_role.currentText() == "dipendente" :
            try:
                int(self.line_username.text()[-3:])
            except:
                QMessageBox.critical(self, 'Errore', "Gli ultimi 3 caratteri dell'username devono indicare la matricola del dipendente", QMessageBox.Ok,
                                 QMessageBox.Ok)
                return
        if len(self.line_password.text()) < 8:
            QMessageBox.critical(self, 'Errore', "La password deve avere almeno 8 caratteri", QMessageBox.Ok, QMessageBox.Ok)
            return
        if self.user is not None:
            self.gestore_users.modifica_user(self.line_username.text(), self.line_password.text(),
                                             self.line_role.currentText())
        else:
            self.gestore_users.salva_user(self.line_username.text(), self.line_password.text(),
                                         self.line_role.currentText())
        self.close()

