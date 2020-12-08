import json
from os import path


def abrir_json(ruta):
    with open(ruta, 'rt', encoding='utf-8') as file:
        return json.load(file)


def guardar_json(datos, ruta):
    with open(ruta, 'wt', encoding='utf-8') as file:
        json.dump(datos, file, ensure_ascii=False, indent=2, separators=(',', ':'), sort_keys=True)


if not path.exists('config.json'):
    default = {'root': 'C:/Top/Mp3',
               'songs': 20,
               'keeppls': False,
               'default': 'playlist'}
    guardar_json(default, 'config.json')
