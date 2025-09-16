# 1. Clonar o copiar el proyecto
cd carpeta-del-proyecto

# 2. Crear un entorno virtual (recomendado)
python3 -m venv venv
source venv/bin/activate    # Mac/Linux
venv\Scripts\activate       # Windows

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Crear un archivo csv
Crea un archivo .csv con las columnas "Pregunta" "Respuesta", añade las preguntas y respuestas en cada linea por cada imagen a crear.

# 5. Correr el script
python3 autoposts.py