import flet as ft
from UI.view import View
from model.model import Autonoleggio

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view : View, model : Autonoleggio):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # --- EVENTO: MOSTRA TUTTE LE AUTO ---
    def mostra_automobili(self, e):
        """Mostra l'elenco completo delle automobili nel database."""
        self._view.lista_auto.controls.clear()
        automobili = self._model.get_automobili()

        if not automobili:
            self._view.show_alert("Nessuna automobile trovata nel database.")
            return

        for auto in automobili:
            self._view.lista_auto.controls.append(ft.Text(str(auto)))

        self._view.update()

    # --- EVENTO: CERCA AUTO PER MODELLO ---
    def cerca_auto_modello(self, e):
        """Cerca automobili per modello e aggiorna la lista di ricerca."""
        modello = self._view.input_modello_auto.value.strip()
        if not modello:
            self._view.show_alert("Inserisci un modello da cercare.")
            return

        self._view.lista_auto_ricerca.controls.clear()
        automobili = self._model.cerca_automobili_per_modello(modello)

        if not automobili:
            self._view.show_alert("Nessuna automobile trovata per il modello indicato.")
            return

        for auto in automobili:
            self._view.lista_auto_ricerca.controls.append(ft.Text(str(auto)))

        self._view.update()