from core.reloj import Reloj
from models.tipo_entidad import TipoEntidad

class Simulador:

    def __init__(self, hora=0, minuto=0):
        self.reloj = Reloj(hora,minuto)
        self.entidades = {}
        self.tareas = []
        
    def agregar_entidad(self, entidad):
        tipo = entidad.tipo
        if tipo not in self.entidades:
            self.entidades[tipo] = []
        if entidad not in self.entidades[tipo]:
            self.entidades[tipo].append(entidad)
        
    def quitar_entidad(self, entidad):
        tipo = entidad.tipo
        if (tipo in self.entidades) and (entidad in self.entidades[tipo]):
            self.entidades[tipo].remove(entidad)
    
    def obtener_entidades(self, tipo):
        return self.entidades.get(tipo, [])

    def agregar_tarea(self, tarea):
        if not tarea in self.tareas:
            self.tareas.append(tarea)
            return True
        return False
    
    def quitar_tarea(self, tarea):
        if tarea in self.tareas:
            self.tareas.remove(tarea)
            return True
        return False
    
    def lista_entidades(self):
        return [entidad for v in self.entidades.values() for entidad in v]

    def buscar_mesa_libre(self):
        for mesa in self.obtener_entidades(TipoEntidad.MESA):
            if not mesa.esta_ocupada():
                return mesa

    def tick(self):
        self.reloj.avanzar()
        for entidad in self.lista_entidades():
            entidad.tick(self)
            