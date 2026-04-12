import flet as ft
def simuMsgs():

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
