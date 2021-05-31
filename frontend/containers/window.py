from frontend.globales import ANCHO, ALTO, COLOR_BG, COLOR_TEXT
from frontend.globales import Renderer, WidgetHandler
from backend.util import abrir_json, guardar_json
from backend.eventhandler import EventHandler
from ..widgets import BaseWidget, Button
from pygame import Rect, font, Surface
from importlib import import_module

config = abrir_json('config.json')
songlist = abrir_json('songlist.json')


class Window(BaseWidget):
    layer = 0

    def __init__(self):
        super().__init__()
        self.rect = Rect(0, 0, ANCHO, ALTO)
        self.image = Surface(self.rect.size)
        self.image.fill(COLOR_BG)
        self.botones = []
        f = font.SysFont('Verdana', 18, bold=True)

        opciones = [
            'Generar una lista de reproducción.',
            'Actualizar la cantidad de canciones.',
            'Cambiar la ruta base de las canciones.',
            'Cambiar los pesos de las canciones.',
            'Restaurar los pesos de las canciones.',
            'Actualizar la lista de canciones.',
            'Conservar la lista de reproducción.',
            'Cambiar el nombre por defecto de las listas.',
            'Salir'
        ]

        methods = [
            lambda: self.configure(opciones[0]),
            lambda: self.configure(opciones[1]),
            lambda: self.configure(opciones[2]),
            lambda: self.configure(opciones[3]),
            lambda: self.configure(opciones[4]),
            lambda: self.configure(opciones[5]),
            lambda: self.configure(opciones[6]),
            lambda: self.configure(opciones[7]),
            lambda: self.configure(opciones[8]),
        ]

        w, h = 200, 80
        d = 5
        for i, text in enumerate(opciones):
            x = (i % 3 * w)
            y = (i // 3 * h)
            btn = Button(self, text, methods[i], (x + d * (i % 3)) + 15, y + d * (i // 3) + 50, w, h)
            self.botones.append(btn)
            Renderer.add_widget(btn)
            WidgetHandler.add_widget(btn)

        render = f.render('Elija una opción, ¿qué desea hacer?', 1, COLOR_TEXT)
        render_rect = render.get_rect()
        self.image.blit(render, render_rect)
        Renderer.add_widget(self)
        WidgetHandler.add_widget(self)

    @staticmethod
    def configure(opcion):
        key, value = None, None
        if opcion == 'Generar una lista de reproducción.':
            import_module('lib.write_and_play')
            import_module('backend.rate')

        elif opcion == 'Actualizar la cantidad de canciones.':
            key = 'songs'

        elif opcion == 'Cambiar la ruta base de las canciones':
            print('La ruta actual es: {}'.format(config['root']))
            print('\nIngrese la nueva ruta')
            key = 'root'

        elif opcion == 'Cambiar los pesos de las canciones.':
            print('Ésta operación aun no se encuentra disponible')
            print(len(songlist))

        elif opcion == 'Restaurar los pesos de las canciones.':
            key = 'weights'
            import_module('backend.update_songlist')

        elif opcion == 'Actualizar la lista de canciones.':
            if config['weights']:
                print('\nAlerta: Esta acción restablecerá los pesos de las canciones')
                import_module('backend.update_songlist')

        elif opcion == 'Conservar la lista de reproducción':
            key = 'keeppls'

        elif opcion == 'Cambiar el nombre por defecto de las listas':
            print('\nIngrese el nuevo nombre por defecto')
            key = 'default'

        elif opcion == 'Salir':
            EventHandler.trigger('salir', 'Window', {'texto': 'normal'})

        if key is not None and value is not None:
            config[key] = value
            guardar_json(config, 'config.json')
