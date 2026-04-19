import flet as ft

from .template import build_lv26_view


def build_mail_settings_view() -> ft.View:
    return build_lv26_view(
        route="/settings/mail",
        appbar_title="Mail Settings",
        body_controls=[ft.Text("Mail settings!")],
    )
