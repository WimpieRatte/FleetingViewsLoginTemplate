import flet as ft
from colors import BLUE_COLOR, PINK_COLOR, WHITE_COLOR, BLACK_COLOR

def settings_init(fv):
    """Settings is going to have an unmount hook that adds a container every time it's called.

    Args:
        fv (_type_): _description_
    """
    n_container = 1

    settings_snack_bar = ft.SnackBar(
        content=ft.Text("", color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD),
        action="Accept!",
        duration=4000,
        bgcolor=WHITE_COLOR,
        action_color=BLACK_COLOR
    )

    def get_params(e):
        """Get app's state using ctx parameter

        Args:
            e (_type_): _description_
        """
        settings_snack_bar.content.value = fv.get_params()
        fv.page.open(settings_snack_bar)

    def my_unmount_hook(ctx):
        nonlocal n_container
        new_container = ft.Container(content=ft.Text(f"New container N = {n_container}"))
        n_container += 1
        fv.append("settings", new_container)

    # Add custom dismount hook during runtime
    fv.add_hooks_or_guards("settings", {"on_dismount": my_unmount_hook})

    settings_button = ft.TextButton(
        icon=ft.Icons.DATA_ARRAY,
        text="Get settings data!",
        on_click=get_params,
        style=ft.ButtonStyle(color=WHITE_COLOR)
    )

    settings_container = ft.Container(content=ft.Text("This is the settings page", size=40))
    fv.append("settings", [settings_container, settings_button])