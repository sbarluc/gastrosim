import time

class Timer:

    def __init__(self):
        self.speed = 1
        self.last_tick = time.time()


    def should_tick(self):
        now = time.time()

        if now - self.last_tick >= 1 / self.speed:
            self.last_tick = now
            return True

        return False