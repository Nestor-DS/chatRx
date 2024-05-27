import reflex as rx
from chatRx.styles import style

def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(
                question, 
                text_align="right",
            ),
            style=style.question_style
        ),
        rx.box(
            rx.text(
                answer, 
                text_align="left",
            ),
            style=style.question_style
        ),
        margin_y="1em",
    )
