from pygame.sprite import Sprite


class BaseWidget(Sprite):
    selected = False
    enabled = True
    _has_mouseover = False

    def __init__(self, parent=None):
        super().__init__()
        if parent is not None:
            self.parent = parent
            self.layer = self.parent.layer + 1

    # event-related methods
    def onmousebuttondown(self, button):
        if button == 1:
            return self

    def onmousebuttonup(self, button):
        pass

    def onmousemotion(self, key):
        pass

    def onmouseover(self):
        self._has_mouseover = True

    def onkeydown(self, key):
        pass

    def onkeyup(self, key):
        pass

    # select-related methods
    def select(self):
        self.selected = True

    def deselect(self):
        self.selected = False

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def update(self):
        pass
