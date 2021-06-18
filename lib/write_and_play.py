from lib import choose_value, generate_playlist
from backend.util import abrir_json, guardar_json
from os import getcwd, startfile, path, remove
from pathlib import Path
from time import sleep
from datetime import datetime

# the base form of this snipet was taken from:
# https://stackoverflow.com/questions/18413229/enqueue-files-to-playlist-in-winamp-with-python

config = abrir_json('config.json')
songlist = abrir_json('songlist.json')
number_of_songs = config['songs']

chosen_songs_filename = []
songs_names = []
while number_of_songs > 0:
    filename = Path(choose_value(songlist))
    chosen_songs_filename.append(filename)
    songs_names.append(filename.stem)
    number_of_songs -= 1

if path.exists(path.join(getcwd(), config['default']+'.pls')) and config['keeppls']:
    random = ''.join([char for char in str(datetime.now()) if char not in [' ', '.', ':', '-']])
    name = config['default'] + random + '.pls'
else:
    name = config['default'] + '.pls'

ruta = path.join(getcwd(), name)
with open(path.join(ruta), 'wt', encoding='latin_1') as file:
    file.writelines(generate_playlist(chosen_songs_filename))

startfile(ruta)
sleep(3)
if not config['keeppls']:
    remove(ruta)

songlist.sort(key=lambda o: o['weight'])
guardar_json(songlist, 'songlist.json')
guardar_json(songs_names, 'chosen.json')
