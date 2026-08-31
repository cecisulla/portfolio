import os

IMAGE_DIR = "assets/img/portfolio"
README_PATH = "README.md"

# Lê as imagens da pasta
images = sorted([f for f in os.listdir(IMAGE_DIR) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))])

# Gera o conteúdo em Markdown (ex: uma lista ou tabela)
image_list = "\n".join([f"![{img}]({IMAGE_DIR}/{img})" for img in images])

# Lê o README atual
with open(README_PATH, "r", encoding="utf-8") as file:
    content = file.read()

# Substitui o conteúdo entre os marcadores
start_marker = "<!-- IMAGES:START -->"
end_marker = "<!-- IMAGES:END -->"

start_idx = content.find(start_marker) + len(start_marker)
end_idx = content.find(end_marker)

new_content = content[:start_idx] + "\n" + image_list + "\n" + content[end_idx:]

with open(README_PATH, "w", encoding="utf-8") as file:
    file.write(new_content)