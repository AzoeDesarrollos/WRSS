import json


def abrir_json(ruta):
    with open(ruta, 'rt', encoding='utf-8') as file:
        return json.load(file)


def guardar_json(datos, ruta):
    with open(ruta, 'wt', encoding='utf-8') as file:
        json.dump(datos, file, ensure_ascii=False, indent=2, separators=(',', ':'), sort_keys=True)
