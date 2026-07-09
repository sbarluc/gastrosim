from core.simulador import Simulador
from models.cliente import Cliente
from models.empleado import Empleado
from models.item_pedido import ItemPedido
from models.mesa import Mesa
from models.estanteria import Estanteria
from models.menu import Menu
from data.test_menu import dicc_precios
from models.tipo_entidad import TipoEntidad
import os

# -------------------------------------------------------------------------
# DEMO DE SIMULADOR
# -------------------------------------------------------------------------

def mostrar_evento(sim, mensaje):
    os.system("cls" if os.name == "nt" else "clear")

    print("="*60)
    print(f"{sim.reloj} | {mensaje}")
    print("=" * 60)

    for tipo in sim.entidades:
        print(f"\n{tipo.name}S:")
        for entidad in sim.entidades[tipo]:
            print(f"{entidad.info()}")

    input("\nPresiona Enter para continuar...")

def demo_completa():
    sim = Simulador(hora=19, minuto=0)

    sim.agregar_entidad(Estanteria([Menu(dicc_precios), Menu(dicc_precios), Menu(dicc_precios), Menu(dicc_precios)]))
    sim.agregar_entidad(Mesa(2))
    sim.agregar_entidad(Empleado("Seve", "Mozo"))
    estanteria_1 = sim.obtener_entidades(TipoEntidad.ESTANTERIA)[0]
    mesa_1 = sim.obtener_entidades(TipoEntidad.MESA)[0]
    empleado_seve = sim.obtener_entidades(TipoEntidad.EMPLEADO)[0]
    mostrar_evento(sim, "Seve abre el local")
    for _ in range(5):
        sim.tick()
        mostrar_evento(sim, "Seve abre el local")
    
    sim.agregar_entidad(Cliente("Ana", 25))
    sim.agregar_entidad(Cliente("Damian", 23))
    [cliente_ana, cliente_damian] = sim.obtener_entidades(TipoEntidad.CLIENTE)
    sim.tick()
    mostrar_evento(sim, "Ana y Damian llegan al local")

    cliente_ana.asignar_mesa(mesa_1)
    cliente_damian.asignar_mesa(mesa_1)
    sim.tick()
    mostrar_evento(sim, "Se le asigna a Ana y Damian la mesa 1")


    cliente_ana.sentarse_en_mesa(mesa_1)
    cliente_damian.sentarse_en_mesa(mesa_1)
    for _ in range(3):
        sim.tick()
        mostrar_evento(sim, "Ana y Damian se sientan en la mesa 1")


    item_menu_1, item_menu_2 = ItemPedido("Menú"), ItemPedido("Menú")
    ### Esto lo va a hacer internamente cada cliente en su metodo tick()
    cliente_ana._pedido.agregar_item(item_menu_1)
    cliente_ana._pedido.buscar_item(item_menu_1).preparar_para_pedir()
    cliente_damian._pedido.agregar_item(item_menu_2)
    cliente_damian._pedido.buscar_item(item_menu_2).preparar_para_pedir()
    sim.tick()
    mostrar_evento(sim, "Ana y Damian piden menus")

    item_agua = ItemPedido("Vaso de agua")
    cliente_ana._pedido.agregar_item(item_agua)
    sim.tick()
    mostrar_evento(sim, "Damian piensa en un vaso de agua")

    ### Esto lo va a hacer internamente el empleado en su metodo tick()
    empleado_seve.crear_pedido(mesa_1)
    for cliente in mesa_1.clientes_sentados():
        items = cliente.tomar_pedido()
        for item in items:
            empleado_seve._pedidos[mesa_1.id].agregar_item(item)
        sim.tick()
        mostrar_evento(sim, f"Seve toma el pedido de {cliente.nombre}")
        


    # menu_1 = estanteria_1.obtener("Menu")
    # empleado_seve.cargar_objeto(estanteria_1, menu_1)
    # menu_2 = estanteria_1.obtener("Menu")
    # empleado_seve.cargar_objeto(estanteria_1, menu_2)
    # sim.tick()
    # mostrar_evento(sim, "Seve carga dos menus de la estanteria")

    # empleado_seve.dejar_objeto(mesa_1, menu_1)
    # empleado_seve.dejar_objeto(mesa_1, menu_2)
    # sim.tick()
    # mostrar_evento(sim, "Seve deja dos menus en la mesa 1")

    # empleado_seve.limpiar_items_de_pedido(mesa_1)
    # cliente_ana.quitar_item(item_menu_1)
    # cliente_damian.quitar_item(item_menu_2)
    # for _ in range(5):
    #     sim.tick()
    #     mostrar_evento(sim, "Ana y Damian están viendo el menu")

    # item_cesar = ItemPedido.desde_menu(menu_1, "Ensalada César con pollo")
    # cliente_ana.agregar_item(item_cesar)
    # cliente_ana.preparar_item_para_pedir(item_cesar)
    # item_lomo = ItemPedido.desde_menu(menu_1, "Lomo saltado")
    # cliente_damian.agregar_item(item_lomo)
    # cliente_damian.preparar_item_para_pedir(item_lomo)
    # sim.tick()
    # mostrar_evento(sim, "Ana y Damian ya saben que van a pedir")
    
    # empleado_seve.crear_pedido(mesa_1)
    # empleado_seve.tomar_pedido_a_mesa(mesa_1)
    # sim.tick()
    # mostrar_evento(sim, "Seve toma el pedido de la mesa 1")


if __name__ == "__main__":
    demo_completa()