from typing import TypedDict


class Message(TypedDict):
    """Representa un mensaje en la conversación."""

    role: str
    content: str
