import flet as ft
import FleetingViews
from Views.login.login_view import login_init
import Views.settings.settings_view as settings_view
import Views.home.home_view as home_view
import connection.session as session
from colors import BLUE_COLOR, PINK_COLOR

def main(page: ft.Page):
    page.padding = ft.padding.all(0)
    page.fonts = {"Oblata": "assets/fonts/OblataDisplayRegular-Zp8o8.otf"}
    page.theme = ft.Theme(font_family="Oblata")

    #region Create the guards
    def logged_in(ctx, name):
        return session.logged_in
    def logged_in_login_guard(ctx, name):
        return not session.logged_in
    #endregion

    #region Create the views
    view_definitions = {
        "home": {
            "bgcolor": BLUE_COLOR,
            "vertical_alignment": ft.MainAxisAlignment.CENTER,
            "horizontal_alignment": ft.CrossAxisAlignment.CENTER,
            "guards": logged_in,
        },
        "login": {
            "vertical_alignment": ft.MainAxisAlignment.CENTER,
            "horizontal_alignment": ft.CrossAxisAlignment.CENTER,
            "guards": logged_in_login_guard,
        },
        "settings": {
            "bgcolor": PINK_COLOR,
            "vertical_alignment": ft.MainAxisAlignment.CENTER,
            "horizontal_alignment": ft.CrossAxisAlignment.CENTER,
            "guards": logged_in,
        },
    }

    # Instantiate FleetingViews Manager:
    fv = FleetingViews.create_views(view_definitions=view_definitions, page=page)
    #endregion

    login_init(fv)  # Initialize the login view
    settings_view.settings_init(fv)  # Initialize the settings view
    home_view.home_init(fv)  # Initialize the home view
    fv.view_go("login")  # Start with the login view


ft.app(target=main)
