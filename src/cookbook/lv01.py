import flet as ft


class Lv00(ft.Container):

    def __init__(self, txt: str = "Oki"):
        super().__init__()

        self.txt = txt
        print(txt)

        self.content = ft.Column([ft.Text(self.txt), ft.Text("Ok")])


class Lv01(ft.Container):

    def __init__(self):
        super().__init__()

        self.padding = 10
        self.border = ft.Border.all(2, ft.Colors.BLUE_GREY_200)
        self.border_radius = 10
        self.content = ft.Row(
            controls=[
                ft.TextField(hint_text="Enter your name", expand=True),
                ft.Button("Join chat"),
            ]
        )


class Lv02(ft.SafeArea):

    def __init__(self):
        content = self.threeBlocs()
        super().__init__(content=content)

    def threeBlocs(self):
        return ft.Container(
            width=500,
            padding=10,
            border=ft.Border.all(2, ft.Colors.BLUE_GREY_200),
            border_radius=10,
            content=ft.Row(
                spacing=8,
                controls=[
                    ft.Container(
                        expand=1,
                        height=60,
                        bgcolor=ft.Colors.CYAN_300,
                        alignment=ft.Alignment.CENTER,
                        border_radius=8,
                        content=ft.Text("1"),
                    ),
                    ft.Container(
                        expand=3,
                        height=60,
                        bgcolor=ft.Colors.AMBER_300,
                        alignment=ft.Alignment.CENTER,
                        border_radius=8,
                        content=ft.Text("3"),
                    ),
                    ft.Container(
                        expand=1,
                        height=60,
                        bgcolor=ft.Colors.PINK_200,
                        alignment=ft.Alignment.CENTER,
                        border_radius=8,
                        content=ft.Text("1"),
                    ),
                ],
            ),
        )
