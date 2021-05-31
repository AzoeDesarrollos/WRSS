from .eventhandler import EventHandler
from os import path, getcwd, mkdir
from pygame import quit
from sys import exit
import json

r = path.join(getcwd(), 'config')
if not path.exists(r):
    mkdir(r)


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


def salir_handler(event):
    print('Status:' + event.data['texto'])
    quit()
    exit()


EventHandler.register(salir_handler, 'salir')
