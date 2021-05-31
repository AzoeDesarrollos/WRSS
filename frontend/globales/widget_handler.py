from pygame import QUIT, KEYDOWN, KEYUP, MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION
from pygame import event, quit, mouse, time
from .group import WidgetGroup
from pygame import K_ESCAPE
from sys import exit


class WidgetHandler:
    widgets = None
    fps = None

    @classmethod
    def init(cls):
        cls.widgets = WidgetGroup()
        cls.fps = time.Clock()

    @classmethod
    def add_widget(cls, widget):
        cls.widgets.add(widget)

    @classmethod
    def del_widget(cls, widget):
        cls.widgets.remove(widget)

    @classmethod
    def update(cls):
        cls.fps.tick(60)
        events = event.get([QUIT, KEYDOWN, KEYUP, MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION])
        event.clear()
        for e in events:
            if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
                quit()
                exit()
            elif e.type == MOUSEBUTTONDOWN:
                widgets = cls.widgets.get_widgets_at(e.pos)
                for widget in widgets:
                    cls.selected = widget.onmousebuttondown(e.button)

            elif e.type == MOUSEBUTTONUP:
                widgets = cls.widgets.get_widgets_at(e.pos)
                for widget in widgets:
                    widget.onmousebuttonup(e.button)

            elif e.type == MOUSEMOTION:
                pass
            elif e.type == KEYDOWN:
                pass
            elif e.type == KEYUP:
                pass

        pos = mouse.get_pos()
        for widget in cls.widgets.widgets():
            if widget.rect.collidepoint(pos):
                widget.onmouseover()

        cls.widgets.update()
