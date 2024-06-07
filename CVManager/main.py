import sys

from PyQt5.QtWidgets import QApplication

from Gestori.GestoreDipendenti import GestoreDipendenti
from View.Users.Login import Login

if __name__ == "__main__":
    gestore_dipendenti = GestoreDipendenti()
    app = QApplication(sys.argv)
    ui = Login()
    ui.show()
    app.exec_()
