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
    messages.append({"role": "user", "content": prompt})
    response = openai_client.chat.completions.create(
        model="gpt-4.1",
        max_completion_tokens=100,
        temperature=1,
        messages=messages,  # type: ignore
    )
    message_content = response.choices[0].message.content or ""
    messages.append({"role": "assistant", "content": message_content})

    return message_content


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
