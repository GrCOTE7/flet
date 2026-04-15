import flet as ft
from tools.screen_utils import gc7_rules as gc7

from .lvAll import *


def main(page: ft.Page):

    title = "Cookbook"
    gc7(page)
    page.title = title.replace("-", "|")
    page.scroll = ft.ScrollMode.AUTO
    page.add(ft.Text(title, size=18, weight=ft.FontWeight.BOLD))
    page.spacing = 20
    # page.bgcolor = ft.Colors.GREEN_900

    lvs = []

    lvs.append(Lv00("Salut !"))  # Simple class with a custom text
    lvs.append(Lv01())  # Form with a text field and a button
    lvs.append(Lv02())  # 3 blocs in a row with different expand values and colors
    lvs.append(Lv03())  # A counter
    lvs.append(Lv04())  # 3 blocs in a stack with different expand values and colors
    lvs.append(Lv05())  #
    # page.add(*lvs)
    page.add(lvs[-1])

    # lvs.append(Lv99())  # 3 blocs in a stack with different expand values and colors
    # page.add(lvs[-1])


if __name__ == "__main__":
    ft.run(main)
