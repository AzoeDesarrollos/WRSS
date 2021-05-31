from frontend.globales import COLOR_TEXT, COLOR_SELECTED, COLOR_BUTTON_BG
from pygame import font, Rect, Surface
from .basewidget import BaseWidget
from lib import render_textrect


class Button(BaseWidget):
    action = None

    def __init__(self, parent, text, method, x, y, w, h):
        super().__init__(parent)
        self.f = font.SysFont('Verdana', 16)
        self.rect = Rect(x, y, w, h)
        self.x, self.y, self.w, self.h = x, y, w, h
        self.img_uns = self.crear(text, self.f, w, h, COLOR_TEXT)
        self.img_sel = self.crear(text, self.f, w, h, COLOR_SELECTED)
        self.image = self.img_uns
        self.action = method

    @staticmethod
    def crear(text, f, w, h, fg):
        img = render_textrect(text, f, w, fg, COLOR_BUTTON_BG, justification=1)
        canvas = Surface((w, h))
        canvas.fill(COLOR_BUTTON_BG)
        canvas.blit(img, img.get_rect(center=canvas.get_rect().center))
        return canvas

    def onmouseover(self):
        super().onmouseover()
        self.select()

    def onmousebuttondown(self, button):
        if button == 1:
            self.action()

    def update(self):
        if self.selected:
            self.image = self.img_sel
        else:
            self.image = self.img_uns

        self.selected = False
