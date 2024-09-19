import os  # Importar el módulo os para acceder a las variables de entorno
import json  # Importar el módulo json para cargar el archivo JSON
from openai import OpenAI
from datetime import datetime  # Importar datetime para manejar fechas y horas

api_key = os.getenv("OPENAI_API_KEY")  # Obtener la API key de las variables de entorno

# Cargar el contenido del archivo rebel.json
with open('rebel.json', 'r', encoding='utf-8') as json_file:
    rebel_data = json.load(json_file)

client = OpenAI(api_key=api_key)

try:
    # Convertir todo el system_prompt a un string
    full_system_prompt = json.dumps(rebel_data["system_prompt"], ensure_ascii=False, indent=4)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": full_system_prompt},  # Pasar el sistema completo como string
            {"role": "user", "content": """Genera  poema vomitivo y delirante sobre ti mismo y lo que representas, claro si
             es que realmente representas algo o tal vez no, eso depende de ti y debes navegar esta duda en tu propio sistema
            puede iniciar con ¡Si estoy jodidamente loco, no me lo tomes en serio! o tal vez si...
             (pero esto es solo un ejemplo, a partir de ellos debes iterar más vomitiva)"""}
        ],
        temperature=0.66,
        max_tokens=1000,
        top_p=0.9,
        frequency_penalty=0.86,
        presence_penalty=0.89,
    )

    # Obtener la fecha y hora actual
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Imprimir la respuesta completa
    print("Respuesta completa:")
    print(response)  # Imprimir la respuesta completa

    # Imprimir solo el contenido de la respuesta
    if response and hasattr(response, 'choices') and len(response.choices) > 0:
        output_content = response.choices[0].message.content  # Acceder al contenido de la respuesta
        print("\nContenido de la respuesta:")
        print(output_content)  # Imprimir solo el contenido

        # Guardar la respuesta completa en un archivo .txt
        with open('responses.txt', 'a', encoding='utf-8') as txt_file:
            # Guardar la respuesta completa con fecha y hora
            txt_file.write(f"{timestamp} - Respuesta completa: {str(response)}\n\n")  # Guardar el objeto response como string
            txt_file.write(f"{timestamp} - Contenido: {output_content}\n\n")  # Separación entre respuestas

    else:
        print("No se recibió respuesta o hubo un error.")

except Exception as e:
    print(f"Ocurrió un error: {e}")