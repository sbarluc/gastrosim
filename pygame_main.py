import pygame
from core.simulador import Simulador
from game.game_loop import GameLoop
from game.timer import Timer
from render.renderer import Renderer
from game.event_handler import EventHandler

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Gastrosim VG1")

sim = Simulador(17,0)
renderer = Renderer(screen)
timer = Timer()
event_handler = EventHandler(timer, renderer)

game = GameLoop(
    sim,
    renderer,
    timer,
    event_handler
)

game.run()

pygame.quit()