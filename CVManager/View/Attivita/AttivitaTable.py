from PyQt5.QtWidgets import QWidget, QTableWidget, QPushButton, QTableWidgetItem, QDesktopWidget
from PyQt5.uic import loadUi

from Gestori.GestoreCurriculum import GestoreCurriculum
from View.Attivita.AttivitaForm import AttivitaForm

class AttivitaTable(QWidget):

    def __init__(self, curriculum, dipendente):
        super(AttivitaTable, self).__init__()
        self.curriculum_form = None
        self.attivita_form = None
        loadUi("./GUILayout/attivita_table.ui", self)

        self.setWindowTitle("Attivita")
        self.center()

        self.curriculum = curriculum
        self.dipendente = dipendente
        self.attivita = []
        self.gestore_curriculum = GestoreCurriculum()

        self.table = self.findChild(QTableWidget, "attivita_table_widget")
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(('Id', 'Azienda', 'Periodo', 'Progetto', 'Descrizione'))
        self.table.setColumnWidth(0, 10)
        self.table.setColumnWidth(1, 200)
        self.table.setColumnWidth(2, 200)
        self.table.setColumnWidth(3, 200)
        self.table.setColumnWidth(4, 199)

        self.cancel = self.findChild(QPushButton, "button_cancel_attivita_table")
        self.aggiorna = self.findChild(QPushButton, "button_aggiorna_attivita_table")
        self.aggiungi = self.findChild(QPushButton, "button_aggiungi_attivita_table")

        self.cancel.clicked.connect(self.handle_cancel_click)
        self.aggiorna.clicked.connect(self.handle_aggiorna_click)
        self.aggiungi.clicked.connect(self.handle_aggiungi_click)

        self.update_ui()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def handle_aggiungi_click(self):
        self.attivita = self.gestore_curriculum.ricerca_curriculum_attivita(self.curriculum.get_dipendente_matricola())
        last_id = None
        if self.attivita is not None and len(self.attivita) > 0:
            ids = []
            for attivita in self.attivita:
                ids.append(int(attivita.get_id()))
            last_id = max(ids)
        self.attivita_form = AttivitaForm(callback=self.update_ui, curriculum_matricola=self.curriculum.get_dipendente_matricola(), attivita=None, last_id=last_id)
        return self.attivita_form.show()

    def handle_aggiorna_click(self):
        r = self.table.currentRow()
        if (r != -1):
            attivita_selected = None
            for attivita in self.attivita:
                if str(attivita.get_id()) == str(self.table.item(r, 0).text()) and int(attivita.get_curriculum_matricola()) == int(self.curriculum.get_dipendente_matricola()):
                    attivita_selected = attivita
            if attivita_selected is not None:
                self.attivita_form = AttivitaForm(callback=self.update_ui, curriculum_matricola=self.curriculum.get_dipendente_matricola(), attivita=attivita_selected, last_id=None)
                return self.attivita_form.show()

    def handle_cancel_click(self):
        from View.Curriculum.CurriculumForm import CurriculumForm
        self.curriculum_form = CurriculumForm(dipendente=self.dipendente, curriculum=self.curriculum)
        self.close()
        return self.curriculum_form.show()

    def update_ui(self):
        self.attivita = self.gestore_curriculum.ricerca_curriculum_attivita(self.curriculum.get_dipendente_matricola())
        if self.attivita is not None:
            self.table.setRowCount(len(self.attivita))
            if self.attivita is not None:
                row = 0
                for attivita in self.attivita:
                    self.table.setItem(row, 0, QTableWidgetItem(str(attivita.get_id())))
                    self.table.setItem(row, 1, QTableWidgetItem(attivita.get_azienda()))
                    self.table.setItem(row, 2, QTableWidgetItem(attivita.get_periodo()))
                    self.table.setItem(row, 3, QTableWidgetItem(attivita.get_progetto()))
                    self.table.setItem(row, 4, QTableWidgetItem(attivita.get_descrizione()))
                    row += 1
