from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QPushButton, QLineEdit, QMessageBox, QDesktopWidget

from Gestori.GestoreLingue import GestoreLingue

class LinguaForm(QDialog):

    def __init__(self, callback, curriculum_matricola, lingua=None, last_id=None):
        super(LinguaForm, self).__init__()

        self.gestore_lingue = GestoreLingue()

        self.curriculum_matricola = curriculum_matricola
        self.lingua = lingua
        self.callback = callback
        self.last_id = last_id
        if last_id is None:
            self.last_id = 0

        loadUi("./GUILayout/lingua_form.ui", self)
        self.setWindowTitle("Edit Lingua")
        self.center()

        self.save = self.findChild(QPushButton, "button_save_lingua")
        self.delete = self.findChild(QPushButton, "button_delete_lingua")
        self.cancel = self.findChild(QPushButton, "button_cancel_lingua")

        if self.lingua is None:
            self.delete.hide()

        self.nome = self.findChild(QLineEdit, "lingua_nome")
        self.comprensione = self.findChild(QLineEdit, "lingua_comprensione")
        self.lettura = self.findChild(QLineEdit, "lingua_lettura")
        self.scrittura = self.findChild(QLineEdit, "lingua_scrittura")

        if self.lingua is not None:
            self.nome.setText(self.lingua.get_nome())
            self.comprensione.setText(self.lingua.get_comprensione())
            self.lettura.setText(self.lingua.get_lettura())
            self.scrittura.setText(self.lingua.get_scrittura())

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

        if self.lingua is None:
            self.gestore_lingue.salva_lingua(id=int(self.last_id) + 1,
                                           curriculum_matricola=self.curriculum_matricola,
                                           nome=self.nome.text(),
                                           comprensione=self.comprensione.text(),
                                           lettura=self.lettura.text(),
                                           scrittura=self.scrittura.text())
        else:
            self.gestore_lingue.modifica_lingua(id=self.lingua.get_id(),
                                           curriculum_matricola=self.curriculum_matricola,
                                           nome=self.nome.text(),
                                           comprensione=self.comprensione.text(),
                                           lettura=self.lettura.text(),
                                           scrittura=self.scrittura.text())
        self.callback()
        self.close()

    def handle_delete_click(self):
        self.gestore_lingue.rimuovi_lingua(self.curriculum_matricola, self.lingua.get_id())
        self.callback()
        self.close()



