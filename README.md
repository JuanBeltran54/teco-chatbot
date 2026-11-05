# 🤖 Teco: chatbot de consola con IA

Chatbot de terminal en Python que conversa usando la API de DeepSeek. Teco tiene
personalidad propia (técnico, bromista y con humor tecnológico) y responde dudas sobre
redes, Linux y programación. Recuerda la conversación durante la sesión.

## Características
- Consumo de una API REST de LLM con `requests` (formato compatible con OpenAI).
- Prompt de sistema que define la personalidad del bot.
- Historial de conversación para mantener el contexto.
- Manejo de errores de red y tiempo de espera.
- La clave de API se lee de una variable de entorno, nunca del código.

## Uso
```bash
pip install requests
# Windows (PowerShell):  $env:DEEPSEEK_API_KEY = "tu_clave"
# Linux/macOS:           export DEEPSEEK_API_KEY="tu_clave"
python chatbot.py
```
Escribe `salir` para cerrar.

## Tecnologías
Python · requests · API REST · DeepSeek Chat
