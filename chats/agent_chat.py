from os import getenv
from datetime import datetime

from langchain.chat_models import init_chat_model
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import InMemorySaver

API_KEY = getenv("OPENAI_API_KEY")


def get_current_date() -> str:
    """Función para obtener la fecha actual."""
    return datetime.now().date().isoformat()


def create_agent():
    """Función para crear un agente de LangChain."""
    model = init_chat_model("openai:gpt-4.1", temperature=0.5, timeout=5)
    memory = InMemorySaver()
    agente = create_react_agent(
        model=model,
        tools=[get_current_date],
        prompt="You are a helpful assistant",
        checkpointer=memory,
    )
    return agente


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

        response = agent.invoke(
            {"messages": prompt}, {"configurable": {"thread_id": "1"}}
        )
        print(f"Agente: {response['messages'][-1].content}")
