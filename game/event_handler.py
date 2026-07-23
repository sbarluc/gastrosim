import pygame


class EventHandler:

    def __init__(self, timer, renderer):

        self.timer = timer
        self.renderer = renderer


    def handle_events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return False


            if event.type == pygame.KEYDOWN:
                self._handle_key_down(event.key)


            if event.type == pygame.MOUSEBUTTONDOWN:
                self._handle_mouse(event)

        return True


    def _handle_key_down(self, key):

        # PAUSA
        if key == pygame.K_SPACE:
            self.timer.toggle_pause()

        # VELOCIDAD x1
        elif key == pygame.K_1:
            self.timer.set_speed(1)

        # VELOCIDAD x2
        elif key == pygame.K_2:
            self.timer.set_speed(2)

        # VELOCIDAD x4
        elif key == pygame.K_3:
            self.timer.set_speed(4)

        # ZOOM +
        elif key == pygame.K_q:
            self.renderer.camera.zoom_in()

        # ZOOM -
        elif key == pygame.K_e:
            self.renderer.camera.zoom_out()


    def _handle_mouse(self, event):
        # rueda del mouse

        if event.button == 4:
            self.renderer.camera.zoom_in()


        elif event.button == 5:
            self.renderer.camera.zoom_out()