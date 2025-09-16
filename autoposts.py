from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import textwrap

# 1. Cargar datos
df = pd.read_csv("posts.csv")

# 2. Configuración
font = ImageFont.truetype("arial.ttf", 36)  # cambia por tu fuente

def draw_bubble(draw, text, xy, fill, max_width):
    wrapped = textwrap.fill(text, width=max_width)
    
    # Obtener tamaño del texto
    bbox = draw.multiline_textbbox((0, 0), wrapped, font=font)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]

    x, y = xy
    padding = 30
    rect = [x, y, x + w + padding*2, y + h + padding*2]

    # Dibujar burbuja
    draw.rounded_rectangle(rect, radius=40, fill=fill)

    # Dibujar texto
    draw.multiline_text((x + padding, y + padding), wrapped, font=font, fill="white")

    return rect[3]  # devolver y final

# 3. Generar imágenes
for i, row in df.iterrows():
    # 📌 Usar fondo (ejemplo: fondo estilo chat)
    bg = Image.open("bg.png").convert("RGB")
    W, H = bg.size
    draw = ImageDraw.Draw(bg)

    # Pregunta (derecha)
    y = 100
    y = draw_bubble(draw, row["Pregunta"], (295, y), fill=(33, 33, 33), max_width=30)

    # Respuesta (izquierda)
    y += 50
    draw_bubble(draw, row["Respuesta"], (50, y), fill=(0,0,0), max_width=50)
    
    # Guardar
    bg.save(f"post_{i+1}.png")
