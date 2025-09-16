# 1. Clonar o copiar el proyecto
cd carpeta-del-proyecto

# 2. Crear un entorno virtual (recomendado)
python3 -m venv venv
source venv/bin/activate    # Mac/Linux
venv\Scripts\activate       # Windows

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Correr el script
python3 autoposts.py