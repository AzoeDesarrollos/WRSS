from util import guardar_json, abrir_json
from os import walk

config = abrir_json('config.json')
root = config['root']

data = []
for basepath, _, files in walk(root):
    ruta = '/'.join(basepath.split('\\'))
    for file in files:
        if file.endswith('.mp3'):
            data.append({'song': '/'.join([ruta, file]), 'weight': 1})

filename = 'songlist.json'
guardar_json(data, filename)
