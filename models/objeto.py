class Objeto:
    def __init__(self, nombre, objetos=None):
        self.nombre = nombre
        self.objetos = objetos if objetos is not None else []
    
    def agregar_objeto(self, objeto):
        self.objetos.append(objeto)

    def quitar_objeto(self, objeto):
        if objeto in self.objetos:
            self.objetos.remove(objeto)
            return objeto
        return None