from util import abrir_json, guardar_json
from constantes import MOCKMODE
from random import choice
from os import startfile

# the base form of this snipet was taken from:
# https://stackoverflow.com/questions/18413229/enqueue-files-to-playlist-in-winamp-with-python

config = abrir_json('config.json')
songlist = abrir_json('songlist.json')
number_of_songs = config['songs']

while number_of_songs > 0:
    chosen_file = choice(songlist)
    idx = songlist.index(chosen_file)
    filename = chosen_file['root']
    if MOCKMODE is False:
        # this relies on the fact that winamp is setup to enqueue files on double-click.
        startfile(filename)

    if 'times' in chosen_file:
        chosen_file['times'] += 1
    else:
        chosen_file['times'] = 1
    number_of_songs -= 1

guardar_json(songlist, 'songlist.json')
