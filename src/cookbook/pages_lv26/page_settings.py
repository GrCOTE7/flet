import flet as ft

from .template import build_lv26_view


def build_settings_view(open_mail_setting) -> ft.View:
    return build_lv26_view(
        route="/settings",
        appbar_title="Settings",
        body_controls=[
            ft.Text(
                "Settings!",
                theme_style=ft.TextThemeStyle.BODY_MEDIUM,
            ),
            ft.Button(
                content="Go to mail settings",
                on_click=open_mail_setting,
            ),
        ],
    )
