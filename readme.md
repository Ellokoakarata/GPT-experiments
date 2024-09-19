# GPT Experiments

Este repositorio contiene experimentos utilizando la API de OpenAI para generar poemas y respuestas creativas basadas en prompts específicos.

## Estructura del Proyecto

- **`response.py`**: Este archivo contiene la lógica para interactuar con la API de OpenAI y generar respuestas basadas en un prompt. Se utiliza para definir el comportamiento del modelo y cómo debe responder a las solicitudes.
  
- **`test.py`**: Este archivo es el script principal que ejecuta la generación de poemas utilizando la API de OpenAI. Aquí se define el prompt y se llama a la API para obtener la respuesta.

- **`responses.txt`**: Este archivo almacena las respuestas generadas por el modelo, junto con la fecha y hora de cada respuesta. Se utiliza para registrar los resultados de las pruebas y las interacciones con el modelo.

- **`output.txt`**: Este archivo contiene los primeros outputs de las pruebas realizadas con el generador. Se utiliza para realizar un seguimiento de las salidas iniciales y evaluar el rendimiento del modelo.

- **`rebel.json`**: Este archivo contiene la configuración o los prompts que se utilizan para guiar al modelo en la generación de respuestas. Define el contexto y las instrucciones que el modelo debe seguir.

## Requisitos

- Python 3.x
- Biblioteca `openai`
- Otras dependencias necesarias (si las hay).

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Ellokoakarata/GPT-experiments.git
   ```

2. Navega al directorio del proyecto:
   ```bash
   cd GPT-experiments
   ```

3. Instala las dependencias necesarias:
   ```bash
   pip install openai
   ```

## Uso

Ejecuta el script `test.py` para generar algo de vomitiva poética:

Las respuestas se guardarán en `responses.txt`.

## Contribuciones

Si deseas contribuir a este proyecto, siéntete libre de hacer un fork y enviar un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.