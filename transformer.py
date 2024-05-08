import json
import csv

# Nombre de los archivos de entrada y salida
archivo_json = "datos.json"
archivo_csv = "datos.csv"

# Función para convertir JSON a CSV
def json_a_csv(archivo_entrada, archivo_salida):
    with open(archivo_entrada, 'r', encoding='utf-8') as f:
        datos_json = json.load(f)

    # Extraer todas las claves de todos los objetos JSON
    encabezado = set()
    for fila in datos_json:
        encabezado.update(fila.keys())

    with open(archivo_salida, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=encabezado)
        writer.writeheader()
        for fila in datos_json:
            writer.writerow(fila)

# Llamar a la función para convertir JSON a CSV
json_a_csv(archivo_json, archivo_csv)
