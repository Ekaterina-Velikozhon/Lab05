import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab 05 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.ddCorsi = None
        self.btnCercaIscritti = None
        self.txtInMatricola = None
        self.txtInNome = None
        self.txtInCognome = None
        self.btnCercaStudente = None
        self.btnCercaStudente = None
        self.btnIscrivi = None
        self.txt_result = None


    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW1
        self.ddCorsi = ft.Dropdown(
            label="corso",
            width=600,
            hint_text="Selezionare un corso",
            options=[],
            autofocus=True,
            on_change=self._controller.leggiCorsi
        )

        self._controller.populateDDCorsi()

        self.btnCercaIscritti = ft.ElevatedButton(text="Cerca iscritti",
                                                   on_click=self._controller.handleCercaIscritti,
                                                   tooltip="cerca gli iscritti al corso selezionato") ##!!!

        row1 = ft.Row([self.ddCorsi, self.btnCercaIscritti],
                      alignment=ft.MainAxisAlignment.CENTER)

        self._page.controls.append(row1)

        #ROW2
        self.txtInMatricola = ft.TextField(label="matricola",
                                            width=200,
                                            hint_text="Inserire matricola"
                                            )
        self.txtInNome = ft.TextField(label="nome",
                                       width=200,
                                       read_only=True
                                       )
        self.txtInCognome = ft.TextField(label="cognome",
                                          width=200,
                                          read_only=True
                                          )

        row2 = ft.Row([self.txtInMatricola, self.txtInNome, self.txtInCognome],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        #ROW3

        self.btnCercaStudente = ft.ElevatedButton(text="Cerca Studente",
                                                   on_click=self._controller.handleCercaStudente)
        self.btnCercaCorsi = ft.ElevatedButton(text="Cerca Corsi",
                                                on_click=self._controller.handleCercaCorsi)
        self.btnIscrivi = ft.ElevatedButton(text="Iscrivi",
                                             on_click=self._controller.handleIscrivi)

        row3 = ft.Row([self.btnCercaStudente, self.btnCercaCorsi, self.btnIscrivi],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)

        self._page.update()

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
