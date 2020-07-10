from util import guardar_json, abrir_json
from os import walk, path

filename = 'songlist.json'
config = abrir_json('config.json')
root = config['root']
songlist = abrir_json(filename)

refresh_weights = True

data = []
i = -1
for basepath, _, files in walk(root):
    ruta = '/'.join(basepath.split('\\'))
    for file in files:
        if file.endswith('.mp3'):
            d = {'song': '/'.join([ruta, file])}
            i += 1
            try:
                song = songlist[i]['song']
            except IndexError as error:
                # no estoy seguro de que esta sea la solución, porque el algoritmo solo se da cuenta de que sobran
                # indices una vez que terminó de recorrer la lista, por lo que los pesos pueden quedar corridos.
                # una solución podría ser que en lugar de sonlist, sea un songdict, con la ruta de las canciones
                # como keys, pero eso alteraría el orden. Aunque de todos modos el orden es aleatorio.
                print(error)
            if refresh_weights:
                d.update({'weight': 1})
            else:
                d.update({'weight': songlist[i]['weight']})

            data.append(d)

flagged = []
for i, item in enumerate(songlist):
    song = item['song']
    if not path.exists(song):
        flagged.append(i)

for idx in flagged:
    del songlist[idx]

guardar_json(data, filename)
