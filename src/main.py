from re import A

import flet as ft
import datetime, time
import asyncio
from tools.screen_utils import gc7_rules as gc7


async def main(page: ft.Page, width: int = 392):
    # gc7(page, width=width)
    # gc7(page, mode="LIGHT", width=width)

    # from examples.lv00_matrice import main as go
    # go(page)

    # from basis.scroll_example import main as scroll
    # scroll(page)

    # from basis.lv01_essai import essai as essai
    # essai(page)

    # # from examples.lv04_calc_ui import calc as calc
    # from examples.lv05_calc_ui_reusable import calc as calc
    # calc(page)

    # from devs.lv01_icons_list import icons_list as icons_list
    # icons_list(page) # 3 versions dispos

    # from devs.lv02_blocs import blocs as dev
    # dev(page)

    # # ❌ Finir game NbreX
    # from devs.lv05_nbre_x import game as game
    # game(page)

    # from examples.lv06_todo_simple import todo_list as todo6
    # todo6(page)

    # Test fonctions asynchones
    if 0:
        from examples.lv07_todo_async import todo_list as todo7
        from examples.lv06_async_todo_simple import todo_list as todo6_async

        async def fini():
            print(
                datetime.datetime.now().strftime("%H:%M:%S"), "> Todos 6 & 7 Ready.\n"
            )

        async def async_fctns():
            print(datetime.datetime.now().strftime("%H:%M:%S"), "> async_fctns")
            await asyncio.gather(todo6_async(page), todo7(page))
            await fini()

        await async_fctns()
        time.sleep(1)

    # from examples.lv08_todo import todo_list as todo8
    # todo8(page)

    # from examples.lv09_todo_simple import todo9 as todo9
    # todo9(page)

    # from examples.lv09_todo import todo_list as todo9
    # todo9(page)

    # page.add(ft.Text('─'*49))

    # * [ ] Cf last todo in GH with footer
    # from examples.lv10_todo import todo as finalTodo
    # gc7(page, width=950)
    # finalTodo(page)

    # from examples.lv11_todo import main as finalTodo  # + Footer
    # finalTodo(page)

    # from examples.lv11_todo_official import main as finalTodo
    # gc7(page, "LIGHT", width=600)
    # finalTodo(page)

    # ❌ faire P.R. pour footer

    # ❌ LV 12 à comprendre pour incorporer ici
    # ⚠️  render_views prend le contrôle total de la page → ne pas mélanger avec page.add()
    # from examples.lv12_todo_reactive import main as reactivTodo
    # reactivTodo(page)
    # return  # render_views incompatible avec page.controls / page.add() ci-dessous

    # * [/] chat
    # from examples.lv20_chat import main  # Base
    # main(page)
    # from examples.lv21_chat import main  # Add pubsub.subscribe ( Broadcasting)
    # main(page)
    # [/] 2verif from examples.lv22_chat import main  # Login
    # main(page)
    # from examples.lv23_chat import main  # ↑ User look
    # main(page)
    # ❌ Corr lv24_chat_uuu et finir tuto
    # from examples.lv24_chat_uuu import main
    # main(page)

    gc7(page, mode="LIGHT", width=976)  # 976 pour // 2 l'écran de droite
    page.bgcolor='#333333'

    # from examples.lv30_aastack_example_1 import main
    # from examples.lv30_aastack_example_2 import main  # 3 cards (Bleu-blanc-rouge)
    # from examples.lv30_aastack_example_3 import main  # A card on a tapis

    # from examples.lv30_solitaire import main # GestureDetector
    # from examples.lv31_solitaire import main # drag a card
    # from examples.lv32_solitaire import main  # drag a card on a slot

    from examples.lv33_solitaire import main  # drag a card on a slot else return back position

    main(page)

    # from devs.lv00_dev import dev as dev
    # dev(page)

    if not page.controls:
        page.add(
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                margin=ft.Margin.only(top=25),
                controls=[
                    ft.Text(
                        "No content.",
                        size=30,
                        color=ft.Colors.RED_ACCENT_200,
                        weight=ft.FontWeight.BOLD,
                    )
                ],
            )
        )


if __name__ == "__main__":
    print(datetime.datetime.now().strftime("%H:%M:%S"), "> ")
    ft.run(main)
