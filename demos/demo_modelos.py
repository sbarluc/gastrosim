from models.objeto import Objeto
from models.mesa import Mesa
from models.estanteria import Estanteria
from models.cliente import Cliente
from models.empleado import Empleado
from models.simulador import Simulador
from models.item_pedido import ItemPedido
from models.pedido import Pedido
from models.menu import Menu
from data.test_menu import dicc_precios
import os

# -------------------------------------------------------------------------
# DEMO DE INTEGRACIÓN (FUSIÓN DE TODOS TESTS)
# -------------------------------------------------------------------------

def mostrar_evento(simulador, mensaje):
    os.system("cls" if os.name == "nt" else "clear")  # Borra la consola

    print("=" * 60)
    print(f"EVENTO: {mensaje}")
    print("=" * 60)
    print("\n")

    simulador.mostrar_universo()
    
    print("\n--- DETALLES DEL ESTADO ACTUAL ---")
    
    for emp in simulador.empleados():
        if emp.cantidad_pedidos() > 0:
            print(f"Empleado {emp.nombre} tiene {emp.cantidad_pedidos()} pedido(s) activos.")
            for id, pedido in emp.pedidos().items():
                print(f"  -> Mesa {id}: ${pedido.valor()} ({pedido.cantidad_items()} ítems)")
    
    for est in simulador.estanterias():
        if est.cantidad_objetos() > 0:
            objetos_str = ", ".join([obj.nombre for obj in est.objetos()])
            print(f"Estantería {est.id} contiene: {objetos_str}")
        else:
            print(f"Estantería {est.id} vacía.")

    input("\nPresiona Enter para continuar...")

def demo_completa():
    
    # --- 1. CONFIGURACIÓN INICIAL (CREACIÓN DE OBJETOS) ---
    print("Inicializando el Restaurante...")
    
    # Objetos y Menús
    servilletero = Objeto("Servilletero", peso=1)
    cenicero = Objeto("Cenicero", peso=2)
    menu = Menu(dicc_precios)
    
    # Estanterías (probando capacidad de los tests iniciales)
    estanteria_principal = Estanteria([servilletero, cenicero], carga_max=10)
    estanteria_vacia = Estanteria(carga_max=5)

    # Mesas
    mesa_1 = Mesa(2)  # Mesa para 2 personas
    mesa_2 = Mesa(3)  # Mesa para 3 personas

    # Personas
    seve = Empleado("Seve", "Mozo")
    ana = Cliente("Ana", 25)
    eduardo = Cliente("Eduardo", 30)
    laura = Cliente("Laura", 28)

    # Simulador
    simulador = Simulador()
    simulador.agregar_mesas([mesa_1, mesa_2]) \
             .agregar_empleados([seve]) \
             .agregar_clientes([ana, eduardo, laura]) \
             .agregar_estanterias([estanteria_principal, estanteria_vacia])

    mostrar_evento(simulador, "Restaurante abierto. Estado inicial.")

    # --- 2. INTERACCIÓN CON ESTANTERÍAS Y OBJETOS ---
    
    # El empleado toma objetos de la estantería
    seve.cargar_objeto(estanteria_principal, servilletero)
    mostrar_evento(simulador, "Seve tomó el servilletero de la estantería.")

    seve.dejar_objeto(mesa_1, servilletero)
    mostrar_evento(simulador, "Seve dejó el servilletero en la Mesa 1.")

    seve.cargar_objeto(estanteria_principal, cenicero)
    mostrar_evento(simulador, "Seve tomó un cenicero y lo dejó en la Mesa 2.")

    seve.dejar_objeto(mesa_2, cenicero)
    mostrar_evento(simulador, "Seve dejó el cenicero en la Mesa 2.")

    # --- 3. ASIGNACIÓN DE MESAS Y CLIENTES ---

    seve.asignar_mesa_a_cliente(ana, mesa_1)
    mostrar_evento(simulador, "Seve asignó la Mesa 1 a Ana")
    
    seve.asignar_mesa_a_cliente(eduardo, mesa_1)
    mostrar_evento(simulador, "Seve asignó la Mesa 1 a Eduardo.")

    ana.sentarse_en(mesa_1)
    mostrar_evento(simulador, "Ana se sentó en la Mesa 1.")

    eduardo.sentarse_en(mesa_1)
    mostrar_evento(simulador, "Eduardo se sentó en la Mesa 1.")

    laura.sentarse_en(mesa_2)
    mostrar_evento(simulador, "Laura se sentó sola en la Mesa 2 sin que le fuera asignada.")

    seve.asignar_mesa_a_cliente(laura, mesa_2)
    mostrar_evento(simulador, "Seve asignó la Mesa 2 a Laura.")

    # --- 4. CREACIÓN DE PEDIDOS (FUSIÓN CON TESTS DE PEDIDOS) ---

    # Los clientes eligen ítems del menú
    cafe = ItemPedido.desde_menu(menu, "Cafe con leche")
    croissant = ItemPedido.desde_menu(menu, "Croissant nutella")
    salmon = ItemPedido.desde_menu(menu, "Salmón a la plancha")
    pizza = ItemPedido.desde_menu(menu, "Pizza margarita")

    # Ana y Eduardo agregan ítems a su lista personal
    ana.agregar_item(cafe)
    ana.agregar_item(croissant)
    eduardo.agregar_item(salmon)
    
    # Preparan los ítems para pedir (estado intermedio)
    ana.preparar_item_para_pedir(cafe)
    eduardo.preparar_item_para_pedir(salmon)
    mostrar_evento(simulador, "Ana y Eduardo armaron su pedido. Ana pide Café, Eduardo pide Salmón.")

    # El empleado toma el pedido de la Mesa 1
    seve.crear_pedido(mesa_1)
    seve.tomar_pedido_a_mesa(mesa_1)
    mostrar_evento(simulador, "Seve tomó el pedido de la Mesa 1 (Solo los ítems marcados como 'para pedir').")

    # Laura pide en la Mesa 2
    laura.agregar_item(pizza)
    laura.preparar_item_para_pedir(pizza)
    seve.crear_pedido(mesa_2)
    seve.tomar_pedido_a_mesa(mesa_2)
    mostrar_evento(simulador, "Laura pidió una Pizza Margarita en la Mesa 2.")

    # --- 5. ENTREGA Y CIERRE DE PEDIDOS ---

    # Seve entrega los platos (simulamos que pasó el tiempo de cocción)
    seve.entregar_item_de_pedido(mesa_1, salmon)
    seve.entregar_item_de_pedido(mesa_1, cafe)
    mostrar_evento(simulador, "Seve entregó el Salmón y el Café en la Mesa 1.")

    seve.entregar_item_de_pedido(mesa_2, pizza)
    mostrar_evento(simulador, "Seve entregó la Pizza en la Mesa 2.")

    # Se cierran los pedidos (los clientes pagan o se van)
    seve.cerrar_pedido(mesa_1)
    mostrar_evento(simulador, "Seve cerró el pedido de la Mesa 1 (Eduardo y Ana se fueron).")

    # Ana se desasigna su mesa
    ana.desasignar_mesa()
    mostrar_evento(simulador, "Ana abandonó su mesa.")

    # Eduardo se desasigna su mesa
    eduardo.desasignar_mesa()
    mostrar_evento(simulador, "Eduardo abandonó su mesa.")
    
    # Ana se para
    ana.pararse()
    mostrar_evento(simulador, "Ana se paró.")

    # Eduardo se para
    eduardo.pararse()
    mostrar_evento(simulador, "Eduardo se paró y abandonó su mesa.")

    # Ana se fue del restaurante
    simulador.quitar_entidad(ana)
    mostrar_evento(simulador, "Ana se fue.")

    # Eduardo se fue del restaurante
    simulador.quitar_entidad(eduardo)
    mostrar_evento(simulador, "Eduardo se fue.")


    del ana
    del eduardo

    # La mesa queda vacía, Seve la limpia y devuelve los objetos
    mesa_1.limpiar()
    mostrar_evento(simulador, "La Mesa 1 fue limpiada.")

    # --- FINAL ---
    print("\n¡Demo finalizada! Todo OK.")
    print(f"Resumen final de ganancias: ${seve.total_pedidos()}")

if __name__ == "__main__":
    demo_completa()