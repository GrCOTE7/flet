import flet as ft
from pathlib import Path


def main(page: ft.Page):
    card1 = ft.GestureDetector(
        left=0,
        top=0,
        content=ft.Container(bgcolor=ft.Colors.GREEN, width=70, height=100),
        on_tap=lambda e: print("tap"),
    )
    card2 = ft.GestureDetector(
        left=0,
        top=0,
        content=ft.Container(bgcolor=ft.Colors.RED, width=70, height=100),
        on_tap=lambda e: print("tap"),
    )

    page.add(ft.Stack(controls=[card1, card2], width=1000, height=500))


if __name__ == "__main__":
    ft.run(main)
