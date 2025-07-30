from os import getenv
from datetime import datetime

from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.agents import initialize_agent, Tool, AgentType, AgentExecutor

API_KEY = getenv("OPENAI_API_KEY")


def get_current_date() -> str:
    """Función para obtener la fecha actual."""
    # TODO: Implementa la lógica para obtener la fecha actual en formato "YYYY-MM-DD".
    # Deberás utilizar la librería datetime para obtener la fecha actual y formatearla
    # correctamente.

    raise NotImplementedError()


def create_agent() -> AgentExecutor:
    """Función para crear un agente de LangChain."""
    # TODO: Implementar la lógica para crear un agente de LangChain que pueda interactuar
    # con el usuario y responder a sus preguntas. Deberás definir las herramientas que el
    # agente puede utilizar, el tipo de agente y la memoria que utilizará para mantener
    # el contexto de la conversación.

    # Para ello, sigue los siguientes pasos:
    # 1. Instancia el modelo de lenguaje que ha de utilizar el agente haciendo uso de ChatOpenAI.
    # 2. Instancia la memoria de conversación utilizando ConversationBufferMemory.
    # 3. Define la herramienta get_current_date como Tool para el agente,
    # especificando su nombre y descripción.
    # 4. Crea el agente utilizando initialize_agent, especificando el tipo de agente
    # (de acuerdo a los diferentes AgentType disponibles), el modelo de lenguaje,
    # la memoria y las herramientas que has instanciado previamente.
    # 5. Devuelve el agente creado.

    raise NotImplementedError()


def agent_chat() -> None:
    """
    Main function to run the agent chat.
    """
    print("Bienvenido al chat de agente. Escribe 'salir' para terminar.")

    agent = create_agent()
    while True:
        prompt = input("Tu: ").strip()

        if prompt.lower() == "salir":
            print("¡Hasta luego!")
            break

        response = agent.run(prompt)
        print(f"Agente: {response}")
