import flet as ft
from pathlib import Path


def main(page: ft.Page):
    # card = ft.GestureDetector(
    #     left=0,
    #     top=0,
    #     content=ft.Container(bgcolor=ft.Colors.GREEN, width=100, height=100),
    # )

    # page.add(ft.Stack(controls=[card], width=1000, height=500))

    path_lc = str(Path(__file__).parent / "imgs" / "chanteur.jpg")
    print(path_lc)

    def getImg(path, title='Image Title'):

       return ft.Stack(
            width=300,
            height=300,
            controls=[
                ft.Image(
                    src=str(path),
                    # src="https://picsum.photos/300/300",
                    width=300,
                    height=300,
                    fit=ft.BoxFit.CONTAIN,
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            value=title,
                            color=ft.Colors.SURFACE_TINT,
                            size=40,
                            weight=ft.FontWeight.BOLD,
                            opacity=0.5,
                        )
                    ],
                ),
            ],
        )

    page.add(getImg(path_lc, 'Lionel chanteur'))
    page.add(getImg('https://picsum.photos/300/300', "Random image"))

    page.add(
        ft.SafeArea(
            content=ft.Stack(
                width=40,
                height=40,
                controls=[
                    ft.CircleAvatar(
                        foreground_image_src="https://avatars.githubusercontent.com/u/5041459?s=88&v=4"
                    ),
                    ft.Container(
                        alignment=ft.Alignment.BOTTOM_LEFT,
                        content=ft.CircleAvatar(bgcolor=ft.Colors.GREEN, radius=5),
                    ),
                ],
            ),
        )
    )


if __name__ == "__main__":
    ft.run(main)
