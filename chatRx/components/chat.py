import reflex as rx
from chatRx.components.qa import qa
from chatRx.State import State

def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            State.chat_history,
            lambda message: qa(message[0], message[1]),
        )
    )