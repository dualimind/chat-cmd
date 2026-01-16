from dotenv import load_dotenv
from chats import http_chat, openai_chat, agent_chat

load_dotenv()


def main() -> None:
    """
    Función principal que ejecuta los diferentes tipos de chat según la
    elección del usuario.
    """

    chat_mode = input("Elige el modo de chat (http/openai/agent): ").strip().lower()
    if chat_mode == "http":
        http_chat()
    elif chat_mode == "openai":
        openai_chat()
    elif chat_mode == "agent":
        agent_chat()
    else:
        print("Modo de chat no válido.")


if __name__ == "__main__":
    main()
