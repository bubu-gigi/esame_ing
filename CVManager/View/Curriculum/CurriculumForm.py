from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QPushButton, QLineEdit, QMessageBox, QTextEdit, QDesktopWidget

from Gestori.GestoreCurriculum import GestoreCurriculum
from View.Attivita.AttivitaTable import AttivitaTable

from View.Lingue.LingueTable import LingueTable


class CurriculumForm(QDialog):

    def __init__(self, dipendente=None, curriculum=None, role="dipendente"):
        super(CurriculumForm, self).__init__()
        self.gestore_curriculum = GestoreCurriculum()
        self.dipendente_form = None
        self.lingue_table = None
        self.attivita_table = None
        self.curriculum = curriculum
        self.dipendente = dipendente
        self.role = role

        loadUi("./GUILayout/curricula_form.ui", self)
        self.setWindowTitle("Curriculum")
        self.center()

        self.save = self.findChild(QPushButton, "button_save_curricula")
        self.lingua = self.findChild(QPushButton, "button_show_lingue")
        self.attivita = self.findChild(QPushButton, "button_show_attivita")
        self.cancel = self.findChild(QPushButton, "button_cancel_curricula")
        self.generate = self.findChild(QPushButton, "button_generate_curricula")

        if self.curriculum is None:
            self.lingua.hide()
            self.attivita.hide()
            self.generate.hide()

        if self.role == "dipendente":
            self.generate.hide()

        self.funzione = self.findChild(QLineEdit, "funzione")
        self.esperienza = self.findChild(QLineEdit, "esperienza")
        self.sintesi = self.findChild(QTextEdit, "sintesi")
        self.formazione = self.findChild(QTextEdit, "formazione")
        self.competenze = self.findChild(QTextEdit, "competenze")

        if curriculum is not None:
            self.funzione.setText(curriculum.get_funzione())
            self.esperienza.setText(curriculum.get_esperienza())
            self.sintesi.setPlainText(curriculum.get_sintesi())
            self.formazione.setPlainText(curriculum.get_formazione())
            self.competenze.setPlainText(curriculum.get_competenze())

        self.save.clicked.connect(self.handle_save_click)
        self.lingua.clicked.connect(self.handle_lingue_click)
        self.attivita.clicked.connect(self.handle_attivita_click)
        self.cancel.clicked.connect(self.handle_cancel_click)
        self.generate.clicked.connect(self.handle_generate_click)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def handle_cancel_click(self):
        from View.Dipendenti.DipendenteForm import DipendenteForm
        self.dipendente_form = DipendenteForm(dipendente=self.dipendente)
        self.close()
        return self.dipendente_form.show()

    def handle_save_click(self):
        lines_children = self.findChildren(QLineEdit)
        text_edit_children = self.findChildren(QTextEdit)

        for l in lines_children:
            if(l.text() == ""):
                QMessageBox.critical(self, 'Errore', "Compila tutti i campi", QMessageBox.Ok, QMessageBox.Ok)
                return

        for t in text_edit_children:
            if(t.toPlainText() == ""):
                QMessageBox.critical(self, 'Errore', "Compila tutti i campi", QMessageBox.Ok, QMessageBox.Ok)
                return


        self.gestore_curriculum.salva_curriculum(dipendente_matricola=self.dipendente.get_matricola(),
                                           funzione=self.funzione.text(),
                                           esperienza=self.esperienza.text(),
                                           sintesi=self.sintesi.toPlainText(),
                                           competenze=self.competenze.toPlainText(),
                                           formazione=self.formazione.toPlainText())

        self.gestore_curriculum.modifica_curriculum(dipendente_matricola=self.dipendente.get_matricola(),
                                               funzione=self.funzione.text(),
                                               esperienza=self.esperienza.text(),
                                               sintesi=self.sintesi.toPlainText(),
                                               competenze=self.competenze.toPlainText(),
                                               formazione=self.formazione.toPlainText())
        from View.Dipendenti.DipendenteForm import DipendenteForm
        self.dipendente_form = DipendenteForm(dipendente=self.dipendente)
        self.close()
        return self.dipendente_form.show()

    def handle_lingue_click(self):
        self.lingue_table = LingueTable(curriculum=self.curriculum, dipendente=self.dipendente)
        self.close()
        return self.lingue_table.show()

    def handle_attivita_click(self):
        self.attivita_table = AttivitaTable(curriculum=self.curriculum, dipendente=self.dipendente)
        self.close()
        return self.attivita_table.show()

    def handle_generate_click(self):
        self.gestore_curriculum.generate_curriculum(curriculum=self.curriculum, dipendente=self.dipendente)