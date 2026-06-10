class Objeto:
    def __init__(self, nombre, objetos=[]):
        self.nombre = nombre
        self.objetos = objetos
    
    def agregar_objeto(self, objeto):
        self.objetos.append(objeto)

    def quitar_objeto(self, objeto):
        if objeto in self.objetos:
            self.objetos.remove(objeto)
            return objeto
        return None