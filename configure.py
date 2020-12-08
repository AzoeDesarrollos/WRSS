from util import abrir_json, guardar_json
from importlib import import_module
from constantes import refresh, refresh_weights

config = abrir_json('config.json')
songlist = abrir_json('songlist.json')

opciones = [
    'Actualizar la cantidad de canciones',
    'Cambiar la ruta base de las canciones',
    'Cambiar los pesos de las canciones',
    'Restaurar los pesos de las canciones',
    'Actualizar la lista de canciones',
    'Conservar la lista de reproducción',
    'Cambiar el nombre por defecto de las listas',
    'Salir'
]

while True:
    key, value = None, None
    for i, opcion in enumerate(opciones):
        print(i, ': ', opcion, sep='')
    print('\nElija una opción, ¿que desea hacer?')
    op = int(input('> '))
    opcion = opciones[op] if 0 <= op <= len(opciones)-1 else None

    if opcion == 'Actualizar la cantidad de canciones':
        value = int(input('\n¿Cuantas canciones? '))
        key = 'songs'

    elif opcion == 'Cambiar la ruta base de las canciones':
        print('\nIngrese la nueva ruta')
        value = input('> ')
        key = 'root'

    elif opcion == 'Cambiar los pesos de las canciones':
        pass

    elif opcion == 'Restaurar los pesos de las canciones':
        r = input('\n¿Desea restaurar los pesos de las canciones? ').lower().startswith('s')
        refresh(r)
        import_module('update_songlist')

    elif opcion == 'Actualizar la lista de canciones':
        go = True
        if refresh_weights:
            print('\nAlerta: Esta acción restablecerá los pesos de las canciones')
            go = input('¿Desea continuar?').lower().startswith('s')

        if go:
            import_module('update_songlist')

    elif opcion == 'Conservar la lista de reproducción':
        value = input('\n¿Desea conservar las listas de reproducción generadas? ').lower().startswith('s')
        key = 'keeppls'

    elif opcion == 'Cambiar el nombre por defecto de las listas':
        print('\nIngrese el nuevo nombre por defecto')
        value = input('> ')+'.pls'
        key = 'default'

    else:          # Salir
        break

    if key is not None and value is not None:
        config[key] = value
        guardar_json(config, 'config.json')
