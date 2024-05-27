import reflex as rx
from chatRx.components.chat import chat
from chatRx.components.input import action_bar

"""
        rx.text("Chat Bot"),
        chat(),
        action_bar(),
        align="center",
        """

def chatBot() -> rx.Component:
    return rx.box(
        rx.dialog.root(
            rx.dialog.trigger(rx.button("Chat Bot", size="4")),
            rx.dialog.content(
                rx.dialog.title("Chat Bot"),
                rx.flex(
                    chat(),
                    action_bar(),
                    align="center",
                    ),
                ),
        )
    )