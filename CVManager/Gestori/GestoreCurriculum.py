import pickle
import os
from time import strftime, gmtime

import jinja2
import pdfkit

from Models.Curriculum import Curriculum
from Gestori.Helper import Helper


class GestoreCurriculum:

    def __init__(self):
        self.curriculum = Helper.get_all_curriculum()
        self.attivita = Helper.get_all_attivita()
        self.lingue = Helper.get_all_lingue()

    def ricerca_curriculum(self, dipendente_matricola: int):
        self.curriculum = Helper.get_all_curriculum()
        if self.curriculum is not None and len(self.curriculum) != 0:
            for c in self.curriculum.values():
                if int(c.get_dipendente_matricola()) == int(dipendente_matricola):
                    return c
        else:
            return None

    def ricerca_curriculum_attivita(self, dipendente_matricola: int):
        self.curriculum = Helper.get_all_curriculum()
        self.attivita = Helper.get_all_attivita()
        check_if_curriculum_exixsts = self.ricerca_curriculum(dipendente_matricola)
        attivita_list_returned = []
        if check_if_curriculum_exixsts is not None:
            if self.attivita is not None:
                for att in self.attivita.values():
                    if int(att.get_curriculum_matricola()) == int(dipendente_matricola):
                        attivita_list_returned = self.__aggiungi_attivita_alla_lista(attivita_list_returned, att)
            return attivita_list_returned

    def __aggiungi_attivita_alla_lista(self, attivita_list, attivita):
        attivita_list.append(attivita)
        return attivita_list

    def ricerca_curriculum_lingue(self, dipendente_matricola: int):
        self.curriculum = Helper.get_all_curriculum()
        self.lingue = Helper.get_all_lingue()
        check_if_curriculum_exixsts = self.ricerca_curriculum(dipendente_matricola)
        lingue_list_returned = []
        if check_if_curriculum_exixsts is not None:
            if self.lingue is not None:
                for lingua in self.lingue.values():
                    if int(lingua.get_curriculum_matricola()) == int(dipendente_matricola):
                        lingue_list_returned = self.__aggiungi_lingua_alla_lista(lingue_list_returned, lingua)
            return lingue_list_returned

    def __aggiungi_lingua_alla_lista(self, lingue_list, lingua):
        lingue_list.append(lingua)
        return lingue_list

    def salva_curriculum(self, dipendente_matricola, funzione, esperienza, sintesi, competenze, formazione):
        self.curriculum = Helper.get_all_curriculum()
        curriculum = Curriculum()
        curriculum.set_dipendente_matricola(dipendente_matricola)
        curriculum.set_funzione(funzione)
        curriculum.set_esperienza(esperienza)
        curriculum.set_sintesi(sintesi)
        curriculum.set_competenze(competenze)
        curriculum.set_formazione(formazione)
        check_if_curriculum_exixsts = self.ricerca_curriculum(dipendente_matricola)
        if check_if_curriculum_exixsts is None:
            if self.curriculum is None:
                self.curriculum = {}
            self.curriculum[curriculum.get_dipendente_matricola()] = curriculum
            with open('Dati/Curriculum.pickle', 'wb') as f:
                pickle.dump(self.curriculum, f, pickle.HIGHEST_PROTOCOL)

    def modifica_curriculum(self, dipendente_matricola, funzione, esperienza, sintesi, competenze, formazione):
        self.curriculum = Helper.get_all_curriculum()
        curriculum = Curriculum()
        curriculum.set_dipendente_matricola(dipendente_matricola)
        curriculum.set_funzione(funzione)
        curriculum.set_esperienza(esperienza)
        curriculum.set_sintesi(sintesi)
        curriculum.set_competenze(competenze)
        curriculum.set_formazione(formazione)
        check_if_curriculum_exixsts = self.ricerca_curriculum(dipendente_matricola)
        if check_if_curriculum_exixsts is not None:
            self.curriculum[curriculum.get_dipendente_matricola()] = curriculum
            with open('Dati/Curriculum.pickle', 'wb') as f:
                pickle.dump(self.curriculum, f, pickle.HIGHEST_PROTOCOL)

    def rimuovi_curriculum(self, dipendente_matricola: int):
        self.curriculum = Helper.get_all_curriculum()
        check_if_curriculum_exixsts = self.ricerca_curriculum(dipendente_matricola)
        if check_if_curriculum_exixsts is not None:
            del self.curriculum[dipendente_matricola]
            with open('Dati/Curriculum.pickle', 'wb') as f:
                pickle.dump(self.curriculum, f, pickle.HIGHEST_PROTOCOL)

    def generate_curriculum(self, curriculum, dipendente):
        attivita = self.ricerca_curriculum_attivita(curriculum.get_dipendente_matricola())
        lingue = self.ricerca_curriculum_lingue(curriculum.get_dipendente_matricola())
        nome_cognome = dipendente.get_nome() + " " + dipendente.get_cognome()
        posizione = curriculum.get_funzione()
        esperienza = curriculum.get_esperienza()
        sintesi = curriculum.get_sintesi()
        formazione = curriculum.get_formazione()
        competenze = curriculum.get_competenze()

        list_attivita_li = ""
        list_lingue_td = ""

        if attivita is not None:
            for a in attivita:
                li = "<li><b>" + a.get_periodo() + "-" + a.get_progetto() + "-" + a.get_azienda() + "</b></br>" + a.get_descrizione() + "</li>"
                list_attivita_li += li

        if lingue is not None:
            for l in lingue:
                td = ("<tr>" +
                      "<td><b>" + l.get_nome() + "</b></td>" +
                      "<td>" + l.get_comprensione() + "</td>" +
                      "<td>" + l.get_lettura() + "</td>" +
                      "<td>" + l.get_scrittura() + "</td>" +
                      "</tr>")
                list_lingue_td += td

        attivita = list_attivita_li
        lingue = list_lingue_td

        context = {
            'nome_cognome': nome_cognome,
            'posizione': posizione,
            'esperienza': esperienza,
            'formazione': formazione,
            'competenze': competenze,
            'sintesi': sintesi,
            'attivita': attivita,
            'lingue': lingue
        }

        self.generatePDF(context, dipendente)

    def generatePDF(self, context, dipendente):
        template_loader = jinja2.FileSystemLoader('./Gestori/')
        template_env = jinja2.Environment(loader=template_loader)

        template = template_env.get_template("CvTemplate.html")
        output_text = template.render(context)

        config = pdfkit.configuration(wkhtmltopdf="/usr/bin/wkhtmltopdf")

        if not os.path.exists("./dipendenti_curriculum"):
            os.makedirs("./dipendenti_curriculum")

        if not os.path.exists("./dipendenti_curriculum/" + dipendente.get_nome() + "_" + dipendente.get_cognome()):
            os.makedirs("./dipendenti_curriculum/" + dipendente.get_nome() + "_" + dipendente.get_cognome())

        pdfkit.from_string(output_text,
                           './dipendenti_curriculum/' + dipendente.get_nome() + "_" + dipendente.get_cognome() + '/' + dipendente.get_nome() + '_' + dipendente.get_cognome() + '_' + strftime(
                               "%Y-%m-%d_%H:%M:%S", gmtime()) + '.pdf', configuration=config)
