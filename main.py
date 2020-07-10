from util import abrir_json, guardar_json
from weighted_choice import choose_value
from constantes import MOCKMODE
from os import startfile

# the base form of this snipet was taken from:
# https://stackoverflow.com/questions/18413229/enqueue-files-to-playlist-in-winamp-with-python

config = abrir_json('config.json')
songlist = abrir_json('songlist.json')
number_of_songs = config['songs']

while number_of_songs > 0:
    filename = choose_value(songlist)
    if MOCKMODE is False:
        # this relies on the fact that winamp is setup to enqueue files on double-click.
        startfile(filename)
    number_of_songs -= 1

guardar_json(songlist, 'songlist.json')
