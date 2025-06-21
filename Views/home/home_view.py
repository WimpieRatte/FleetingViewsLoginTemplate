import flet as ft
from colors import BLUE_COLOR, PINK_COLOR, WHITE_COLOR, BLACK_COLOR

def home_init(fv):

    home_snack_bar = ft.SnackBar(
        content=ft.Text("", color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD),
        action="Accept!",
        duration=4000,
        bgcolor=WHITE_COLOR,
        action_color=BLACK_COLOR
    )

    def get_params(e):
        home_snack_bar.content.value = fv.get_params()
        fv.page.open(home_snack_bar)

    home_button = ft.TextButton(
        icon=ft.Icons.DATA_ARRAY,
        text="Get home data!",
        on_click=get_params,
        style=ft.ButtonStyle(color=WHITE_COLOR)
    )

    home_container = ft.Container(content=ft.Text("This is the home page", size=40))
    fv.append("home", [home_container, home_button])