import json
from os import path, getcwd

r = path.join(getcwd(), 'config')


def abrir_json(ruta):
    ruta = path.join(r, ruta)
    with open(ruta, 'rt', encoding='utf-8') as file:
        return json.load(file)


def guardar_json(datos, ruta):
    ruta = path.join(r, ruta)
    with open(ruta, 'wt', encoding='utf-8') as file:
        json.dump(datos, file, ensure_ascii=False, indent=2, separators=(',', ':'), sort_keys=True)


route = path.join(r, 'config.json')
if not path.exists(route):
    default = {'root': 'D:/Mp3',
               'songs': 20,
               'keeppls': False,
               'default': 'playlist',
               'weights': False}
    guardar_json(default, route)
