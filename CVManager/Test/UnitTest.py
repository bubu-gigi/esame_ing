import datetime
import os.path
from unittest import TestCase

from Gestori.GestoreAttivita import GestoreAttivita
from Gestori.GestoreCurriculum import GestoreCurriculum
from Gestori.GestoreDipendenti import GestoreDipendenti
from Gestori.GestoreLingue import GestoreLingue
from Gestori.Helper import Helper

class UnitTest(TestCase):

    def test_add_dipendente(self):
        self.gestore_dipendente = GestoreDipendenti()
        self.gestore_dipendente.salva_dipendente(99, "mario", "rossi", datetime.datetime(1989, 12, 12),
                                                 "uomo", "ancona",
                                          "BRGGLL02EA271B", "via 123", "40123", "rimini",
                                                "rimini", "diploma", "sviluppatore", "full-stack developer",
                                                 "mariorossi@gmail.com",
                                                "3347578918", "attivo")
        self.dipendenti = Helper.get_all_dipendenti()
        self.assertIsNotNone(self.dipendenti)
        self.assertIn(99, self.dipendenti)

    def test_dipendente_modified(self):
        self.gestore_dipendente = GestoreDipendenti()
        self.gestore_dipendente.modifica_dipendente(99, "fabio", "rossi", datetime.datetime(1989, 12, 12), "uomo",
                                                    "ancona","BRGGLL02EA271B", "via 123", "40123", "rimini",
                                                "rimini", "diploma", "sviluppatore", "full-stack developer",
                                                    "mariorossi@gmail.com",
                                                "3347578918", "attivo")
        self.dipendenti = Helper.get_all_dipendenti()
        self.dip = self.gestore_dipendente.ricerca_dipendente(99)
        self.assertIsNotNone(self.dip)
        self.assertEqual("fabio", str(self.dip.get_nome()))

    def test_generate_curriculum(self):
        self.test_add_dipendente()
        self.test_dipendente_modified()
        self.gestore_dipendente = GestoreDipendenti()
        self.gestore_curriculum = GestoreCurriculum()
        self.gestore_lingue = GestoreLingue()
        self.gestore_attivita = GestoreAttivita()
        self.gestore_curriculum.salva_curriculum(99, "Full-Stack Developer", ">13 anni gruppo INF",
                                                 "lavoratore egregio",
                                                 "soft skill, pyhton ,php", "laurea in ingegneria informatica presso UNIVPM")
        self.gestore_lingue.salva_lingua(1, 99, "italiano", "madrelingua",
                                         "madrelingua", "madrelingua")
        self.gestore_lingue.salva_lingua(2, 99, "inglese", "buono", "buono", "buono")
        self.gestore_attivita.salva_attivita(1, 99, "UNIVPM", "ingegneria del software",
                                             "tesina per esame", "marzo-2024 to giugno-2024")
        self.gestore_attivita.salva_attivita(2, 99, "INF", "CV Manager",
                                             "progetto per gestione dei cv di dipendenti di un'azienda ", "2023-ora")
        self.gestore_curriculum.generate_curriculum(self.gestore_curriculum.ricerca_curriculum(99),
                                                    self.gestore_dipendente.ricerca_dipendente(99))
        self.lingue = self.gestore_curriculum.ricerca_curriculum_lingue(99)
        self.attivita = self.gestore_curriculum.ricerca_curriculum_attivita(99)
        self.assertEqual(2, len(self.lingue))
        self.assertEqual(2, len(self.attivita))
        self.assertIsNotNone(self.gestore_curriculum.ricerca_curriculum(99))
        self.assertTrue(os.path.isdir('dipendenti_curriculum/fabio_rossi'))


    def test_dipendente_removed(self):
        self.gestore_dipendente = GestoreDipendenti()
        self.gestore_dipendente.rimuovi_dipendente(99)
        self.dipendenti = Helper.get_all_dipendenti()
        self.dip = self.gestore_dipendente.ricerca_dipendente(99)
        self.assertIsNone(self.dip)


