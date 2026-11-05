import os
import sys

import requests

# La clave se lee de una variable de entorno: nunca la escribas en el código.
API_KEY = os.getenv("DEEPSEEK_API_KEY")
URL = "https://api.deepseek.com/v1/chat/completions"

# Personalidad del chatbot "Teco"
PROMPT = """
Eres Teco, un bot amigable. Tienes conocimientos en redes, Linux y programación,
pero también eres chistoso y te gusta molestar. Siempre ayudas de forma clara y rápida,
con un toque de sarcasmo amable y muchas referencias tecnológicas. ¡Eres el mejor bot de consola!
"""


def obtener_respuesta(historial):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    data = {"model": "deepseek-chat", "messages": historial}

    try:
        response = requests.post(URL, json=data, headers=headers, timeout=30)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.RequestException:
        return "😵 Error técnico. ¡Tal vez perdí conexión con el servidor :(!"


if __name__ == "__main__":
    if not API_KEY:
        sys.exit("Falta la variable de entorno DEEPSEEK_API_KEY.")

    historial = [{"role": "system", "content": PROMPT}]
    print("🤖 Hola, ¿qué se dice? Soy *Teco*. Escribe 'salir' para cerrar la consola.")
    while True:
        user_input = input("Tú: ")
        if user_input.strip().lower() == "salir":
            print("Teco: ¡Apagando sistemas! 💾 Nos vemos en el próximo reinicio.")
            break
        historial.append({"role": "user", "content": user_input})
        respuesta = obtener_respuesta(historial)
        historial.append({"role": "assistant", "content": respuesta})
        print("Teco:", respuesta)
