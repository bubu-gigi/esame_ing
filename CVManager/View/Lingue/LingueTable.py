from PyQt5.QtWidgets import QWidget, QTableWidget, QPushButton, QTableWidgetItem, QDesktopWidget
from PyQt5.uic import loadUi

from Gestori.GestoreCurriculum import GestoreCurriculum
from View.Lingue.LinguaForm import LinguaForm

class LingueTable(QWidget):

    def __init__(self, curriculum, dipendente):
        super(LingueTable, self).__init__()
        self.lingua_form = None
        self.curricula_form = None
        loadUi("./GUILayout/lingue_table.ui", self)

        self.setWindowTitle("Lingue")
        self.center()

        self.gestore_curriculum = GestoreCurriculum()

        self.curriculum = curriculum
        self.dipendente = dipendente
        self.lingue = []

        self.table = self.findChild(QTableWidget, "tableWidget")
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(('Id', 'Nome', 'Comprensione', 'Lettura', 'Scrittua'))
        self.table.setColumnWidth(0, 10)
        self.table.setColumnWidth(1, 200)
        self.table.setColumnWidth(2, 200)
        self.table.setColumnWidth(3, 200)
        self.table.setColumnWidth(4, 199)

        self.cancel = self.findChild(QPushButton, "button_cancel_lingue_table")
        self.aggiorna = self.findChild(QPushButton, "button_aggiorna_lingue_table")
        self.aggiungi = self.findChild(QPushButton, "button_aggiungi_lingue_table")

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
        self.lingue = self.gestore_curriculum.ricerca_curriculum_lingue(self.curriculum.get_dipendente_matricola())
        last_id = None
        if self.lingue is not None and len(self.lingue) > 0:
            ids = []
            for lingua in self.lingue:
                ids.append(int(lingua.get_id()))
            last_id = max(ids)
        self.lingua_form = LinguaForm(callback=self.update_ui, curriculum_matricola=self.curriculum.get_dipendente_matricola(), lingua=None, last_id=last_id)
        return self.lingua_form.show()

    def handle_aggiorna_click(self):
        r = self.table.currentRow()
        if (r != -1):
            lingua_selected = None
            for lingua in self.lingue:
                if int(lingua.get_curriculum_matricola()) == int(self.curriculum.get_dipendente_matricola()) and str(lingua.get_id()) == str(self.table.item(r, 0).text()):
                    lingua_selected = lingua
            if lingua_selected is not None:
                self.lingua_form = LinguaForm(callback=self.update_ui, curriculum_matricola=self.curriculum.get_dipendente_matricola(), lingua=lingua_selected, last_id=None)
                return self.lingua_form.show()

    def handle_cancel_click(self):
        from View.Curriculum.CurriculumForm import CurriculumForm
        self.curricula_form = CurriculumForm(dipendente=self.dipendente, curriculum=self.curriculum)
        self.close()
        return self.curricula_form.show()

    def update_ui(self):
        self.lingue = self.gestore_curriculum.ricerca_curriculum_lingue(self.curriculum.get_dipendente_matricola())
        self.table.setRowCount(len(self.lingue))
        if self.lingue is not None:
            row = 0
            for lingua in self.lingue:
                self.table.setItem(row, 0, QTableWidgetItem(str(lingua.get_id())))
                self.table.setItem(row, 1, QTableWidgetItem(lingua.get_nome()))
                self.table.setItem(row, 2, QTableWidgetItem(lingua.get_comprensione()))
                self.table.setItem(row, 3, QTableWidgetItem(lingua.get_lettura()))
                self.table.setItem(row, 4, QTableWidgetItem(lingua.get_scrittura()))
                row += 1