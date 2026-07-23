import pygame
from scenarios.restaruante_demo import crear_restaurante

class GameLoop:

    def __init__(
        self,
        simulador,
        renderer,
        timer,
        event_handler
    ):

        self.simulador = crear_restaurante()
        self.renderer = renderer
        self.timer = timer
        self.event_handler = event_handler

        self.running = True
        self.clock = pygame.time.Clock()


    def run(self):

        while self.running:
            self.clock.tick(60)

            self.running = (
                self.event_handler.handle_events()
            )

            if self.timer.should_tick():
                self.simulador.tick()

            self.renderer.render(
                self.simulador
            )

            pygame.display.flip()


    def stop(self):
        self.running = False