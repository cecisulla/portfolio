import os

IMAGE_DIR = "assets/img/portfolio"
README_PATH = "README.md"

# 1. Verifica se a pasta existe
if not os.path.exists(IMAGE_DIR):
    print(f"Diretório {IMAGE_DIR} não encontrado.")
    exit(0)

# 2. Lê e filtra as imagens da pasta
images = sorted([f for f in os.listdir(IMAGE_DIR) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))])

# 3. Gera o HTML/Markdown para exibir as imagens em formato de lista ou galeria
image_list = "\n".join([f'<img src="{IMAGE_DIR}/{img}" width="300" alt="{img}">' for img in images])

# 4. Lê o README atual
if not os.path.exists(README_PATH):
    print(f"Arquivo {README_PATH} não encontrado.")
    exit(1)

with open(README_PATH, "r", encoding="utf-8") as file:
    content = file.read()

# 5. Define os marcadores
start_marker = "<!-- IMAGES:START -->"
end_marker = "<!-- IMAGES:END -->"

if start_marker not in content or end_marker not in content:
    print("Erro: Os marcadores <!-- IMAGES:START --> ou <!-- IMAGES:END --> não foram encontrados no README.md.")
    exit(1)

# 6. Realiza a substituição de forma segura entre os marcadores
start_idx = content.find(start_marker) + len(start_marker)
end_idx = content.find(end_marker)

new_content = content[:start_idx] + "\n\n" + image_list + "\n\n" + content[end_idx:]

# 7. Salva o arquivo atualizado
with open(README_PATH, "w", encoding="utf-8") as file:
    file.write(new_content)

print("README atualizado com sucesso!")