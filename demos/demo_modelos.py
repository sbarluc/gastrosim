from models.objeto import Objeto
from models.mesa import Mesa
from models.estanteria import Estanteria
from models.cliente import Cliente
from models.empleado import Empleado
from models.simulador import Simulador
import os

from models.pedido import Pedido
from models.menu import Menu
from data.test_menu import dicc_precios

def test2():
    menu = Menu(dicc_precios)
    mesa = Mesa(1)
    pedido = Pedido(mesa, menu)
    pedido.agregar_item("Cafe con leche")
    pedido.agregar_item("Croissant nutella")
    pedido.quitar_item("Croissant nutella")

def test():  

    servilletero = Objeto("Servilletero")
    menus = list(map(lambda x: Objeto(f"menu[{x}]"), [1,2,3]))
    estanteria = Estanteria([servilletero]+menus)
    mesa1 = Mesa(2)
    mesa2 = Mesa(1)
    seve = Empleado("Seve", "Moz@")
    ana = Cliente("Ana", 25, specs=["Alegre", "Distraida"])
    eduardo = Cliente("Eduardo", 26)
    zoteldo = Cliente("Zoteldo", 28)
    simulador = Simulador()
    simulador.agregar_mesas([mesa1, mesa2])    \
        .agregar_empleados([seve])  \
        .agregar_clientes([ana, eduardo, zoteldo])   \
        .agregar_estanterias([estanteria])   \
    
    mostrar_evento(simulador, "Estado inicial")

    seve.cargar_objeto(estanteria, servilletero)
    for menu in menus:
        seve.cargar_objeto(estanteria, menu)
        mostrar_evento(simulador, f"Seve cargó un {menu} y los menús.")
   

    seve.dejar_objeto(mesa1, servilletero)
    mostrar_evento(simulador, "Seve dejó un servilletero en la mesa 1.")

    seve.asignar_mesa_a_cliente(eduardo, mesa1)
    mostrar_evento(simulador, "Seve asignó la mesa 1 a Eduardo.")

    ana.sentarse_en(mesa1)
    mostrar_evento(simulador, "Ana se sentó en la mesa 1.")

    eduardo.sentarse_en(mesa1)
    mostrar_evento(simulador, "Eduardo se sentó en la mesa 1.")

    seve.asignar_mesa_a_cliente(ana, mesa2)
    mostrar_evento(simulador, "Seve asignó la mesa 2 a Ana.")

    ana.pararse()
    mostrar_evento(simulador, "Ana se paró porque no estaba en la mesa correcta.")

    ana.sentarse_en(mesa2)
    mostrar_evento(simulador, "Ana se sentó en la mesa 2.")

    seve.dejar_objeto(mesa1, menus.pop())
    mostrar_evento(simulador, "Seve dejó un menú en la mesa 1.")

    seve.dejar_objeto(mesa2, menus.pop())
    mostrar_evento(simulador, "Seve dejó un menú en la mesa 2.")

    zoteldo.sentarse_en(mesa2)
    mostrar_evento(simulador, "Zoteldo intenta sentarse en la mesa 2.")

    seve.dejar_objeto(estanteria, menus.pop())
    mostrar_evento(simulador, "Seve devolvió un menú a la estantería.")


def mostrar_evento(simulador, mensaje):
    os.system("cls" if os.name == "nt" else "clear")  # Borra la consola
    print(mensaje)
    print("=" * 60)
    simulador.mostrar_universo()
    input("\n$")