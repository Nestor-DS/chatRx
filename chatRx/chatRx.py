"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from chatRx.views.chatBot import chatBot
from chatRx.styles import style


from rxconfig import config



def index() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            chatBot(),
        ),
        rx.logo(),
    )


app = rx.App()
app.add_page(index)
