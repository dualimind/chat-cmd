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
    api_url = "https://api.openai.com/v1/chat/completions"
    messages.append({"role": "user", "content": message})
    response = requests.post(
        api_url,
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={"model": "gpt-4.1", "messages": messages},
        timeout=5,
    )
    response_message = response.json()["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": response_message})
    return response_message


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
