import pygame
from models.tipo_entidad import TipoEntidad


class Renderer:

    def __init__(self, screen):

        self.screen = screen

        self.width = self.screen.get_width()
        self.height = self.screen.get_height()


    def render(self, simulador):

        # limpiar la pantalla
        self.screen.fill((30, 30, 30))

        # dibujar las entidades
        self._render_mesas(simulador)
        self._render_estanterias(simulador)
        self._render_empleados(simulador)
        self._render_clientes(simulador)


    def _render_mesas(self, simulador):

        for mesa in simulador.obtener_entidades(TipoEntidad.MESA):
            
            pygame.draw.rect(
                self.screen,
                (150, 75, 0),
                (mesa.posicion.x, mesa.posicion.y, 40, 40)
            )

            self._render_text(
                mesa.label,
                mesa.posicion.x + 5,
                mesa.posicion.y - 5
            )

    def _render_estanterias(self, simulador):

        for estanteria in simulador.obtener_entidades(
                TipoEntidad.ESTANTERIA):

            pygame.draw.rect(
                self.screen,
                (100, 100, 100),
                (estanteria.posicion.x, estanteria.posicion.y, 50, 25)
            )

            self._render_text(
                estanteria.label,
                estanteria.posicion.x + 5,
                estanteria.posicion.y - 5
            )


    def _render_empleados(self, simulador):

        for empleado in simulador.obtener_entidades(
                TipoEntidad.EMPLEADO):

            pygame.draw.circle(
                self.screen,
                (0, 100, 255),
                (empleado.posicion.x, empleado.posicion.y),
                12
            )

            self._render_text(
                empleado.label,
                empleado.posicion.x + 5,
                empleado.posicion.y - 5
            )


    def _render_clientes(self, simulador):

        for cliente in simulador.obtener_entidades(
                TipoEntidad.CLIENTE):

            pygame.draw.circle(
                self.screen,
                (0, 200, 0),
                (cliente.posicion.x, cliente.posicion.y),
                12
            )

            self._render_text(
                cliente.label,
                cliente.posicion.x + 5,
                cliente.posicion.y - 5
            )

    def _render_text(self, texto, x, y):

        fuente = pygame.font.SysFont("Mono", 14)

        superficie = fuente.render(
            texto,
            True,
            (255, 255, 255)
        )

        self.screen.blit(
            superficie,
            (x, y)
        )