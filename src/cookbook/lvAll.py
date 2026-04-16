import flet as ft
import os, sys
from pathlib import Path


class Lv99(ft.Container):
    def __init__(self):
        super().__init__()

        self.padding = ft.Padding.symmetric(vertical=3, horizontal=10)
        self.border_radius = 7
        self.bgcolor = ft.Colors.LIGHT_GREEN_ACCENT_400
        self.content = ft.Text(
            "Ready.",
            color=ft.Colors.BLACK_87,
            size=18,
            weight=ft.FontWeight.BOLD,
            italic=True,
            font_family="Arial",
        )


class Lv00(ft.Column):

    def __init__(self, t1: str | None = None):
        t_ready = ft.Text("Ready.")
        t1_text = self.txt(t1)

        controls: list[ft.Control] = [t_ready]
        if t1_text:
            print(t1_text.value)
            controls.insert(0, t1_text)

        super().__init__(controls=controls)

    def txt(self, t1: str | None = None):
        if t1:
            return ft.Text(t1)
        return None


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

    def __init__(self):
        content = self.mySerie()
        super().__init__(content=content)

    def myCard(self, myLabel: str = ""):
        return ft.Card(
            shape=ft.ContinuousRectangleBorder(radius=10),
            content=ft.Container(
                padding=ft.Padding.symmetric(horizontal=7, vertical=-3),
                border_radius=ft.BorderRadius.all(4),
                bgcolor=ft.Colors.AMBER_100,
                content=ft.Text(myLabel, color=ft.Colors.BLACK, size=24),
            ),
        )

    def mySerie(self):
        return ft.Row(  # Try Column / Row
            expand=True,
            height=100,
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            controls=[self.myCard(str(i)) for i in range(1, 6)],
        )


class Lv06(ft.Container):

    def __init__(self):
        content = self.myResponsiveRow()
        super().__init__(content=content)

    def myCard(self, myLabel: str = ""):
        return ft.Card(
            shape=ft.ContinuousRectangleBorder(radius=10),
            content=ft.Container(
                padding=ft.Padding.symmetric(horizontal=7, vertical=-3),
                border_radius=ft.BorderRadius.all(4),
                bgcolor=ft.Colors.AMBER_100,
                content=ft.Text(myLabel, color=ft.Colors.BLACK, size=24),
            ),
        )

    def myResponsiveRow(self):
        return ft.ResponsiveRow(
            controls=[
                ft.Button(
                    f"Button {i}",
                    color=ft.Colors.BLUE_GREY_300,
                    col={
                        ft.ResponsiveRowBreakpoint.XS: 12,
                        ft.ResponsiveRowBreakpoint.MD: 6,
                        ft.ResponsiveRowBreakpoint.LG: 3,
                    },
                )
                for i in range(1, 6)
            ],
        )


class Lv07(ft.Container):

    def __init__(self):
        self.btn = self.myShadowedBtn()
        super().__init__(content=self.btn)

    def btnAction(self, e: ft.Event[ft.Button]):

        msg = f"Button {e.control.data} clicked!"
        e.control.content = msg
        e.control.update()
        print(msg)

    def longPress(self):
        print("Long Press!")

    def myBtn(self):
        label = "Lesson Lv07"
        return ft.Button(
            content=label,
            data="btn_" + label,
            on_click=self.btnAction,
            icon=ft.Icons.PARK_ROUNDED,
            icon_color=ft.Colors.GREEN_400,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=4),
                color={
                    ft.ControlState.HOVERED: ft.Colors.RED_700,
                    ft.ControlState.FOCUSED: ft.Colors.BLUE,
                    ft.ControlState.DEFAULT: ft.Colors.RED_300,
                },
                bgcolor={
                    ft.ControlState.FOCUSED: ft.Colors.PINK_200,
                    ft.ControlState.DEFAULT: ft.Colors.YELLOW_ACCENT_200,
                },
                mouse_cursor=ft.MouseCursor.CLICK,
                # elevation={
                #     ft.ControlState.DEFAULT: 0,
                #     ft.ControlState.HOVERED: 5,
                #     ft.ControlState.PRESSED: 10,
                # },
                # animation_duration=500,
            ),
            on_long_press=self.longPress,
        )

    def myShadowedBtn(self):
        return ft.Container(
            content=self.myBtn(),
            # border_radius=ft.BorderRadius.all(50),
            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
            shadow=ft.BoxShadow(
                color=ft.Colors.RED_400,
                blur_radius=10,
                offset=ft.Offset(5, 5),
            ),
        )


class Lv08(ft.Container):

    def __init__(self):
        super().__init__(
            content=self.myLv08(),
            # alignment=ft.Alignment.CENTER,
            # alignment=ft.Alignment(0, -1),
            # alignment=ft.Alignment(0, 1),
            alignment=ft.Alignment(1, 1),
            bgcolor=ft.Colors.RED,
            width=392,
            height=984,  # 984
            padding=ft.Padding.symmetric(horizontal=8, vertical=13),
        )

    def myLv08(self):

        return ft.Container(
            width=216,  # largeur du fond jaune
            height=54,
            padding=ft.Padding.symmetric(horizontal=20, vertical=8),
            alignment=ft.Alignment.CENTER,
            bgcolor=ft.Colors.YELLOW,
            border_radius=7,
            border=ft.Border.all(2, ft.Colors.BLACK_38),
            content=ft.Text(
                "#08",
                text_align=ft.TextAlign.CENTER,
                color=ft.Colors.BLACK,
                size=24,
            ),
        )


class Lv09(ft.Container):

    def __init__(self, page):
        super().__init__(
            content=self.myLv09(),
        )

        page.fonts = {
            "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
            "Open Sans": "/fonts/OpenSans-Regular.ttf",
            "Roboto Condensed": "https://raw.githubusercontent.com/google/fonts/main/apache/robotocondensed/RobotoCondensed-Regular.ttf",
        }
        print(page.fonts)

    def myLv09(self):

        doc = ft.Column()

        z = ft.Row()  # z → zône

        z.controls.append(ft.Image(src="icon.png", width=50, height=50))

        z.controls.append(
            ft.Column(
                controls=[
                    ft.Text(
                        "Premier texte de la leçon #09\n",
                        text_align=ft.TextAlign.CENTER,
                        color=ft.Colors.AMBER,
                        size=20,
                    ),
                    ft.Text(
                        "2ème texte de la leçon #09",
                        text_align=ft.TextAlign.CENTER,
                        color=ft.Colors.AMBER,
                        size=20,
                        font_family="Consolas",
                    ),
                ],
                spacing=-30,
            )
        )
        doc.controls.append(z)

        doc.controls.append(ft.Divider(color=ft.Colors.RED_ACCENT_400))

        doc.controls.append(
            ft.Text("Kanit", font_family="Kanit", size=20, color=ft.Colors.CYAN_700)
        )
        doc.controls.append(
            ft.Text(
                "Open Sans", font_family="Open Sans", size=20, color=ft.Colors.CYAN_700
            )
        )
        doc.controls.append(
            ft.Text(
                "Arial Gras",
                weight=ft.FontWeight.BOLD,
                font_family="Arial",
                size=20,
                color=ft.Colors.CYAN_700,
            )
        )
        doc.controls.append(
            ft.Text("Arial", font_family="Arial", size=20, color=ft.Colors.CYAN_700)
        )
        doc.controls.append(ft.Divider(color=ft.Colors.WHITE24))
        doc.controls.append(
            ft.Text(
                "Exemples largeur / stretch",
                size=16,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.ORANGE_300,
            )
        )
        doc.controls.append(
            ft.Text(
                "Roboto Condensed = vraie fonte plus etroite",
                font_family="Roboto Condensed",
                size=20,
                color=ft.Colors.LIGHT_GREEN_300,
            )
        )
        doc.controls.append(
            ft.Text(
                "Arial avec letter_spacing negatif (simulation compacte)",
                size=20,
                color=ft.Colors.CYAN_700,
                style=ft.TextStyle(font_family="Arial", letter_spacing=-1.5),
            )
        )
        doc.controls.append(
            ft.Text(
                "Arial avec letter_spacing positif (simulation elargie)",
                size=20,
                color=ft.Colors.CYAN_700,
                style=ft.TextStyle(font_family="Arial", letter_spacing=3),
            )
        )
        doc.controls.append(
            ft.Text(
                "Le letter_spacing change l'espacement, pas la largeur reelle des glyphes.",
                size=14,
                color=ft.Colors.GREY_400,
                italic=True,
            )
        )

        return doc


def _read_env_value(key: str, fallback: str = "No defined") -> str:
    """Récupère la valeur d'une clé dans les variables d'environnement ou dans un fichier .env
    (En cherchant cette key d'abord dans src/.env, puis dans le .env à la racine du projet).
    Args:
        key (str): La clé à rechercher.
        fallback (str, optional): Valeur par défaut si la clé n'est pas trouvée. Defaults to "Not defined".

    Returns:
        str: La valeur de la clé ou la valeur par défaut si la clé n'est pas trouvée.
    """
    value = os.environ.get(key)
    if value is not None:
        return value

    env_candidates = [
        Path(__file__).resolve().parents[1] / ".env",
        Path(__file__).resolve().parents[2] / ".env",
    ]

    for env_path in env_candidates:
        if not env_path.is_file():
            continue

        for raw_line in env_path.read_text(encoding="utf-8").splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue

            env_key, env_value = line.split("=", 1)
            if env_key.strip() == key:
                return env_value.strip().strip("\"'")

    return fallback


class Lv10(ft.Container):

    def __init__(self):
        super().__init__(
            content=self.myLv09(), width=392, height=1088, bgcolor="#070021"
        )

    def myLv09(self):

        return ft.Text(
            self.ct(), text_align=ft.TextAlign.CENTER, color=ft.Colors.AMBER, size=14
        )

    def ct(self):

        default_env = os.environ.get(
            "FLET_ASSETS_DIR", "No defined"
        )  # → D:\flet_doc\src\assets

        custom_env = _read_env_value("MY_KEY")  # → MY_VALUE_SRC depuis src/.env

        txt = f"oki {default_env} - {custom_env}"
        print(txt)

        return txt


class Lv11(ft.Container):

    def __init__(self):
        super().__init__(
            content=self.myLv09(), width=392, height=1088, bgcolor="#070021"
        )

    def myLv09(self):

        return ft.Text(
            self.ct(), text_align=ft.TextAlign.CENTER, color=ft.Colors.AMBER, size=14
        )

    def ct(self):

        txt = "Ready."

        return txt
