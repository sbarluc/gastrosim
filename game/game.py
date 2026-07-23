from core.simulador import Simulador
from render.renderer import Renderer

class Game:

    def __init__(self):

        self.sim = Simulador()
        self.renderer = Renderer()
        self.running = True


    def run(self):

        while self.running:
            self.manejar_eventos()
            self.sim.tick()
            self.renderer.render(self.sim)