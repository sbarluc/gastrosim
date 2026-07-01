from models.objeto import Objeto

class Menu(Objeto):

    def __init__(self, dicc_precios):
        super().__init__("Menu")

        self._precios = dicc_precios()

    def precio(self, nombre):
        if nombre in self._precios:
            return self._precios[nombre]
        return None

    def __repr__(self):
        return self._precios