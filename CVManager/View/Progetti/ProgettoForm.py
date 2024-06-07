from Gestori.GestoreProgetti import GestoreProgetti
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QPushButton, QLineEdit, QMessageBox, QTextEdit, QComboBox, QListWidget, \
    QDesktopWidget

from Gestori.Helper import Helper
from View.Dipendenti.RicercaDipendente import RicercaDipendente


class ProgettoForm(QDialog):

    def __init__(self, callback, progetto = None):
        super(ProgettoForm, self).__init__()

        self.ricerca_dipendente = None
        self.gestore_progetti = GestoreProgetti()

        self.callback = callback
        self.progetto = progetto
        loadUi("./GUILayout/progetto_form.ui", self)
        self.setWindowTitle("Edit Progetto")
        self.center()

        self.save = self.findChild(QPushButton, "button_save_progetto_form")
        self.delete = self.findChild(QPushButton, "button_delete_progetto_form")
        self.cancel = self.findChild(QPushButton, "button_cancel_progetto_form")

        if progetto is None:
            self.delete.hide()

        self.titolo = self.findChild(QLineEdit, "progetto_titolo")
        self.pm_matricola = self.findChild(QLineEdit, "progetto_pm_matricola")
        self.tipologia = self.findChild(QComboBox, "combobox_tipologia")
        self.stato = self.findChild(QComboBox, "combobox_stato")
        self.budget = self.findChild(QLineEdit, "progetto_budget")
        self.data_inizio = self.findChild(QLineEdit, "progetto_data_inizio")
        self.data_fine = self.findChild(QLineEdit, "progetto_data_fine")
        self.descrizione = self.findChild(QTextEdit, "progetto_descrizione")
        self.list_dipendenti = self.findChild(QListWidget, "list_dipendenti")
        self.add_dipendente = self.findChild(QPushButton, "button_add_dipendente")
        self.remove_dipendente = self.findChild(QPushButton, "button_remove_dipendente")
        #azzera filtri

        tipologia_list = ["gara", "progetto operativo", "progetto interno"]
        stato_list = ["in corso", "da avviare", "chiuso"]

        self.tipologia.addItems(tipologia_list)
        self.stato.addItems(stato_list)

        self.add_dipendente.clicked.connect(self.handle_add_dipendente_click)
        self.remove_dipendente.clicked.connect(self.handle_remove_dipendente_click)

        if progetto is not None:
            self.titolo.setText(progetto.get_titolo())
            self.pm_matricola.setText(progetto.get_pm_matricola())
            self.tipologia.setCurrentText(progetto.get_tipologia())
            self.stato.setCurrentText(progetto.get_stato())
            self.budget.setText(progetto.get_budget())
            self.data_inizio.setText(progetto.get_data_inizio())
            self.data_fine.setText(progetto.get_data_fine())
            self.descrizione.setPlainText(progetto.get_descrizione())
            dips = []
            for dip in progetto.get_dipendenti():
                dips.append(dip)
            self.list_dipendenti.addItems(dips)

        self.save.clicked.connect(self.handle_save_click)
        self.cancel.clicked.connect(self.handle_cancel_click)
        self.delete.clicked.connect(self.handle_delete_click)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def handle_add_dipendente_click(self):
        self.ricerca_dipendente = RicercaDipendente(self.handle_ricerca)
        return self.ricerca_dipendente.show()

    def handle_ricerca(self, value):
        from Gestori.GestoreDipendenti import GestoreDipendenti
        gestore_dipendenti = GestoreDipendenti()
        dipendente = gestore_dipendenti.ricerca_dipendente(int(value))
        self.list_dipendenti.addItem(dipendente.get_cognome() + " " + dipendente.get_nome())

    def handle_remove_dipendente_click(self):
        listItems = self.list_dipendenti.selectedItems()
        if not listItems: return
        for item in listItems:
            self.list_dipendenti.takeItem(self.list_dipendenti.row(item))

    def handle_save_click(self):
        try:
            int(self.pm_matricola.text())
        except:
            QMessageBox.critical(self, 'Errore', 'L\'id e la matricola devono essere un numero', QMessageBox.Ok, QMessageBox.Ok)
            return
        children = self.findChildren(QLineEdit)
        for c in children:
            if(c.text() == ""):
                QMessageBox.critical(self, 'Errore', "Compila tutti i campi", QMessageBox.Ok, QMessageBox.Ok)
                return
        if self.descrizione.toPlainText() == "":
            QMessageBox.critical(self, 'Errore', "Compila tutti i campi", QMessageBox.Ok, QMessageBox.Ok)
            return

        from Gestori.GestoreDipendenti import GestoreDipendenti
        gestore_dipendenti = GestoreDipendenti()
        check_if_pm_exists = gestore_dipendenti.ricerca_dipendente(int(self.pm_matricola.text()))

        if check_if_pm_exists is None:
            QMessageBox.critical(self, 'Errore', "Matricola non trovata. Riprovare", QMessageBox.Ok, QMessageBox.Ok)
            return

        if self.stato.currentText() == "" or self.tipologia.currentText() == "":
            QMessageBox.critical(self, 'Errore', "Matricola non trovata. Riprovare", QMessageBox.Ok, QMessageBox.Ok)
            return

        items = [self.list_dipendenti.item(x).text() for x in range(self.list_dipendenti.count())]

        len_progetti = None
        progetti = Helper.get_all_progetti()
        if progetti is None:
            len_progetti = 0
        else:
            len_progetti = len(progetti)

        if self.progetto is None:
            self.gestore_progetti.salva_progetto(id=int(len_progetti + 1),
                                                pm_matricola=self.pm_matricola.text(),
                                                titolo=self.titolo.text(),
                                                tipologia=self.tipologia.currentText(),
                                                stato=self.stato.currentText(),
                                                budget=self.budget.text(),
                                                data_inizio=self.data_inizio.text(),
                                                data_fine=self.data_fine.text(),
                                                descrizione=self.descrizione.toPlainText(),
                                                dipendenti=items)
        else:
            self.gestore_progetti.modifica_progetto(id=int(self.progetto.get_id()),
                                                    pm_matricola=self.pm_matricola.text(),
                                                    titolo=self.titolo.text(),
                                                    tipologia=self.tipologia.currentText(),
                                                    stato=self.stato.currentText(),
                                                    budget=self.budget.text(),
                                                    data_inizio=self.data_inizio.text(),
                                                    data_fine=self.data_fine.text(),
                                                    descrizione=self.descrizione.toPlainText(),
                                                    dipendenti=items)
        self.callback()
        self.close()

    def handle_cancel_click(self):
        self.close()

    def handle_delete_click(self):
        self.gestore_progetti.rimuovi_progetto(self.progetto.get_id())
        self.close()




