from os import getenv
import requests
from .types import Message

API_KEY = getenv("OPENAI_API_KEY")


messages: list[Message] = [
    {
        "role": "system",
        "content": "Eres un asistente ágil, práctico y con buen sentido del humor.",
    }
]


def send_message(message: str) -> str:
    """Función para enviar un mensaje al modelo de OpenAI y recibir una respuesta."""
    # TODO: Implementar la lógica para enviar el mensaje a la API de OpenAI, haciendo uso
    # de la librería requests, y recibir la respuesta. Deberás realizar la petición correcta
    # y manejar la respuesta para extraer el texto generado por el modelo.

    # Para ello, responde primero estas preguntas:
    # 1. ¿Qué endpoint de la API de OpenAI necesitas utilizar?
    # 2. ¿Qué tipo de petición hay que hacer (GET, POST, etc.)?
    # 3. ¿Qué formato ha de tener el JSON de la petición?
    # 4. ¿Qué cabeceras HTTP son necesarias (por ejemplo, para la autenticación)?
    # 5. ¿Qué formato tiene el JSON de la respuesta?

    # Además de realizar la petición, deberás almacenar tanto el mensaje de entrada como
    # la respuesta dada por el modelo en la variable `messages`, para mantener
    # el contexto de la conversación en cada interacción (piensa que el modelo necesita
    # ver el historial de mensajes en cada petición para generar respuestas coherentes).

    raise NotImplementedError()


def http_chat() -> None:
    """
    Main function to run the HTTP chat.
    """

    print("Bienvenido al chat HTTP. Escribe 'salir' para terminar.")
    while True:
        prompt = input("Tu: ").strip()

        if prompt.lower() == "salir":
            print("¡Hasta luego!")
            break

        response = send_message(prompt)
        print(f"Chatbot: {response}")
