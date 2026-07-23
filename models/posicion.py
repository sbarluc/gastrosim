import math

class Posicion:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y


    def mover(self, dx: int, dy: int):
        self.x += dx
        self.y += dy


    def mover_a(self, x: int, y: int):
        self.x = x
        self.y = y


    def distancia_a(self, otra: "Posicion") -> float:
        return math.sqrt((self.x - otra.x) ** 2 + (self.y - otra.y) ** 2)


    def copiar(self) -> "Posicion":
        return Posicion(self.x, self.y)


    def __repr__(self):
        return f"Posicion({self.x}, {self.y})"