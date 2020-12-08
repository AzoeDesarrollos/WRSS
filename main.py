from lib import choose_value, generate_playlist
from util import abrir_json, guardar_json
from os import getcwd, startfile, path, remove
from pathlib import Path
from time import sleep
from datetime import datetime

# the base form of this snipet was taken from:
# https://stackoverflow.com/questions/18413229/enqueue-files-to-playlist-in-winamp-with-python

config = abrir_json('config.json')
songlist = abrir_json('songlist.json')
number_of_songs = config['songs']

chosen_songs = []
while number_of_songs > 0:
    filename = choose_value(songlist)
    chosen_songs.append(Path(filename))
    number_of_songs -= 1

if path.exists(path.join(getcwd(), config['default'])) and config['keeppls']:
    random = ''.join([char for char in str(datetime.now()) if char not in [' ', '.', ':', '-']])
    name = config['default'][:-4] + random + config['default'][-4:]
else:
    name = config

ruta = path.join(getcwd(), name)
with open(path.join(ruta), 'wt', encoding='utf-8') as file:
    file.writelines(generate_playlist(chosen_songs))

startfile(ruta)
sleep(3)
if not config['keeppls']:
    remove(ruta)

songlist.sort(key=lambda o: o['weight'])
guardar_json(songlist, 'songlist.json')
