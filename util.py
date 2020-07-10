import json


def abrir_json(ruta):
    with open(ruta, 'rt', encoding='utf-8') as file:
        return json.load(file)
