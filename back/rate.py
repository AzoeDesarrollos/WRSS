from .util import abrir_json, guardar_json
import os

chosen = abrir_json('chosen.json')
songlist = abrir_json('songlist.json')
songnames = [song['name'] for song in songlist]

while True:
    os.system(['clear', 'cls'][os.name == 'nt'])
    print('Estás escuchando estas canciones:')
    for i, name in enumerate(chosen):
        idx = songnames.index(name)
        fav = ' (F)' if songlist[idx].get('Favourite', False) else ''
        print(i, name, sep=': ', end=fav+'\n')

    if input('\n¿Te gustaría calificar algunas de estas como tus favoritas? ').lower().startswith('s'):
        op = int(input('Canción Favorita: '))
        if 0 <= op <= len(chosen):
            idx = songnames.index(chosen[op])
            if not songlist[idx].get('Favourite', False):
                songlist[idx]['Favourite'] = True
            else:
                print('\nEsta canción ya está señalada como una de tus favoritas')
                input('<Presiona Enter para continuar>')

    else:
        guardar_json(songlist, 'songlist.json')
        os.remove('config/chosen.json')
        os.system(['clear', 'cls'][os.name == 'nt'])
        break
