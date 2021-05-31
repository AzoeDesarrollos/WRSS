from frontend.globales import WidgetHandler, Renderer
from backend.eventhandler import EventHandler
from frontend.containers import Window

Renderer.init()
WidgetHandler.init()

Window()

while True:
    EventHandler.process()
    WidgetHandler.update()
    Renderer.update()
