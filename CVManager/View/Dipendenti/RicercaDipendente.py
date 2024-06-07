from PyQt5.QtWidgets import QDialog, QLineEdit, QPushButton, QMessageBox, QDesktopWidget
from PyQt5.uic import loadUi

from Gestori.GestoreDipendenti import GestoreDipendenti
from Gestori.Helper import Helper


class RicercaDipendente(QDialog):
    def __init__(self, callback):
        super(RicercaDipendente, self).__init__()

        self.edit_user = None
        self.callback = callback
        loadUi("./GUILayout/ricerca_dipendente.ui", self)
        self.gestore_dipendenti = GestoreDipendenti()

        self.setWindowTitle("Ricerca Dipendente")
        self.center()

        self.line_username = self.findChild(QLineEdit, "line_dipendente")
        self.button_ricerca = self.findChild(QPushButton, "button_add")
        self.button_cancel = self.findChild(QPushButton, "button_cancel")

        self.button_ricerca.clicked.connect(self.handle_ricerca_click)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def handle_ricerca_click(self):
        dipendente = self.gestore_dipendenti.ricerca_dipendente(self.line_username.text())
        if dipendente is None:
            QMessageBox.critical(self, 'Errore', "Nessun dipendente trovato con questa matricola. Riprova", QMessageBox.Ok, QMessageBox.Ok)
        else:
            self.callback(int(self.line_username.text()))
            self.close()