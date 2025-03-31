import flet as ft

from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        # self dizionario corsi
        self._id_map_corsi = {}
        # il corso selezionato nel menu a tendina
        self.corso_selezionato = None

    def leggiCorsi(self, e): ## Funzione che gestisce il cambiamento della selezione del dropdown
        self.corso_selezionato = self._view.ddCorsi.value
        self._view.update_page()

    def populateDDCorsi(self):
        for corso in self._model.getCorsi():
            self._id_map_corsi[corso.codins] = corso
            self._view.ddCorsi.options.append(ft.dropdown.Option(key=corso.codins, text=corso))
        self._view.update_page()


    def handleCercaIscritti(self, e):
        if self.corso_selezionato is None:
            self._view.create_alert("Selezionare un corso!")
            self._view.update_page()
            return

        iscritti = self._model.getIscritti(self.corso_selezionato)
        if iscritti is None:
            self._view.create_alert("Problema nella connessione!")
            self._view.update_page()
            return

        self._view.txt_result.controls.clear()
        if len(iscritti) == 0:
            self._view.txt_result.controls.append(ft.Text("Non ci sono iscritti al corso"))
            self._view.update_page()
        else:
            self._view.txt_result.controls.append(ft.Text(f"Ci sono {len(iscritti)} iscritti al corso:"))
            for studente in iscritti:
                self._view.txt_result.controls.append(ft.Text(f"{studente}"))
            self._view.update_page()


    def handleCercaStudente(self, e):
        matricola = self._view.txtInMatricola.value
        if matricola == "":
            self._view.create_alert("Inserire una matricola!")
            self._view.update_page()
            return

        studente = self._model.getStudente(matricola)
        if studente is None:
            self._view.create_alert("Matricola non e' presente nel database!")
            self._view.update_page()
            return
        else:
            self._view.txtInNome.value = f"{studente.nome}" #lo trasforma in stringa!!!
            self._view.txtInCognome.value = f"{studente.cognome}"
            self._view.update_page()

    def handleCercaCorsi(self, e):
        matricola = self._view.txtInMatricola.value
        if matricola == "":
            self._view.create_alert("Inserire una matricola!")
            self._view.update_page()
            return

        studente = self._model.getStudente(matricola)
        if studente is None:
            self._view.create_alert("Matricola non e' presente nel database!")
            self._view.update_page()
            return
        else:
            corsiStudente = self._model.getCorsiStudente(matricola)
            self._view.txt_result.controls.append(ft.Text(f"Risultano {len(corsiStudente)}:"))
            for corso in corsiStudente:
                self._view.txt_result.controls.append(ft.Text(f"{corso}"))
            self._view.update_page()


    def handleIscrivi(self, e):
        pass
