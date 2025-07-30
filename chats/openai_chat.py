from os import getenv
from openai import OpenAI
from .types import Message

API_KEY = getenv("OPENAI_API_KEY")
openai_client = OpenAI(api_key=API_KEY)

messages: list[Message] = [
    {
        "role": "system",
        "content": "Eres un asistente ágil, práctico y con buen sentido del humor.",
    }
]


def send_message(prompt: str) -> str:
    """Función para enviar un mensaje al modelo de OpenAI y recibir una respuesta."""
    # TODO: Implementar la lógica para enviar el mensaje a la API de OpenAI, haciendo uso
    # de la librería cliente de OpenAI, y recibir la respuesta. Deberás hacer uso del método
    # correcto del cliente y manejar la respuesta para extraer el texto generado por el modelo.

    # Para ello, responde primero estas preguntas:
    # 1. ¿Qué método del cliente de OpenAI necesitas utilizar?
    # 2. ¿Qué parámetros son necesarios para la petición?
    # 3. ¿Cómo se estructura la respuesta del modelo?

    # Además de realizar la petición, deberás almacenar tanto el mensaje de entrada como
    # la respuesta dada por el modelo en la variable `messages`, para mantener
    # el contexto de la conversación en cada interacción (piensa que el modelo necesita
    # ver el historial de mensajes en cada petición para generar respuestas coherentes).

    raise NotImplementedError()


def openai_chat() -> None:
    """
    Main function to run the OpenAI chat.
    """

    print(
        "Bienvenido al chat libería cliente de OpenAI. Escribe 'salir' para terminar."
    )
    while True:
        prompt = input("Tu: ").strip()

        if prompt.lower() == "salir":
            print("¡Hasta luego!")
            break

        response = send_message(prompt)
        print(f"Chatbot: {response}")
