from core.simulador import Simulador
from models.mesa import Mesa
from models.cliente import Cliente
from models.empleado import Empleado
from models.estanteria import Estanteria
from models.menu import Menu

from data.test_menu import dicc_precios

def crear_restaurante():
    
    simulador = Simulador(10,0)

    # mesas
    mesa1 = Mesa(4)
    mesa1.posicion.mover_a(200, 200)
    mesa2 = Mesa(2)
    mesa2.posicion.mover_a(400, 200)

    # empleados
    empleado1 = Empleado("Juan", "Mozo")
    empleado1.posicion.mover_a(400, 400)

    # clientes
    cliente1 = Cliente("Pedro", 20)
    cliente1.posicion.mover_a(100, 100)

    # estanterias
    estanteria1 = Estanteria([Menu(dicc_precios), Menu(dicc_precios), Menu(dicc_precios), Menu(dicc_precios)])
    estanteria1.posicion.mover_a(0, 600)

    # regsitro
    simulador.agregar_entidad(mesa1)
    simulador.agregar_entidad(mesa2)
    simulador.agregar_entidad(empleado1)
    simulador.agregar_entidad(cliente1)
    simulador.agregar_entidad(estanteria1)

    return simulador