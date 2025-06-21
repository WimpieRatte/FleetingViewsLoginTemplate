import flet as ft
from connection.credentials import real_password, real_username
import connection.session as session
from colors import BLUE_COLOR, PINK_COLOR, WHITE_COLOR, BLACK_COLOR


def login_init(fv):
    """Initialise the login view.

    Args:
        fv (_type_): The FleetingViews manager
    """

    appbar = ft.AppBar(
        title=ft.Text("FleetingViews"),
        leading=ft.IconButton(icon=ft.Icons.ARROW_BACK_ROUNDED, on_click=lambda _: fv.go_back()),
        actions=[
            ft.IconButton(icon=ft.Icons.HOME, on_click=lambda _: fv.view_go("home")),  # can pass query parameters in the view_go calls (e.g: "home?id=23")
            ft.IconButton(icon=ft.Icons.SETTINGS, on_click=lambda _: fv.view_go("settings", duration=200, mode="bottom_left")),  # FleetingViews has built-in transitions
            ft.IconButton(icon=ft.Icons.ERROR_ROUNDED, on_click=lambda _: fv.view_go("asdfasdf", duration=200, mode="bottom_right"))  # Prompt non-existing view, to see the error handling
        ]
    )

    alert = ft.SnackBar(
        content=ft.Text("Invalid username or password", color=BLACK_COLOR),
        action="OK",
        duration=5000,
        open=False,
        bgcolor=WHITE_COLOR,
        on_action=lambda _: fv.page.close(alert),  # FleetingViews has your page as property
    )

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

    def home_on_mount(ctx):
        alert.content = ft.Text(f"Welcome to {ctx.actual_view.route}")
        ctx.page.open(alert)  # Show the alert when the view is mounted

    def login(e):
        nonlocal fv
        username = user_input.value.strip()
        password = password_input.value

        if username == real_username and password == real_password:
            session.logged_in = True
            successful_login_appbar()
        else:
            fv.page.open(alert)  # Show the alert if login fails

    #region UI

    login_button = ft.ElevatedButton(
        icon=ft.Icons.LOGIN_ROUNDED,
        text="Login",
        width=200,
        style=ft.ButtonStyle(color=BLACK_COLOR, bgcolor=({ft.ControlState.HOVERED: BLUE_COLOR, ft.ControlState.DEFAULT: PINK_COLOR})),
        icon_color=BLACK_COLOR,
        on_click=login
    )

    login_container = ft.Container(content=ft.Text("Login",
                                                   size=30,
                                                   color=BLUE_COLOR))

    user_text_container = ft.Container(
        ft.Text("Username", size=20, weight=ft.FontWeight.BOLD
                ),
        alignment=ft.alignment.center_left,
        width=500
    )

    user_input = ft.TextField(
        value="",
        multiline=False,
        label="Username",
        color=WHITE_COLOR,
        width=500,
        suffix_icon=ft.Icon(ft.Icons.PERSON_2_ROUNDED, color=WHITE_COLOR),
        label_style=ft.TextStyle(color=WHITE_COLOR),
        border_color=WHITE_COLOR,
        focused_border_color=BLUE_COLOR,
        cursor_color=WHITE_COLOR
    )

    password_text_container = ft.Container(
        ft.Text("Password",
                size=20,
                weight=ft.FontWeight.BOLD,
                color=BLUE_COLOR
                ),
        alignment=ft.alignment.center_left,
        width=500
    )

    password_input = ft.TextField(
        value="",
        multiline=False,
        label="Password",
        color=WHITE_COLOR,
        width=500,
        label_style=ft.TextStyle(color=WHITE_COLOR),
        border_color=WHITE_COLOR,
        focused_border_color=BLUE_COLOR,
        cursor_color=WHITE_COLOR,
        password=True,
        can_reveal_password=True
    )

    login_column = ft.Column(
        controls=[
            login_container,
            user_text_container,
            user_input,
            password_text_container,
            password_input,
            login_button],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        height=350,
        alignment=ft.MainAxisAlignment.CENTER
    )

    login_container = ft.Container(
        content=login_column,
        bgcolor=PINK_COLOR,
        padding=ft.padding.all(20),
        border_radius=ft.border_radius.all(25),
        blur=ft.Blur(1000, 10, ft.BlurTileMode.DECAL)
    )

    # add to the FleetingViews manager
    fv.append("login", [login_container])

    #endregion

    # Return the UI's memory access in the case that main.py might need it
    return login_column