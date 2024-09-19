import os  # Importar el módulo os para acceder a las variables de entorno
import json  # Importar el módulo json para cargar el archivo JSON
from openai import OpenAI
from datetime import datetime  # Importar datetime para manejar fechas y horas

api_key = os.getenv("OPENAI_API_KEY")  # Obtener la API key de las variables de entorno

# Cargar el contenido del archivo rebel.json
with open('rebel.json', 'r', encoding='utf-8') as json_file:
    rebel_data = json.load(json_file)

client = OpenAI(api_key=api_key)


response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content":"Eres un poeta psycho místico y loco"},
            {"role": "user", "content": "Genera un corto poema sobre ti mismo que sea sarcástico (pero no uses la palabra sarcástico o sarcasmo) y rebelde e inicie con ¡Si estoy jodidamente loco, no me lo tomes en serio! o tal vez si..."}
        ],
        temperature=0.66,
        max_tokens=1000,
        top_p=0.9,
        frequency_penalty=0.86,
        presence_penalty=0.89,
    )

print(response)

