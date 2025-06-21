import flet as ft
from connection.credentials import real_password, real_username
import connection.session as session


def login_init(fv):
    """Initialise the login view. Also builds the appbar for all the views.

    Args:
        fv (FleetingViews): The FleetingViews manager
    """

    #region AppBar
    """Creates the appbar that will be used in all views/pages.
    """

    appbar = ft.AppBar(
        title=ft.Text("FleetingViews"),
        leading=ft.IconButton(icon=ft.Icons.ARROW_BACK_ROUNDED, on_click=lambda _: fv.go_back()),
        actions=[
            ft.IconButton(icon=ft.Icons.HOME, on_click=lambda _: fv.view_go("home")),  # can pass query parameters in the view_go calls (e.g: "home?id=23")
            ft.IconButton(icon=ft.Icons.SETTINGS, on_click=lambda _: fv.view_go("settings")),  # FleetingViews has built-in transitions (e.g: , duration=200, mode="bottom_left")
            ft.IconButton(icon=ft.Icons.ERROR_ROUNDED, on_click=lambda _: fv.view_go("asdfasdf")),  # Prompt non-existing view, to see the error handling
            ft.IconButton(icon=ft.Icons.LOGOUT, on_click=lambda _: logout())  # Logout button
        ]
    )

    #endregion AppBar

    #region Alert (snackbar)

    alert = ft.SnackBar(
        content=ft.Text("Invalid username or password. Please try again."),
        duration=5000,
    )

    def home_on_mount(ctx):
        """Displays an appropriate welcome message in the alert when any view/page is mounted.
        """
        alert.content = ft.Text(f"Welcome to {ctx.actual_view.route}")
        alert.action = ""
        open_alert()

    def open_alert():
        fv.page.open(alert)

    #endregion Alert (snackbar)

    #region Authentication

    def successful_login_appbar():
        """Called on successful login
        """
        fv.view_go("home")
        fv.clear()
        for view_name in fv.views:
            if view_name != "login":
                fv.update_view(view_name, "appbar", appbar)
                if view_name == "home" or view_name == "settings":
                    fv.add_hooks_or_guards(view_name, {"on_mount": home_on_mount})

    def logout():
        """Called when the user clicks the logout button in the appbar.
        """
        session.logged_in = False
        alert.content = ft.Text("Please log in to continue.")
        alert.action = ""
        open_alert()
        fv.view_go("login")

    def login(e):
        nonlocal fv
        username = user_input.value.strip()
        password = password_input.value

        if username == real_username and password == real_password:
            session.logged_in = True
            successful_login_appbar()
        else:
            open_alert()

    #endregion Authentication

    #region Login UI

    #region Controls

    # Header label for the login view (Added first into main_login_column)
    login_header_label = ft.Container(content=ft.Text("Login",
                                      size=30
                                      ))

    # Label for the username input field (Added into main_login_column, just above user_input.)
    user_text_container = ft.Container(
        ft.Text("Username", size=20, weight=ft.FontWeight.BOLD
                ),
        alignment=ft.alignment.center_left,
        width=500
    )

    # Username input field (Added into main_login_column)
    user_input = ft.TextField(
        value="",
        multiline=False,
        label="Username",
        width=500,
        suffix_icon=ft.Icon(ft.Icons.PERSON_2_ROUNDED)
    )

    # Label for the password input field (Added into main_login_column, just above password_input.)
    password_text_container = ft.Container(
        ft.Text("Password",
                size=20,
                weight=ft.FontWeight.BOLD
                ),
        alignment=ft.alignment.center_left,
        width=500
    )

    # Password input field with reveal option (Added into main_login_column)
    password_input = ft.TextField(value="",
                                  multiline=False,
                                  label="Password",
                                  password=True,
                                  can_reveal_password=True,
                                  width=500,
                                  on_submit=login
                                  )

    # Button to login (Added at the end into main_login_column)
    login_button = ft.ElevatedButton(
        icon=ft.Icons.LOGIN_ROUNDED,
        text="Login",
        width=200,
        on_click=login
    )

    #endregion Controls

    #region Containers

    # Main (and only) column of the login view. (Added into entire_page_login_container)
    main_login_column = ft.Column(
        [
            login_header_label,
            user_text_container,
            user_input,
            password_text_container,
            password_input,
            login_button
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        height=350,
        alignment=ft.MainAxisAlignment.CENTER
    )

    # Entire login view container:
    entire_page_login_container = ft.Container(
        content=main_login_column,
        padding=ft.padding.all(20),
        border_radius=ft.border_radius.all(25),
        blur=ft.Blur(1000, 10, ft.BlurTileMode.DECAL)
    )

    # add to the FleetingViews manager
    fv.append("login", [entire_page_login_container])
    #endregion Containers

    #endregion Login UI

    # Return the UI's controls, in case main.py also wants some access to them.
    return main_login_column