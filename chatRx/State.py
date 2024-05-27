import reflex as rx
import os
import asyncio
from openai import AsyncOpenAI, OpenAIError, RateLimitError

# Establece tu API key directamente en el código para pruebas
os.environ["OPENAI_API_KEY"] = ''

class State(rx.State):
    question: str
    chat_history: list[tuple[str, str]] = []

    async def answer(self):
        try:
            print("Creando cliente de OpenAI...")
            client = AsyncOpenAI(api_key=os.environ["OPENAI_API_KEY"])

            print("Iniciando sesión de chat...")
            session = await client.chat.completions.create(
                model="gpt-3.5-turbo-16k",
                messages=[{"role": "user", "content": self.question}],
                stop=None,
                temperature=0.7,
                stream=True,
            )

            # Añadir a la respuesta a medida que el chatbot responde
            answer = ""
            self.chat_history.append((self.question, answer))

            # Limpiar la entrada de la pregunta
            self.question = ""
            # Yield aquí para limpiar la entrada del frontend antes de continuar
            yield

            async for item in session:
                print("Recibiendo respuesta del chatbot...")
                if hasattr(item.choices[0].delta, "content"):
                    if item.choices[0].delta.content is None:
                        # Presencia de 'None' indica el final de la respuesta
                        break
                    answer += item.choices[0].delta.content
                    self.chat_history[-1] = (self.chat_history[-1][0], answer)
                    yield
        except RateLimitError as e:
            print(f"Error de cuota: {e}. Has excedido tu cuota de API. Por favor, revisa tu plan y los detalles de facturación en OpenAI.")
        except OpenAIError as e:
            print(f"Error de OpenAI: {e}. Por favor, revisa tu plan y los detalles de facturación en OpenAI.")
        except Exception as e:
            print(f"Otro error ocurrió: {e}")
