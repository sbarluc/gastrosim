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

    input("\nPresiona Enter para continuar...")

def demo_completa():
    simulador = Simulador()
    mostrar_evento(simulador, "Demo")

if __name__ == "__main__":
    demo_completa()