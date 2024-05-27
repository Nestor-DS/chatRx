import reflex as rx
from chatRx.styles import style
from chatRx.State import State

def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            value=State.question,
            placeholder="Ask a question",
            on_change=State.set_question,
            style=style.input_style),
        rx.button("Ask", on_click=State.answer, style=style.button_style),
    )