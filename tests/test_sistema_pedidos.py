# import pytest # pyright: ignore[reportMissingImports]
# from models.mesa import Mesa
# from models.menu import Menu
# from models.item_pedido import ItemPedido
# from models.cliente import Cliente
# from models.empleado import Empleado
# from data.test_menu import dicc_precios

# @pytest.fixture
# def menu():
#     return Menu(dicc_precios)
# @pytest.fixture
# def mesa_1():
#     return Mesa(2)
# @pytest.fixture
# def mesa_2():
#     return Mesa(3)
# @pytest.fixture
# def empleado():
#     return Empleado("Juan", "Mozo")
# @pytest.fixture
# def cliente_ana():
#     return Cliente("Ana", 25)
# @pytest.fixture
# def cliente_carlos():
#     return Cliente("Carlos", 30)
# @pytest.fixture
# def cliente_laura():
#     return Cliente("Laura", 28)

# # ==================== TESTS DE CLIENTE Y SU PEDIDO ====================

# def test_cliente_empieza_sin_items(cliente_ana):
#     assert cliente_ana.cantidad_items() == 0
#     assert cliente_ana.items() == []


# def test_cliente_agregar_item(cliente_ana):
#     item = ItemPedido("Cenicero")
#     assert cliente_ana.agregar_item(item)
#     assert cliente_ana.cantidad_items() == 1
#     assert cliente_ana.valor_total_items() == 0


# def test_cliente_agregar_item_desde_menu(cliente_ana, menu):
#     item = ItemPedido.desde_menu(menu, "Cheesecake frutos rojos")
#     assert cliente_ana.agregar_item(item)
#     assert cliente_ana.cantidad_items() == 1
#     assert cliente_ana.valor_total_items() == 5000


# def test_cliente_agregar_multiple_items(cliente_ana, menu):
#     cenicero = ItemPedido("Cenicero")
#     cafe_con_leche = ItemPedido.desde_menu(menu, "Cafe con leche")
#     cheesecake = ItemPedido.desde_menu(menu, "Cheesecake frutos rojos")
    
#     assert cliente_ana.agregar_item(cheesecake)
#     assert cliente_ana.agregar_item(cenicero)
#     assert cliente_ana.agregar_item(cafe_con_leche)
    
#     assert cliente_ana.cantidad_items() == 3
#     assert cliente_ana.valor_total_items() == 8000


# def test_cliente_agregar_item_inexistente(cliente_ana, menu):
#     sanguche_de_miga = ItemPedido.desde_menu(menu, "Sanguche de miga")
#     assert not cliente_ana.agregar_item(sanguche_de_miga)
#     assert cliente_ana.cantidad_items() == 0
#     assert cliente_ana.valor_total_items() == 0


# def test_cliente_agregar_item_duplicado(cliente_ana):
#     item = ItemPedido("Cenicero")
#     assert cliente_ana.agregar_item(item)
#     assert not cliente_ana.agregar_item(item)
#     assert cliente_ana.cantidad_items() == 1


# def test_cliente_quitar_item(cliente_ana, menu):
#     cafe_con_leche = ItemPedido.desde_menu(menu, "Cafe con leche")
#     cheesecake = ItemPedido.desde_menu(menu, "Cheesecake frutos rojos")
    
#     cliente_ana.agregar_item(cafe_con_leche)
#     cliente_ana.agregar_item(cheesecake)
    
#     assert cliente_ana.quitar_item(cheesecake)
#     assert cliente_ana.cantidad_items() == 1
#     assert cliente_ana.valor_total_items() == 3000


# def test_cliente_quitar_item_inexistente(cliente_ana, menu):
#     cafe_con_leche = ItemPedido.desde_menu(menu, "Cafe con leche")
#     cheesecake = ItemPedido.desde_menu(menu, "Cheesecake frutos rojos")
    
#     cliente_ana.agregar_item(cafe_con_leche)
    
#     assert not cliente_ana.quitar_item(cheesecake)
#     assert cliente_ana.cantidad_items() == 1


# def test_cliente_preparar_item_para_pedir(cliente_ana):
#     item = ItemPedido("Cenicero")
#     cliente_ana.agregar_item(item)
    
#     assert not cliente_ana.items()[0].esta_para_pedir()
    
#     cliente_ana.preparar_item_para_pedir(item)
#     assert cliente_ana.items()[0].esta_para_pedir()


# def test_cliente_limpiar_items(cliente_ana, menu):
#     cafe = ItemPedido.desde_menu(menu, "Cafe con leche")
#     cheesecake = ItemPedido.desde_menu(menu, "Cheesecake frutos rojos")
    
#     cliente_ana.agregar_item(cafe)
#     cliente_ana.agregar_item(cheesecake)
#     assert cliente_ana.cantidad_items() == 2
    
#     cliente_ana.limpiar_items()
#     assert cliente_ana.cantidad_items() == 0
#     assert cliente_ana.valor_total_items() == 0


# def test_cliente_items_devuelve_copia(cliente_ana, menu):
#     item = ItemPedido.desde_menu(menu, "Cafe con leche")
#     cliente_ana.agregar_item(item)
    
#     items = cliente_ana.items()
#     items.clear()
    
#     assert cliente_ana.cantidad_items() == 1

# # ==================== TESTS DE EMPLEADO Y GESTION DE PEDIDOS ====================

# def test_empleado_empieza_sin_pedidos(empleado):
#     assert empleado.cantidad_pedidos() == 0
#     assert empleado.pedidos() == {}


# def test_empleado_crear_pedido_para_mesa(empleado, mesa_1):
#     assert empleado.crear_pedido(mesa_1)
#     assert empleado.cantidad_pedidos() == 1
#     assert mesa_1.id in empleado.pedidos()
#     assert empleado.pedido_de_mesa(mesa_1) is not None


# def test_empleado_no_crear_pedido_duplicado(empleado, mesa_1):
#     empleado.crear_pedido(mesa_1)
#     assert not empleado.crear_pedido(mesa_1)
#     assert empleado.cantidad_pedidos() == 1


# def test_empleado_agregar_item_a_pedido(empleado, mesa_1):
#     empleado.crear_pedido(mesa_1)
#     item = ItemPedido("Cafe con leche", 3000)
    
#     assert empleado.agregar_item_a_pedido(mesa_1, item)
    
#     pedido = empleado.pedido_de_mesa(mesa_1)
#     assert pedido.cantidad_items() == 1
#     assert pedido.valor() == 3000


# def test_empleado_agregar_item_sin_pedido(empleado, mesa_1):
#     item = ItemPedido("Cafe con leche", 3000)
#     assert not empleado.agregar_item_a_pedido(mesa_1, item)


# def test_empleado_agregar_item_duplicado(empleado, mesa_1):
#     empleado.crear_pedido(mesa_1)
#     item = ItemPedido("Cafe con leche", 3000)
    
#     empleado.agregar_item_a_pedido(mesa_1, item)
#     assert not empleado.agregar_item_a_pedido(mesa_1, item)


# def test_empleado_tomar_pedido_a_mesa(empleado, cliente_ana, cliente_carlos, mesa_1, menu):
#     cliente_ana.asignar_mesa(mesa_1)
#     cliente_carlos.asignar_mesa(mesa_1)
    
#     cliente_ana.sentarse_en(mesa_1)
#     cliente_carlos.sentarse_en(mesa_1)
    
#     item1 = ItemPedido("servilletero")
#     item2 = ItemPedido.desde_menu(menu, "Cafe con leche")
#     item3 = ItemPedido("agua")
    
#     cliente_ana.agregar_item(item1)
#     cliente_carlos.agregar_item(item2)
#     cliente_carlos.agregar_item(item3)
    
#     cliente_carlos.preparar_item_para_pedir(item2)
#     cliente_carlos.preparar_item_para_pedir(item3)
#     cliente_ana.preparar_item_para_pedir(item1)
    
#     empleado.crear_pedido(mesa_1)
#     assert empleado.tomar_pedido_a_mesa(mesa_1)
    
#     pedido = empleado.pedido_de_mesa(mesa_1)
#     assert pedido.cantidad_items() == 3
#     assert item1 in pedido.items()
#     assert item2 in pedido.items()
#     assert item3 in pedido.items()


# def test_empleado_tomar_pedido_a_mesa_solo_items_para_pedir(empleado, cliente_ana, mesa_1):
#     empleado.asignar_mesa_a_cliente(cliente_ana, mesa_1)
#     cliente_ana.sentarse_en(mesa_1)
    
#     item1 = ItemPedido("Cafe con leche", 3000)
#     item2 = ItemPedido("Croissant", 4000)
    
#     cliente_ana.agregar_item(item1)
#     cliente_ana.agregar_item(item2)
#     cliente_ana.preparar_item_para_pedir(item1)
    
#     empleado.crear_pedido(mesa_1)
#     empleado.tomar_pedido_a_mesa(mesa_1)
    
#     pedido = empleado.pedido_de_mesa(mesa_1)
#     assert pedido.cantidad_items() == 1
#     assert pedido.items()[0] == item1
#     assert not item1.esta_para_pedir()


# def test_empleado_tomar_pedido_a_mesa_sin_pedido(empleado, cliente_ana, mesa_1):
#     cliente_ana.sentarse_en(mesa_1)
#     item = ItemPedido("Cafe con leche", 3000)
#     cliente_ana.agregar_item(item)
#     cliente_ana.preparar_item_para_pedir(item)
    
#     assert not empleado.tomar_pedido_a_mesa(mesa_1)


# def test_empleado_tomar_pedido_a_mesa_sin_clientes(empleado, mesa_1):
#     empleado.crear_pedido(mesa_1)
#     assert empleado.tomar_pedido_a_mesa(mesa_1)
    
#     pedido = empleado.pedido_de_mesa(mesa_1)
#     assert pedido.cantidad_items() == 0


# def test_empleado_tomar_pedido_a_mesa_clientes_sin_items(empleado, cliente_ana, mesa_1):
#     empleado.asignar_mesa_a_cliente(cliente_ana, mesa_1)
#     cliente_ana.sentarse_en(mesa_1)
    
#     empleado.crear_pedido(mesa_1)
#     assert empleado.tomar_pedido_a_mesa(mesa_1)
    
#     pedido = empleado.pedido_de_mesa(mesa_1)
#     assert pedido.cantidad_items() == 0


# def test_empleado_tomar_pedido_a_mesa_clientes_sentados_correctamente(empleado, cliente_ana, cliente_carlos, mesa_1, mesa_2):
#     cliente_ana.asignar_mesa(mesa_1)
#     cliente_carlos.asignar_mesa(mesa_2)
    
#     cliente_ana.sentarse_en(mesa_1)
#     cliente_carlos.sentarse_en(mesa_2)
    
#     item_ana = ItemPedido("Cafe con leche", 3000)
#     item_carlos = ItemPedido("Croissant", 4000)
    
#     cliente_ana.agregar_item(item_ana)
#     cliente_ana.preparar_item_para_pedir(item_ana)
    
#     cliente_carlos.agregar_item(item_carlos)
#     cliente_carlos.preparar_item_para_pedir(item_carlos)
    
#     empleado.crear_pedido(mesa_1)
#     empleado.crear_pedido(mesa_2)
    
#     empleado.tomar_pedido_a_mesa(mesa_1)
    
#     pedido_mesa1 = empleado.pedido_de_mesa(mesa_1)
#     pedido_mesa2 = empleado.pedido_de_mesa(mesa_2)
    
#     assert pedido_mesa1.cantidad_items() == 1
#     assert pedido_mesa2.cantidad_items() == 0


# def test_empleado_tomar_pedido_a_mesa_no_duplica(empleado, cliente_ana, mesa_1):
#     empleado.asignar_mesa_a_cliente(cliente_ana, mesa_1)
#     cliente_ana.sentarse_en(mesa_1)
    
#     item = ItemPedido("Cafe con leche", 3000)
#     cliente_ana.agregar_item(item)
#     cliente_ana.preparar_item_para_pedir(item)
    
#     empleado.crear_pedido(mesa_1)
#     empleado.tomar_pedido_a_mesa(mesa_1)
#     empleado.tomar_pedido_a_mesa(mesa_1)
    
#     pedido = empleado.pedido_de_mesa(mesa_1)
#     assert pedido.cantidad_items() == 1


# def test_empleado_tomar_pedido_a_mesa_actualiza_estado_items(empleado, cliente_ana, mesa_1):
#     empleado.asignar_mesa_a_cliente(cliente_ana, mesa_1)
#     cliente_ana.sentarse_en(mesa_1)
    
#     item = ItemPedido("Cafe con leche", 3000)
#     cliente_ana.agregar_item(item)
#     cliente_ana.preparar_item_para_pedir(item)
    
#     assert item.esta_para_pedir()
#     assert not item.fue_pedido()
    
#     empleado.crear_pedido(mesa_1)
#     empleado.tomar_pedido_a_mesa(mesa_1)
    
#     assert not item.esta_para_pedir()
#     assert item.fue_pedido()


# def test_empleado_cerrar_pedido(empleado, mesa_1):
#     empleado.crear_pedido(mesa_1)
#     assert empleado.cantidad_pedidos() == 1
    
#     assert empleado.cerrar_pedido(mesa_1)
#     assert empleado.cantidad_pedidos() == 0
#     assert empleado.pedido_de_mesa(mesa_1) is None


# def test_empleado_cerrar_pedido_inexistente(empleado, mesa_1):
#     assert not empleado.cerrar_pedido(mesa_1)


# def test_empleado_cerrar_pedido_libera_items(empleado, cliente_ana, mesa_1):
#     empleado.asignar_mesa_a_cliente(cliente_ana, mesa_1)
#     cliente_ana.sentarse_en(mesa_1)
    
#     item = ItemPedido("Cafe con leche", 3000)
#     cliente_ana.agregar_item(item)
#     cliente_ana.preparar_item_para_pedir(item)
    
#     empleado.crear_pedido(mesa_1)
#     empleado.tomar_pedido_a_mesa(mesa_1)
    
#     assert empleado.cantidad_pedidos() == 1
    
#     empleado.cerrar_pedido(mesa_1)
    
#     assert empleado.cantidad_pedidos() == 0
#     assert cliente_ana.cantidad_items() == 1


# def test_empleado_obtener_resumen_pedido(empleado, mesa_1):
#     empleado.crear_pedido(mesa_1)
    
#     item1 = ItemPedido("Cafe con leche", 3000)
#     item2 = ItemPedido("Croissant", 4000)
    
#     empleado.agregar_item_a_pedido(mesa_1, item1)
#     empleado.agregar_item_a_pedido(mesa_1, item2)
    
#     resumen = empleado.resumen_pedido(mesa_1)
#     assert resumen is not None
#     assert resumen["mesa"] == mesa_1
#     assert resumen["total"] == 7000
#     assert len(resumen["items"]) == 2
#     assert item1 in resumen["items"]
#     assert item2 in resumen["items"]


# def test_empleado_resumen_pedido_inexistente(empleado, mesa_1):
#     assert empleado.resumen_pedido(mesa_1) is None


# def test_empleado_total_pedidos(empleado, mesa_1, mesa_2):
#     empleado.crear_pedido(mesa_1)
#     empleado.crear_pedido(mesa_2)
    
#     item1 = ItemPedido("Cafe con leche", 3000)
#     item2 = ItemPedido("Croissant", 4000)
#     item3 = ItemPedido("Salmón", 9800)
    
#     empleado.agregar_item_a_pedido(mesa_1, item1)
#     empleado.agregar_item_a_pedido(mesa_1, item2)
#     empleado.agregar_item_a_pedido(mesa_2, item3)
    
#     assert empleado.total_pedidos() == 3000 + 4000 + 9800


# def test_cliente_quitar_item_entregado_no_permitido(cliente_ana, empleado, mesa_1, menu):
#     empleado.asignar_mesa_a_cliente(cliente_ana, mesa_1)
#     cliente_ana.sentarse_en(mesa_1)
    
#     item = ItemPedido.desde_menu(menu, "Cafe con leche")
#     cliente_ana.agregar_item(item)
    
#     cliente_ana.preparar_item_para_pedir(item)
#     assert item.esta_para_pedir()
    
#     empleado.crear_pedido(mesa_1)
#     empleado.tomar_pedido_a_mesa(mesa_1)
#     assert item.fue_pedido()
    
#     empleado.entregar_item_de_pedido(mesa_1, item)
#     assert item.fue_entregado()

# # ==================== TESTS DE INTEGRACION ====================

# def test_flujo_completo_pedido(empleado, mesa_1, menu, cliente_ana, cliente_carlos):
#     cliente_ana.asignar_mesa(mesa_1)
#     cliente_carlos.asignar_mesa(mesa_1)
    
#     cliente_ana.sentarse_en(mesa_1)
#     cliente_carlos.sentarse_en(mesa_1)
    
#     item_ana_1 = ItemPedido.desde_menu(menu, "Cafe con leche")
#     item_ana_2 = ItemPedido.desde_menu(menu, "Croissant nutella")
#     item_carlos = ItemPedido.desde_menu(menu, "Salmón a la plancha")
    
#     cliente_ana.agregar_item(item_ana_1)
#     cliente_ana.agregar_item(item_ana_2)
#     cliente_carlos.agregar_item(item_carlos)
    
#     cliente_ana.preparar_item_para_pedir(item_ana_1)
#     cliente_carlos.preparar_item_para_pedir(item_carlos)
    
#     assert cliente_ana.cantidad_items() == 2
#     assert cliente_carlos.cantidad_items() == 1
    
#     empleado.crear_pedido(mesa_1)
#     empleado.tomar_pedido_a_mesa(mesa_1)
    
#     pedido = empleado.pedido_de_mesa(mesa_1)
#     assert pedido.cantidad_items() == 2
#     assert pedido.valor() == 3000 + 9800
    
#     assert item_ana_1.fue_pedido()
#     assert not item_ana_2.fue_pedido()
#     assert item_carlos.fue_pedido()
    
#     empleado.cerrar_pedido(mesa_1)
#     assert empleado.pedido_de_mesa(mesa_1) is None


# def test_flujo_completo_con_varias_mesas(empleado, mesa_1, mesa_2, menu, 
#                                           cliente_ana, cliente_carlos, cliente_laura):
#     cliente_ana.asignar_mesa(mesa_1)
#     cliente_carlos.asignar_mesa(mesa_1)
#     cliente_laura.asignar_mesa(mesa_2)
    
#     cliente_ana.sentarse_en(mesa_1)
#     cliente_carlos.sentarse_en(mesa_1)
#     cliente_laura.sentarse_en(mesa_2)
    
#     item1 = ItemPedido.desde_menu(menu, "Cafe con leche")
#     item2 = ItemPedido.desde_menu(menu, "Croissant nutella")
#     item3 = ItemPedido.desde_menu(menu, "Salmón a la plancha")
#     item4 = ItemPedido.desde_menu(menu, "Pizza margarita")
#     item5 = ItemPedido.desde_menu(menu, "Ravioles con salsa fileto")
    
#     cliente_ana.agregar_item(item1)
#     cliente_ana.agregar_item(item2)
#     cliente_carlos.agregar_item(item3)
#     cliente_carlos.agregar_item(item4)
#     cliente_laura.agregar_item(item5)
    
#     cliente_ana.preparar_item_para_pedir(item1)
#     cliente_carlos.preparar_item_para_pedir(item3)
#     cliente_carlos.preparar_item_para_pedir(item4)
#     cliente_laura.preparar_item_para_pedir(item5)
    
#     empleado.crear_pedido(mesa_1)
#     empleado.crear_pedido(mesa_2)
    
#     empleado.tomar_pedido_a_mesa(mesa_1)
#     empleado.tomar_pedido_a_mesa(mesa_2)
    
#     pedido1 = empleado.pedido_de_mesa(mesa_1)
#     pedido2 = empleado.pedido_de_mesa(mesa_2)
    
#     assert pedido1.cantidad_items() == 3
#     assert pedido1.valor() == 3000 + 9800 + 7500
#     assert pedido2.cantidad_items() == 1
#     assert pedido2.valor() == 7200
    
#     total = empleado.total_pedidos()
#     assert total == 3000 + 9800 + 7500 + 7200