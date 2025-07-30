# ChatCMD 💬

En este proyecto, crearás un pequeño asistente de chat que puede responder preguntas y mantener conversaciones a través de la línea de comandos. El asistente se conectará a un modelo de lenguaje de OpenAI para generar respuestas basadas en las entradas del usuario. Crearemos tres versiones del asistente:

- 😐 **Versión básica**: Haciendo uso de `requests`, realizando peticiones HTTP a la API de OpenAI.
- 😎 **Versión avanzada**: Utilizando la librería cliente oficial de OpenAI, que simplifica la interacción con la API.
- 🧠 **Versión agente**: Implementando una cadena de `langchain`, que permite incluir herramientas y funcionalidades avanzadas, como la capacidad de buscar información en la web para incluir en las respuestas.

## 1. Requisitos

- `python ≥ 3.12`
- `git`

## 2. Arranque rápido

```bash
# Clona tu propio fork
git clone <tu‑fork‑url> chat-cmd
cd chat-cmd

# Crea y activa un entorno virtual
python -m venv .venv
source .venv/bin/activate      # Windows: .\.venv\Scripts\activate

# Instala dependencias de desarrollo
pip install -r requirements-dev.txt

# Formatea y analiza (solo deberían aparecer TODOs sin implementar)
black .
pylint chat_cmd.py chats/
mypy chat_cmd.py chats/

# Ejecuta el juego (fallará hasta que completes el código)
python chat_cmd.py
```

## 3. Variables de entorno

En este proyecto, utilizamos variables de entorno para almacenar la clave de la API de OpenAI. Este es un mecanismo común para mantener seguras las credenciales sensibles, evitando tenerlas escritas directamente en el código. Para configurar dicha variable de entorno, crea un archivo llamado `.env` en la raíz del proyecto y añade la siguiente línea:

```plaintext
OPENAI_API_KEY=<clave_de_api_de_openai>
```

## 4. Tareas a completar

1. Implementa las funciones marcadas con **`TODO`** en los archivos `chats/http_chat.py`, `chats/openai_chat.py` y `chats/agent_chat.py`.
