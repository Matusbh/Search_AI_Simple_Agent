# AI Research Agent

Mi primer proyecto con agentes de IA. Es un asistente de investigación sencillo hecho en Python con LangChain y Claude (Anthropic).

> **Nota:** este proyecto es mi primera toma de contacto con este tipo de proyectos.

## Qué hace

1. Te pregunta qué quieres investigar.
2. El agente (Claude) decide qué herramientas usar para responder.
3. Busca información en internet con DuckDuckGo.
4. Guarda el resultado en un archivo de texto (`research_output.txt`).
5. Devuelve la respuesta con un formato fijo: tema, resumen, fuentes y herramientas usadas.

## Qué he aprendido con él

- Cómo crear un agente con LangChain que usa herramientas (`create_tool_calling_agent` y `AgentExecutor`).
- Cómo crear mis propias herramientas (buscar en la web y guardar en un archivo).
- Cómo obligar al modelo a responder con un formato concreto usando Pydantic.
- Cómo guardar las claves de API en un archivo `.env` sin subirlas al repositorio.

## Estructura

| Archivo            | Para qué sirve                                                   |
| ------------------ | ---------------------------------------------------------------- |
| `main.py`          | Programa principal: modelo, prompt, agente y salida estructurada |
| `tools.py`         | Herramientas del agente: búsqueda web y guardado en archivo      |
| `requirements.txt` | Dependencias del proyecto                                        |
| `.env`             | Clave de API (no se sube a git)                                  |

## Cómo usarlo

1. Crea y activa un entorno virtual:
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```
2. Instala las dependencias:
   ```powershell
   pip install -r requirements.txt
   ```
3. Escribe lo que quieres investigar y mira el resultado en la terminal y en `research_output.txt`.

## Tecnologías

- Python
- LangChain
- Claude (Anthropic)
- DuckDuckGo Search
- Pydantic
