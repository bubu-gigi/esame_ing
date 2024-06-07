from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QPushButton, QLineEdit, QMessageBox, QTextEdit, QDesktopWidget

from Gestori.GestoreAttivita import GestoreAttivita

class AttivitaForm(QDialog):

    def __init__(self, callback, curriculum_matricola, attivita=None, last_id=None):
        super(AttivitaForm, self).__init__()
        self.curriculum_matricola = curriculum_matricola
        self.attivita = attivita
        self.callback = callback
        self.last_id = last_id
        self.gestore_attivita = GestoreAttivita()

        if last_id is None:
            self.last_id = 0

        loadUi("./GUILayout/attivita_form.ui", self)
        self.setWindowTitle("Edit Attivita")
        self.center()

        self.save = self.findChild(QPushButton, "button_save_attivita")
        self.delete = self.findChild(QPushButton, "button_delete_attivita")
        self.cancel = self.findChild(QPushButton, "button_cancel_attivita")

        if self.attivita is None:
            self.delete.hide()

        self.azienda = self.findChild(QLineEdit, "attivita_azienda")
        self.periodo = self.findChild(QLineEdit, "attivita_periodo")
        self.progetto = self.findChild(QLineEdit, "attivita_progetto")
        self.descrizione = self.findChild(QTextEdit, "attivita_descrizione")

        if self.attivita is not None:
            self.azienda.setText(self.attivita.get_azienda())
            self.periodo.setText(self.attivita.get_periodo())
            self.progetto.setText(self.attivita.get_progetto())
            self.descrizione.setPlainText(self.attivita.get_descrizione())

        self.save.clicked.connect(self.handle_save_click)
        self.delete.clicked.connect(self.handle_delete_click)
        self.cancel.clicked.connect(self.handle_cancel_click)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def handle_cancel_click(self):
        self.close()

    def handle_save_click(self):
        lines_children = self.findChildren(QLineEdit)

        for l in lines_children:
            if l.text() == "":
                QMessageBox.critical(self, 'Errore', "Compila tutti i campi", QMessageBox.Ok, QMessageBox.Ok)
                return

        if self.descrizione.toPlainText() == "":
            QMessageBox.critical(self, 'Errore', "Compila tutti i campi", QMessageBox.Ok, QMessageBox.Ok)
            return

        if self.attivita is None:
            self.gestore_attivita.salva_attivita(id=int(self.last_id) + 1,
                                           curriculum_matricola=self.curriculum_matricola,
                                           azienda=self.azienda.text(),
                                           periodo=self.periodo.text(),
                                           progetto=self.progetto.text(),
                                           descrizione=self.descrizione.toPlainText())
        else:
            self.gestore_attivita.modifica_attivita(id=self.attivita.get_id(),
                                               curriculum_matricola=self.curriculum_matricola,
                                               azienda=self.azienda.text(),
                                               periodo=self.periodo.text(),
                                               progetto=self.progetto.text(),
                                               descrizione=self.descrizione.toPlainText())

        self.callback()
        self.close()

    def handle_delete_click(self):
        self.gestore_attivita.rimuovi_attivita(self.curriculum_matricola, self.attivita.get_id())
        self.callback()
        self.close()



