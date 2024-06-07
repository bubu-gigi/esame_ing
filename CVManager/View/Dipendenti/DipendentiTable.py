from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QPushButton, QTableWidget, QTableWidgetItem, QCheckBox, QLineEdit, QComboBox, \
    QDesktopWidget

from Gestori.GestoreFiltri import GestoreFiltri
from Models.Filters.FiltriDipendenti import FiltriDipendenti
from View.Dipendenti.DipendenteForm import DipendenteForm
from View.Users.RicercaUser import RicercaUser
from View.Users.UserForm import UserForm


class DipendentiTable(QMainWindow):
    def __init__(self):
        super(DipendentiTable, self).__init__()
        self.login = None
        self.edit_user = None
        self.find_user = None
        self.dipendenti_form = None
        self.progetti_table = None
        loadUi("./GUILayout/dipendenti_table.ui", self)

        self.setWindowTitle("Dipendenti")
        self.center()

        self.dipendenti = []
        self.filtri = FiltriDipendenti()

        self.search = self.findChild(QLineEdit, "search_dipendente")
        self.search.textChanged.connect(self.update_ui)

        self.ruolo = self.findChild(QComboBox, "combobox_ruoli")

        ruoli_list = ["tutti", "sviluppatore", "sistemista", "manager", "amministrazione", "redazione"]

        self.ruolo.addItems(ruoli_list)

        self.ruolo.currentTextChanged.connect(self.update_ui)

        self.ordinamento = self.findChild(QComboBox, "combobox_ordinamento")

        ordinamento_list = ["alfabetico ascendente", "alfabetico discendente", "matricola ascendente", "matricola discendente"]

        self.ordinamento.addItems(ordinamento_list)

        self.ordinamento.currentTextChanged.connect(self.update_ui)

        self.table = self.findChild(QTableWidget, "tableWidget")
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(('Matricola', 'Cognome e Nome', 'Codice Fiscale', 'Ruolo', 'Stato'))
        self.table.setColumnWidth(0, 68)
        self.table.setColumnWidth(1, 222)
        self.table.setColumnWidth(2, 222)
        self.table.setColumnWidth(3, 222)
        self.table.setColumnWidth(4, 222)

        self.button_new_dipendente = self.findChild(QPushButton, "new_dipendente")
        self.button_new_dipendente.clicked.connect(self.handle_new_dipendente_click)
        self.button_aggiorna_dipendente = self.findChild(QPushButton, "aggiorna_dipendente")
        self.button_aggiorna_dipendente.clicked.connect(self.handle_aggiorna_dipendente_click)
        self.button_progetti = self.findChild(QPushButton, "button_progetti")
        self.button_progetti.clicked.connect(self.handle_progetti_click)
        self.button_crea_user = self.findChild(QPushButton, "button_crea_user")
        self.button_crea_user.clicked.connect(self.handle_crea_user_click)
        self.button_edit_user = self.findChild(QPushButton, "button_edit_user")
        self.button_edit_user.clicked.connect(self.handle_edit_user_click)
        self.button_logout = self.findChild(QPushButton, "button_logout")
        self.button_logout.clicked.connect(self.handle_logout_click)
        self.button_azzera_filtri = self.findChild(QPushButton, "button_azzera_filtri")
        self.button_azzera_filtri.clicked.connect(self.handle_azzera_filtri_click)

        self.checkbox_attivo = self.findChild(QCheckBox, "checkbox_attivo")
        self.checkbox_attivo.setChecked(True)
        self.checkbox_attivo.stateChanged.connect(self.update_ui)
        self.checkbox_inattivo = self.findChild(QCheckBox, "checkbox_inattivo")
        self.checkbox_inattivo.stateChanged.connect(self.update_ui)

        self.update_ui()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def handle_azzera_filtri_click(self):
        self.search.setText("")
        self.ruolo.setCurrentText("tutti")
        self.checkbox_attivo.setChecked(True)
        self.checkbox_inattivo.setChecked(True)
        self.ordinamento.setCurrentText("alfabetico ascendente")

    def handle_new_dipendente_click(self):
        self.dipendenti_form = DipendenteForm(callback=self.update_ui, dipendente=None, role="admin")
        return self.dipendenti_form.show()

    def handle_aggiorna_dipendente_click(self):
        r = self.table.currentRow()
        if(r != -1):
            matricola_selected = self.table.item(r, 0).text()
            dipendente_selected = None
            for dipendente in self.dipendenti:
                if dipendente.get_matricola() == matricola_selected:
                    dipendente_selected = dipendente
            if dipendente_selected is not None:
                self.dipendenti_form = DipendenteForm(callback=self.update_ui, dipendente=dipendente_selected, role="admin")
                return self.dipendenti_form.show()

    def update_ui(self):
        self.handle_filters()
        if self.dipendenti is not None:
            self.table.setRowCount(len(self.dipendenti))
            row = 0
            for dipendente in self.dipendenti:
                self.table.setItem(row, 0, QTableWidgetItem(dipendente.get_matricola()))
                self.table.setItem(row, 1, QTableWidgetItem(dipendente.get_cognome() + " " + dipendente.get_nome()))
                self.table.setItem(row, 2, QTableWidgetItem(dipendente.get_codice_fiscale()))
                self.table.setItem(row, 3, QTableWidgetItem(dipendente.get_ruolo()))
                self.table.setItem(row, 4, QTableWidgetItem(dipendente.get_stato()))
                row += 1

    def handle_filters(self):
        gestore_filtri = GestoreFiltri()
        if ((self.checkbox_attivo.isChecked() and self.checkbox_inattivo.isChecked()) or (
                not (self.checkbox_attivo.isChecked()) and not (self.checkbox_inattivo.isChecked()))):
            self.filtri.set_stato("tutti")
        elif self.checkbox_attivo.isChecked() and not (self.checkbox_inattivo.isChecked()):
            self.filtri.set_stato("attivo")
        else:
            self.filtri.set_stato("inattivo")
        self.filtri.set_search(self.search.text())
        self.filtri.set_ruolo(self.ruolo.currentText())
        self.filtri.set_ordinamento(self.ordinamento.currentText())
        self.dipendenti = gestore_filtri.handle_filtri_list_view_dipendenti(self.filtri)

    def handle_progetti_click(self):
        from View.Progetti.ProgettiTable import ProgettiTable
        self.progetti_table = ProgettiTable()
        self.close()
        return self.progetti_table.show()

    def handle_edit_user_click(self):
        self.find_user = RicercaUser()
        return self.find_user.show()

    def handle_crea_user_click(self):
        self.edit_user = UserForm()
        return self.edit_user.show()
        
    def handle_logout_click(self):
        from View.Users.Login import Login
        self.login = Login()
        self.close()
        return self.login.show()




