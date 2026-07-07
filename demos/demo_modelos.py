from core.simulador import Simulador
import os

# -------------------------------------------------------------------------
# DEMO DE INTEGRACIÓN (FUSIÓN DE TODOS LOS TESTS)
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