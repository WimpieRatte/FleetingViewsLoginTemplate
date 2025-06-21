import flet as ft

def home_init(fv):

    #region Alert (snackbar) & params

    home_snack_bar = ft.SnackBar(
        content=ft.Text("", weight=ft.FontWeight.BOLD),
        action="Accept!",
        duration=4000,
    )


    def get_params(e):
        home_snack_bar.content.value = fv.get_params()
        fv.page.open(home_snack_bar)

    #endregion Alert (snackbar) & params

    #region Controls

    home_button = ft.TextButton(
        icon=ft.Icons.DATA_ARRAY,
        text="Get home data!",
        on_click=get_params,
    )

    #endregion Controls

    #region Containers

    home_container = ft.Container(content=ft.Text("This is the home page", size=40))
    fv.append("home", [home_container, home_button])

    #endregion Containers