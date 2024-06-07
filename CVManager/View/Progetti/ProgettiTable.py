from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QPushButton, QTableWidget, QTableWidgetItem, QLineEdit, QComboBox, QWidget, QDesktopWidget

from Gestori.GestoreFiltri import GestoreFiltri
from Models.Filters.FiltriProgetti import FiltriProgetti
from View.Progetti.ProgettoForm import ProgettoForm
from View.Users.RicercaUser import RicercaUser
from View.Users.UserForm import UserForm


class ProgettiTable(QWidget):
    def __init__(self):
        super(ProgettiTable, self).__init__()
        self.login = None
        self.progetto_form = None
        self.dipendenti_table = None
        loadUi("./GUILayout/progetti_table.ui", self)

        self.setWindowTitle("Progetti")
        self.center()

        self.progetti = []
        self.filtri = FiltriProgetti()
        self.gestore_filtri = GestoreFiltri()


        self.search = self.findChild(QLineEdit, "search_progetti")
        self.search.textChanged.connect(self.update_ui)

        self.tipologia = self.findChild(QComboBox, "combobox_tipologia_progetti")
        tipologia_list = ["tutti", "progetto operativo", "progetto interno", "gara"]
        self.tipologia.addItems(tipologia_list)
        self.tipologia.currentTextChanged.connect(self.update_ui)

        self.stato = self.findChild(QComboBox, "combobox_stato_progetti")
        stato_list = ["tutti", "in corso", "da avviare", "chiuso"]
        self.stato.addItems(stato_list)
        self.stato.currentTextChanged.connect(self.update_ui)

        self.ordinamento = self.findChild(QComboBox, "combobox_ordinamento")
        ordinamento_list = ["alfabetico ascendente", "alfabetico discendente"]
        self.ordinamento.addItems(ordinamento_list)
        self.ordinamento.currentTextChanged.connect(self.update_ui)

        self.table = self.findChild(QTableWidget, "table_progetti")
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(('PM Matricola', 'Titolo', 'Tipologia', 'Stato'))
        self.table.setColumnWidth(0, 100)
        self.table.setColumnWidth(1, 285)
        self.table.setColumnWidth(2, 286)
        self.table.setColumnWidth(3, 285)

        self.aggiungi = self.findChild(QPushButton, "button_aggiungi_progetto")
        self.aggiungi.clicked.connect(self.handle_aggiungi_progetto_click)
        self.aggiorna = self.findChild(QPushButton, "button_aggiorna_progetto")
        self.aggiorna.clicked.connect(self.handle_aggiorna_progetto_click)
        self.dipendenti = self.findChild(QPushButton, "button_dipendenti")
        self.dipendenti.clicked.connect(self.handle_dipendenti_click)
        self.button_crea_user = self.findChild(QPushButton, "button_crea_user")
        self.button_crea_user.clicked.connect(self.handle_crea_user_click)
        self.button_edit_user = self.findChild(QPushButton, "button_edit_user")
        self.button_edit_user.clicked.connect(self.handle_edit_user_click)
        self.button_logout = self.findChild(QPushButton, "button_logout")
        self.button_logout.clicked.connect(self.handle_logout_click)
        self.button_azzera_filtri = self.findChild(QPushButton, "button_azzera_filtri")
        self.button_azzera_filtri.clicked.connect(self.handle_azzera_filtri_click)

        self.update_ui()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


    def handle_azzera_filtri_click(self):
        self.search.setText("")
        self.tipologia.setCurrentText("tutti")
        self.stato.setCurrentText("tutti")
        self.ordinamento.setCurrentText("alfabetico ascendente")

    def handle_aggiungi_progetto_click(self):
        self.progetto_form = ProgettoForm(callback=self.update_ui, progetto=None)
        return self.progetto_form.show()

    def handle_aggiorna_progetto_click(self):
        r = self.table.currentRow()
        if(r != -1):
            titolo = self.table.item(r, 1).text()
            progetto_selected = None
            for progetto in self.progetti:
                if progetto.get_titolo() == titolo:
                    progetto_selected = progetto
            if progetto_selected != None:
                pass
                self.progetto_form = ProgettoForm(callback=self.update_ui, progetto=progetto_selected)
                return self.progetto_form.show()

    def update_ui(self):
        self.handle_filters()
        if self.progetti is not None:
            self.table.setRowCount(len(self.progetti))
            row = 0
            for progetto in self.progetti:
                self.table.setItem(row, 0, QTableWidgetItem(progetto.get_pm_matricola()))
                self.table.setItem(row, 1, QTableWidgetItem(progetto.get_titolo()))
                self.table.setItem(row, 2, QTableWidgetItem(progetto.get_tipologia()))
                self.table.setItem(row, 3, QTableWidgetItem(progetto.get_stato()))
                row += 1

    def handle_filters(self):
        self.filtri.set_search(self.search.text())
        self.filtri.set_tipologia(self.tipologia.currentText())
        self.filtri.set_stato(self.stato.currentText())
        self.filtri.set_ordinamento(self.ordinamento.currentText())
        self.progetti = self.gestore_filtri.handle_filtri_list_view_progetti(self.filtri)

    def handle_dipendenti_click(self):
        from View.Dipendenti.DipendentiTable import DipendentiTable
        self.dipendenti_table = DipendentiTable()
        self.close()
        return self.dipendenti_table.show()
        
    def handle_logout_click(self):
        from View.Users.Login import Login
        self.login = Login()
        self.close()
        return self.login.show()

    def handle_edit_user_click(self):
        self.find_user = RicercaUser()
        return self.find_user.show()

    def handle_crea_user_click(self):
        self.edit_user = UserForm()
        return self.edit_user.show()

