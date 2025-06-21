import flet as ft
import FleetingViews
from Views.login.login_view import login_init
import Views.settings.settings_view as settings_view
import Views.home.home_view as home_view
import connection.session as session

title = "FleetingViews Example"

def main(page: ft.Page):
    #region Page configuration
    page.padding = ft.padding.all(0)
    page.fonts = {"Arial": "assets/fonts/ARIAL.TTF"}
    page.title = title
    page.theme = ft.Theme(
        font_family="Arial",
        color_scheme_seed=ft.Colors.INDIGO
    )
    page.theme_mode = ft.ThemeMode.LIGHT
    #endregion Page configuration

    #region Create the guards
    def logged_in(ctx, name):
        return session.logged_in
    def logged_in_login_guard(ctx, name):
        return not session.logged_in
    #endregion

    #region Create the views
    view_definitions = {
        "home": {
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
            "vertical_alignment": ft.MainAxisAlignment.CENTER,
            "horizontal_alignment": ft.CrossAxisAlignment.CENTER,
            "guards": logged_in,
        },
    }

    # Instantiate FleetingViews Manager:
    fv = FleetingViews.create_views(view_definitions=view_definitions, page=page)
    #endregion

    #region Initialise the views and go to login
    login_init(fv)  # Initialize the login view
    settings_view.settings_init(fv)  # Initialize the settings view
    home_view.home_init(fv)  # Initialize the home view
    fv.view_go("login")  # Start with the login view
    #endregion Initialise the views and go to login

ft.app(target=main)
