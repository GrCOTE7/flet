import flet as ft


class Lv99(ft.Container):
    def __init__(self):
        super().__init__()

        self.padding = ft.Padding.symmetric(vertical=3, horizontal=10)
        self.border_radius = 7
        self.bgcolor = ft.Colors.LIGHT_GREEN_ACCENT_400
        self.content = ft.Text(
            "Ready.",
            color=ft.Colors.BLACK_87,
            # color=ft.Colors.WHITE,
            size=18,
            weight=ft.FontWeight.BOLD,
            italic=True,
            font_family="Arial",
        )


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
        ink = ft.TextStyle(color=ft.Colors.BLACK_87, size=24)
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
                        content=ft.Text("1", style=ink),
                    ),
                    ft.Container(
                        expand=3,
                        height=60,
                        bgcolor=ft.Colors.AMBER_300,
                        alignment=ft.Alignment.CENTER,
                        border_radius=8,
                        content=ft.Text("3", style=ink),
                    ),
                    ft.Container(
                        expand=1,
                        height=60,
                        bgcolor=ft.Colors.PINK_200,
                        alignment=ft.Alignment.CENTER,
                        border_radius=8,
                        content=ft.Text("1", style=ink),
                    ),
                ],
            ),
        )


class State:
    counter = 0


class Lv03(ft.SafeArea):

    def __init__(self):
        self.state = State()
        self.message = ft.Text("0", size=32, color=ft.Colors.BLACK_87)
        bloc = ft.Container(
            width=200,
            height=100,
            bgcolor=ft.Colors.CYAN_200,
            border_radius=8,
            content=ft.Stack(
                controls=[
                    ft.Container(
                        expand=True,
                        alignment=ft.Alignment.CENTER,
                        content=self.message,
                    ),
                    ft.Container(
                        right=12,
                        bottom=12,
                        content=ft.FloatingActionButton(
                            icon=ft.Icons.ADD,
                            mini=True,
                            on_click=self.handle_button_click,
                        ),
                    ),
                ]
            ),
        )

        super().__init__(
            expand=True,
            content=ft.Container(
                alignment=ft.Alignment.CENTER,
                content=bloc,
            ),
        )

    def handle_button_click(self, e: ft.Event[ft.FloatingActionButton]):
        self.state.counter += 1
        self.message.value = str(self.state.counter)
        self.message.update()


class Lv04(ft.Container):
    def __init__(self):
        super().__init__()

        my_stack = ft.Stack(
            controls=[
                ft.Container(
                    width=200,
                    height=200,
                    left=100,
                    top=20,
                    bgcolor=ft.Colors.BLUE,
                ),
                ft.Container(
                    width=100,
                    height=100,
                    bgcolor=ft.Colors.RED,
                    top=50,
                    left=50,
                ),
                ft.Container(
                    width=50,
                    height=50,
                    bgcolor=ft.Colors.with_opacity(0.7, ft.Colors.YELLOW),
                    top=120,
                    left=120,
                ),
            ],
        )
        self.width = 300
        self.height = 240
        self.bgcolor = ft.Colors.GREEN_400
        self.padding = 12
        self.border_radius = 8
        self.content = my_stack


class Lv05(ft.Container):
    def __init__(self, radius: int = 7):
        super().__init__()

        self.padding = ft.Padding.symmetric(vertical=3, horizontal=10)
        self.border_radius = radius
        self.bgcolor = ft.Colors.LIGHT_GREEN_ACCENT_400
        self.content = ft.Text(
            "Ready. "+str(radius),
            color=ft.Colors.BLACK_87,
            # color=ft.Colors.WHITE,
            size=18,
            weight=ft.FontWeight.BOLD,
            italic=True,
            font_family="Arial",
        )
