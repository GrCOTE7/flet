from enum import auto

import flet as ft
from dataclasses import dataclass
import asyncio, random, time


@dataclass
class Message:
    user_name: str
    text: str
    msg_type: str


@ft.control
class ChatMessage(ft.Row):
    def __init__(self, message: Message):
        super().__init__()
        self.message = message
        self.vertical_alignment = ft.CrossAxisAlignment.START
        self.controls = [
            ft.CircleAvatar(
                content=ft.Text(self.get_initials(self.message.user_name)),
                color=ft.Colors.WHITE,
                bgcolor=self.get_avatar_color(self.message.user_name),
            ),
            ft.Column(
                tight=True,
                spacing=5,
                controls=[
                    ft.Text(self.message.user_name, weight=ft.FontWeight.BOLD),
                    ft.Text(self.message.text, selectable=True),
                ],
            ),
        ]

    def get_initials(self, user_name: str):
        if user_name:
            return user_name[:1].capitalize()
        else:
            return "Unknown"  # or any default value you prefer

    def get_avatar_color(self, user_name: str):
        colors_lookup = [
            ft.Colors.AMBER,
            ft.Colors.BLUE,
            ft.Colors.BROWN,
            ft.Colors.CYAN,
            ft.Colors.GREEN,
            ft.Colors.INDIGO,
            ft.Colors.LIME,
            ft.Colors.ORANGE,
            ft.Colors.PINK,
            ft.Colors.PURPLE,
            ft.Colors.RED,
            ft.Colors.TEAL,
            ft.Colors.YELLOW,
        ]
        return colors_lookup[hash(user_name) % len(colors_lookup)]


def main(page: ft.Page):

    page.bgcolor = "#333333"
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    page.title = "Flet Chat 2aa3"

    def join_chat_click(e):

        if not join_user_name.value:
            join_user_name.error = "Name can't be blank!"
            join_user_name.update()
        else:
            page.session.store.set("user_name", join_user_name.value)
            welcome_dlg.open = False
            new_message.prefix = ft.Text(f"{join_user_name.value}: ")
            page.pubsub.send_all(
                Message(
                    user_name=join_user_name.value,
                    text=f"{join_user_name.value} has joined the chat.",
                    msg_type="login_message",
                )
            )

    # async def send_message_click(e):
    #     page.pubsub.send_all(
    #         Message(
    #             user=page.session.store.get("user_name"),  # 2ar # type: ignore
    #             text=new_message.value,
    #             msg_type="chat_message",
    #         )
    #     )
    #     print(user_name.value, "→", new_message.value)
    #     new_message.value = ""

    # chat = ft.Column()

    # new_message = ft.TextField(
    #     bgcolor="#111111", color=ft.Colors.WHITE, border_color="#777777"
    # )
    # new_message.expand = True

    async def send_message_click(e):
        if new_message.value != "":
            page.pubsub.send_all(
                Message(
                    page.session.store.get("user_name"),
                    new_message.value,
                    msg_type="chat_message",
                )
            )
            new_message.value = ""
            await new_message.focus()

    def on_message(message: Message):
        if message.msg_type == "chat_message":
            m = ChatMessage(message)
        elif message.msg_type == "login_message":
            m = ft.Text(message.text, italic=True, color=ft.Colors.WHITE_54, size=14)
        chat.controls.append(m)
        page.update()

    page.pubsub.subscribe(on_message)  # Broadcasting
    # user_name = ft.TextField(label="Enter your name", value="Lionel")

    # page.show_dialog(
    #     ft.AlertDialog(
    #         open=True,
    #         modal=True,
    #         title="Welcome!",
    #         content=ft.Column([user_name], tight=True),
    #         actions=[
    #             ft.Button(
    #                 content="Join chat",
    #                 on_click=join_click,
    #                 style=ft.ButtonStyle(
    #                     mouse_cursor=ft.MouseCursor.CLICK,
    #                     bgcolor=ft.Colors.BLACK_54,
    #                     # side=ft.BorderSide(1, ft.Colors.RED),
    #                     shape=ft.RoundedRectangleBorder(radius=7),
    #                 ),
    #             )
    #         ],
    #         actions_alignment=ft.MainAxisAlignment.END,
    #         bgcolor="#252525",
    #         shape=ft.RoundedRectangleBorder(radius=12),
    #     )
    # )

    # A dialog asking for a user displcwxay name
    join_user_name = ft.TextField(
        label="Enter your name to join the chat",
        autofocus=True,
        on_submit=join_chat_click,
    )
    welcome_dlg = ft.AlertDialog(
        open=True,
        modal=True,
        title=ft.Text("Welcome!"),
        content=ft.Column([join_user_name], width=300, height=70, tight=True),
        actions=[ft.Button(content="Join chat", on_click=join_chat_click)],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    page.overlay.append(welcome_dlg)

    # Simule le clic sur "Join chat" avec le champ deja rempli.
    # join_chat_click(None)

    # Chat messages
    chat = ft.ListView(
        expand=True,
        spacing=10,
        auto_scroll=True,
    )
    # A new message entry form
    new_message = ft.TextField(
        hint_text="Write a message...",
        autofocus=True,
        shift_enter=True,
        min_lines=1,
        max_lines=5,
        filled=True,
        expand=True,
        on_submit=send_message_click,
    )

    async def simuMsgs():

        users = [
            "1Alice",
            "1Bob",
            "1Charlie",
            "1Diana",
            "2Alice",
            "2Bob",
            "2Charlie",
            "2Diana",
            "3Alice",
            "3Bob",
            "3Charlie",
            "3Diana",
            "4Alice",
            "4Bob",
            "4Charlie",
            "4Diana",
            "5Alice",
            "5Bob",
            "5Charlie",
            "5Diana",
        ]
        messages = [
            "Hello everyone!",
            "How's it going?",
            "Anyone up for a game?",
            "What's the plan for today?",
            "Did you see the news?",
            "2 Hello everyone!",
            "How's it going?",
            "Anyone up for a game?",
            "What's the plan for today?",
            "Did you see the news?",
            "3 Hello everyone!",
            "How's it going?",
            "Anyone up for a game?",
            "What's the plan for today?",
            "Did you see the news?",
            "4 Hello everyone!",
            "How's it going?",
            "Anyone up for a game?",
            "What's the plan for today?",
            "Did you see the news?",
            "5 Hello everyone!",
            "How's it going?",
            "Anyone up for a game?",
            "What's the plan for today?",
            "Did you see the news?",
        ]

        random.shuffle(users)
        selected_messages = random.sample(messages, k=len(users))

        for user, text in zip(users, selected_messages):
            await asyncio.sleep(random.randint(2, 5))
            page.pubsub.send_all(
                Message(
                    user=user,
                    text=text,
                    msg_type="chat_message",
                )
            )
            print(user, "→", text)

        if not page.session.store.get("user_name"):
            join_click(None)

    page.run_task(simuMsgs)

    page.add(
        ft.Row(
            [
                ft.Text(
                    page.title,
                    size=18,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Container(
            content=chat,
            border=ft.Border.all(1, ft.Colors.OUTLINE),
            border_radius=7,
            padding=10,
            expand=True,
        ),
        ft.Row(
            [
                new_message,
                ft.IconButton(
                    icon=ft.Icons.SEND_ROUNDED,
                    tooltip="Send message",
                    height=46,
                    on_click=send_message_click,
                    style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=4),
                        bgcolor=ft.Colors.BLACK_54,
                        mouse_cursor=ft.MouseCursor.CLICK,
                    ),
                ),
            ],
            spacing=10,
        ),
    )


if __name__ == "__main__":
    ft.run(main)
