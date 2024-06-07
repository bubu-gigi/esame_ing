from datetime import datetime

from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QPushButton, QLineEdit, QMessageBox, QComboBox, QDesktopWidget

from Gestori.GestoreCurriculum import GestoreCurriculum
from Gestori.GestoreDipendenti import GestoreDipendenti
from Gestori.Helper import Helper
from View.Curriculum.CurriculumForm import CurriculumForm


class DipendenteForm(QDialog):

    def __init__(self, callback=None, dipendente=None, role="dipendente"):
        super(DipendenteForm, self).__init__()

        self.gestore_dipendenti = GestoreDipendenti()

        self.dipendenti_table = None
        self.curriculum_form = None
        self.callback = callback
        self.dipendente = dipendente
        self.role = role
        loadUi("./GUILayout/dipendenti_form.ui", self)
        self.setWindowTitle("Edit Dipendente")
        self.center()

        self.ok = self.findChild(QPushButton, "button_save")
        self.curriculum = self.findChild(QPushButton, "button_curricula")
        self.delete = self.findChild(QPushButton, "button_delete")
        self.cancel = self.findChild(QPushButton, "button_cancel")

        if dipendente is None:
            self.delete.hide()
            self.curriculum.hide()

        if role == "dipendente":
            self.delete.hide()


        self.matricola = self.findChild(QLineEdit, "dip_matricola")
        self.nome = self.findChild(QLineEdit, "dip_nome")
        self.cognome = self.findChild(QLineEdit, "dip_cognome")
        self.data_nascita = self.findChild(QLineEdit, "dip_data_nascita")
        self.genere = self.findChild(QLineEdit, "dip_genere")
        self.citta_nascita = self.findChild(QLineEdit, "dip_citta_nascita")
        self.codice_fiscale = self.findChild(QLineEdit, "dip_codice_fiscale")
        self.indirizzo = self.findChild(QLineEdit, "dip_indirizzo")
        self.cap = self.findChild(QLineEdit, "dip_cap")
        self.comune = self.findChild(QLineEdit, "dip_comune")
        self.provincia = self.findChild(QLineEdit, "dip_provincia")
        self.titolo_studio = self.findChild(QLineEdit, "dip_titolo_studio")
        self.ruolo = self.findChild(QComboBox, "combobox_ruolo")
        self.funzione = self.findChild(QLineEdit, "dip_funzione")
        self.email_aziendale = self.findChild(QLineEdit, "dip_email_aziendale")
        self.telefono = self.findChild(QLineEdit, "dip_telefono")
        self.stato = self.findChild(QComboBox, "combobox_stato")

        ruoli_list = ["sviluppatore", "manager", "sistemista", "amministrazione", "redazione"]
        stato_list = ["attivo", "inattivo"]

        self.ruolo.addItems(ruoli_list)
        self.stato.addItems(stato_list)

        if dipendente is not None:
            self.matricola.setText(dipendente.get_matricola())
            self.nome.setText(dipendente.get_nome())
            self.cognome.setText(dipendente.get_cognome())
            self.data_nascita.setText(Helper.map_data_to_format(str(dipendente.get_data_nascita())))
            self.genere.setText(dipendente.get_genere())
            self.citta_nascita.setText(dipendente.get_citta_nascita())
            self.codice_fiscale.setText(dipendente.get_codice_fiscale())
            self.indirizzo.setText(dipendente.get_indirizzo())
            self.cap.setText(dipendente.get_cap())
            self.comune.setText(dipendente.get_comune())
            self.provincia.setText(dipendente.get_provincia())
            self.titolo_studio.setText(dipendente.get_titolo_studio())
            self.ruolo.setCurrentText(dipendente.get_ruolo())
            self.funzione.setText(dipendente.get_funzione())
            self.email_aziendale.setText(dipendente.get_email_aziendale())
            self.telefono.setText(dipendente.get_telefono())
            self.stato.setCurrentText(dipendente.get_stato())

        self.ok.clicked.connect(self.handle_save_click)
        self.curriculum.clicked.connect(self.handle_curriculum_click)
        self.cancel.clicked.connect(self.handle_cancel_click)
        self.delete.clicked.connect(self.handle_delete_click)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def handle_save_click(self):
        try:
            int(self.matricola.text())
        except:
            QMessageBox.critical(self, 'Errore', 'La matricola deve essere un numero', QMessageBox.Ok, QMessageBox.Ok)
            return
        children = self.findChildren(QLineEdit)
        for c in children:
            if (c.text() == ""):
                QMessageBox.critical(self, 'Errore', "Compila tutti i campi", QMessageBox.Ok, QMessageBox.Ok)
                return
        if self.ruolo.currentText() == "" or self.stato.currentText() == "":
            QMessageBox.critical(self, 'Errore', "Compila tutti i campi", QMessageBox.Ok, QMessageBox.Ok)
            return

        if self.dipendente is None:
            self.gestore_dipendenti.salva_dipendente(matricola=self.matricola.text(), nome=self.nome.text(),
                                                   cognome=self.cognome.text(),
                                                   data_nascita=datetime.strptime(self.data_nascita.text(), '%d/%m/%Y'),
                                                   genere=self.genere.text(), citta_nascita=self.citta_nascita.text(),
                                                   codice_fiscale=self.codice_fiscale.text(),
                                                   indirizzo=self.indirizzo.text(), cap=self.cap.text(),
                                                   comune=self.comune.text(), provincia=self.provincia.text(),
                                                   titolo_studio=self.titolo_studio.text(),
                                                   ruolo=self.ruolo.currentText(), funzione=self.funzione.text(),
                                                   email_aziendale=self.email_aziendale.text(),
                                                   telefono=self.telefono.text(),
                                                   stato=self.stato.currentText())
        else:
            self.gestore_dipendenti.modifica_dipendente(matricola=self.matricola.text(), nome=self.nome.text(),
                                                   cognome=self.cognome.text(),
                                                   data_nascita=datetime.strptime(self.data_nascita.text(), '%d/%m/%Y'),
                                                   genere=self.genere.text(), citta_nascita=self.citta_nascita.text(),
                                                   codice_fiscale=self.codice_fiscale.text(),
                                                   indirizzo=self.indirizzo.text(), cap=self.cap.text(),
                                                   comune=self.comune.text(), provincia=self.provincia.text(),
                                                   titolo_studio=self.titolo_studio.text(),
                                                   ruolo=self.ruolo.currentText(), funzione=self.funzione.text(),
                                                   email_aziendale=self.email_aziendale.text(),
                                                   telefono=self.telefono.text(),
                                                   stato=self.stato.currentText())
        if self.callback is not None:
            self.callback()
        if self.role == "admin":
            self.close()

    def handle_cancel_click(self):
        self.close()

    def handle_delete_click(self):
        feedback = self.gestore_dipendenti.rimuovi_dipendente(self.dipendente.get_matricola())
        if feedback == "ok":
            self.close()
        else:
            QMessageBox.critical(self, 'Errore', "Errore nell'eliminazione del dipendente. Riprova", QMessageBox.Ok,
                                 QMessageBox.Ok)

    def handle_curriculum_click(self):
        gestore_curriculum = GestoreCurriculum()
        curriculum = gestore_curriculum.ricerca_curriculum(self.dipendente.get_matricola())
        self.curriculum_form = CurriculumForm(dipendente=self.dipendente, curriculum=curriculum)
        self.close()
        return self.curriculum_form.show()

