import flet as ft


class HomePage(ft.Column):
    def __init__(self, page: ft.Page):
        super().__init__(expand=True)
        self.page = page

        # --- Basic FAB only ---
        self.fab = ft.FloatingActionButton(
            icon=ft.Icons.ADD,
            tooltip="Create",
            bgcolor=ft.Colors.BLUE,
            on_click=self._fab_pressed,
        )

        # Register FAB globally so it stays bottom-right
        page.floating_action_button = self.fab

    def _fab_pressed(self, e):
        if self.page:
            self.page.open(ft.SnackBar(ft.Text("FAB pressed!")))
