import flet as ft

from app.config import APP_TITLE
from ui.pages.home_page import HomePage
from ui.pages.settings_page import SettingsPage


def main(page: ft.Page):
    page.title = APP_TITLE

    # Pages
    home = HomePage(page)
    settings = SettingsPage(page)

    # A container for the current "screen"
    content = ft.Container(expand=True, content=home)

    # Handle navigation changes
    def on_nav_change(e):
        if e.control.selected_index == 0:
            content.content = home
            page.floating_action_button = home.fab
        elif e.control.selected_index == 1:
            content.content = settings
            page.floating_action_button = None
        content.update()
        page.update()

    # Global navigation bar
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.Icons.NOTE_OUTLINED,
                selected_icon=ft.Icons.NOTE,
                label="Notes",
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.SETTINGS_OUTLINED,
                selected_icon=ft.Icons.SETTINGS,
                label="Settings",
            ),
        ],
        on_change=on_nav_change,
    )

    page.add(content)


if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.FLET_APP)
