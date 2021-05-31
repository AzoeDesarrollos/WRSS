from .constants import ANCHO, ALTO, COLOR_BG
from .group import WidgetGroup
from pygame import display, init


class Renderer:
    contents = None

    @classmethod
    def init(cls):
        init()
        display.set_mode((ANCHO, ALTO))
        cls.contents = WidgetGroup()

    @classmethod
    def add_widget(cls, widget):
        cls.contents.add(widget)

    @classmethod
    def del_widget(cls, widget):
        cls.contents.remove(widget)

    @classmethod
    def update(cls):
        fondo = display.get_surface()
        rect = [fondo.fill(COLOR_BG)]
        rect.extend(cls.contents.draw(fondo))
        display.update(rect)
