from random import choice
from os import listdir, path, startfile
from util import abrir_json

# the base form of this snipet was taken from:
# https://stackoverflow.com/questions/18413229/enqueue-files-to-playlist-in-winamp-with-python

number_of_songs = 20
root = abrir_json('config.json')['root']
while number_of_songs > 0:
    filename = choice(listdir(root))
    if filename.endswith('mp3'):
        filepath = path.join(root, filename)

        # this relies on the fact that winamp is setup to enqueue files on double-click.
        startfile(filepath)
        number_of_songs -= 1
