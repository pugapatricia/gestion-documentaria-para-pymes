import os
import re

# Ruta a la carpeta donde están los documentos
folder = "/Users/patricia/Documents/BD_IA_PROJECT/Documentacion PYME"

# Regex para buscar versiones tipo _v1, _v2, _v10, etc.
pattern = re.compile(r"_v(\d+)", re.IGNORECASE)

versiones = {}

for file in os.listdir(folder):
    if not os.path.isfile(os.path.join(folder, file)):
        continue  # ignorar subcarpetas si las hubiera
    
    match = pattern.search(file)
    if match:
        version = int(match.group(1))
        base_name = file.split("_v")[0]  # ej: "Contrato"
        
        if base_name not in versiones or version > versiones[base_name][0]:
            versiones[base_name] = (version, file)

print("📌 Últimas versiones detectadas:\n")
for doc, (v, file) in versiones.items():
    print(f"📑 Documento base: {doc} | Última versión: {file}")
