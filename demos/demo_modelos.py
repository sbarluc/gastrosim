from core.simulador import Simulador
from models.cliente import Cliente
from models.empleado import Empleado
from models.item_pedido import ItemPedido
from models.mesa import Mesa
from models.estanteria import Estanteria
from models.menu import Menu
from data.test_menu import dicc_precios
from models.tipo_entidad import TipoEntidad
from models.estado_cliente import EstadoCliente
import os

# -------------------------------------------------------------------------
# DEMO DE SIMULADOR
# -------------------------------------------------------------------------

def mostrar_evento(sim, mensaje=None):
    os.system("cls" if os.name == "nt" else "clear")

    print("="*60)
    print(f"{sim.reloj} {f'| {mensaje}' if mensaje else ''}")
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
    sim.agregar_entidad(Mesa(2))
    sim.agregar_entidad(Empleado("Seve", "Mozo"))
    estanteria_1 = sim.obtener_entidades(TipoEntidad.ESTANTERIA)[0]
    mesa_1 = sim.obtener_entidades(TipoEntidad.MESA)[0]
    mesa_2 = sim.obtener_entidades(TipoEntidad.MESA)[1]
    empleado_1 = sim.obtener_entidades(TipoEntidad.EMPLEADO)[0]

    for _ in range(5):
        sim.tick()
        mostrar_evento(sim, "Abriendo local")
    
    sim.agregar_entidad(Cliente("Ana", 25))
    sim.agregar_entidad(Cliente("Damian", 23))
    [cliente_1, cliente_2] = sim.obtener_entidades(TipoEntidad.CLIENTE)
    sim.tick()
    mostrar_evento(sim, f"Agrega: {cliente_1} y {cliente_2}")

    for _ in range(5):
        sim.tick()
        mostrar_evento(sim)

    cliente_1.asignar_mesa(mesa_1)
    sim.tick()
    mostrar_evento(sim)

    while(not cliente_2.tiene_estado(EstadoCliente.SENTADO)):
        sim.tick()
        mostrar_evento(sim)

    for _ in range(5):
        sim.tick()
        mostrar_evento(sim)

    cliente_2.asignar_mesa(mesa_1)
    sim.tick()
    mostrar_evento(sim)

    for _ in range(5):
        sim.tick()
        mostrar_evento(sim)

    empleado_1.crear_pedido(mesa_1)
    for cliente in mesa_1.clientes_sentados():
        items = cliente.tomar_pedido()
        for item in items:
            empleado_1._pedidos[mesa_1.id].agregar_item(item)
        sim.tick()
        mostrar_evento(sim, f"{empleado_1} toma el pedido de {cliente}")

    # menu_1 = estanteria_1.obtener_objeto("Menu")
    # empleado_1.cargar_objeto_desde(menu_1, estanteria_1)
    # menu_2 = estanteria_1.obtener_objeto("Menu")
    # empleado_1.cargar_objeto_desde(menu_2, estanteria_1)
    # sim.tick()
    # mostrar_evento(sim, f"{empleado_1} carga {menu_1} y {menu_2} de {estanteria_1}")

    # empleado_1.dejar_objeto_en(menu_1, mesa_1)
    # empleado_1.dejar_objeto_en(menu_2, mesa_1)
    # sim.tick()
    # mostrar_evento(sim, f"{empleado_1} deja {menu_1} y {menu_2} en {mesa_1}")

    # empleado_1.pedidos()[mesa_1.id].limpiar_items()
    # cliente_1.pedido().limpiar_items()
    # cliente_2.pedido().limpiar_items()
    # sim.tick()
    # mostrar_evento(sim, f"{empleado_1} limpia el pedido de {mesa_1}\n{cliente_1} y {cliente_2} limpian sus pedidos")
    # # LIMPIAN LOS PEDIDOS PORQUE EL TIPO DE ITEMPEDIDO NO ERA IMPORTANTE

    # for _ in range(4):
    #     sim.tick()
    #     mostrar_evento(sim, f"{cliente_1} esta viendo {menu_1} y {cliente_2} esta viendo {menu_2}")

    
    # item_coca_1 = ItemPedido("Coca cola", 2500)
    # item_coca_2 = ItemPedido("Coca cola", 2500)
    # cliente_1.pedido().agregar_item(item_coca_1)
    # cliente_1.pedido().preparar_item_para_pedir(item_coca_1)
    # cliente_1.pedido().agregar_item(item_coca_2)
    # cliente_1.pedido().preparar_item_para_pedir(item_coca_2)
    # for _ in range(1):
    #     sim.tick()
    #     mostrar_evento(sim, f"{cliente_1} pide {item_coca_1} y {cliente_2} pide {item_coca_2}")

    # item_cesar = ItemPedido.desde_menu(menu_1, "Ensalada César con pollo")
    # cliente_1.pedido().agregar_item(item_cesar)
    # cliente_1.pedido().preparar_item_para_pedir(item_cesar)
    # item_lomo = ItemPedido.desde_menu(menu_1, "Lomo saltado")
    # cliente_2.pedido().agregar_item(item_lomo)
    # cliente_2.pedido().preparar_item_para_pedir(item_lomo)
    # sim.tick()
    # mostrar_evento(sim, f"Ana y Damian ya saben que van a pedir")

    # empleado_1.crear_pedido(mesa_1)
    # empleado_1.tomar_pedido_a_mesa(mesa_1)
    # sim.tick()
    # mostrar_evento(sim, f"{empleado_1} toma el pedido de la mesa 1")


if __name__ == "__main__":
    demo_completa()