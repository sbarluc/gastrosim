from models.reloj import Reloj

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
    
    def tick(self):
        self.reloj.avanzar()