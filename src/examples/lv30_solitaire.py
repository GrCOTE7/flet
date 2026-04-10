import flet as ft
from pathlib import Path


def main(page: ft.Page):
    # card = ft.GestureDetector(
    #     left=0,
    #     top=0,
    #     content=ft.Container(bgcolor=ft.Colors.GREEN, width=100, height=100),
    # )

    # page.add(ft.Stack(controls=[card], width=1000, height=500))

    path = Path(__file__).parent / "imgs" / "chanteur.jpg"
    print(path)

    img = ft.Stack(
        width=300,
        height=300,
        controls=[
            ft.Image(
                src=str(path),
                width=300,
                height=300,
                fit=ft.BoxFit.CONTAIN,
            ),
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Text(
                        value="Image title",
                        color=ft.Colors.SURFACE_TINT,
                        size=40,
                        weight=ft.FontWeight.BOLD,
                        opacity=0.5,
                    )
                ],
            ),
        ],
    )

    page.add(img)


if __name__ == "__main__":
    ft.run(main)
