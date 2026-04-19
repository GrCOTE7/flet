import flet as ft

from .template import build_lv26_view


def build_root_view(open_setting) -> ft.View:
    return build_lv26_view(
        route="/",
        appbar_title="Flet App",
        body_controls=[
            ft.Button("Go to Settings", on_click=open_setting),
        ],
    )
