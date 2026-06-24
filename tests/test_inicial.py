from models.objeto import Objeto
from models.mesa import Mesa
from models.estanteria import Estanteria
from models.cliente import Cliente
from models.empleado import Empleado
from models.simulador import Simulador

def test_inicial():  

    servilletero = Objeto("Servilletero")
    menu = Objeto("Menu")
    estanteria = Estanteria([servilletero, menu])
    mesa1 = Mesa(2)
    mesa2 = Mesa(1)
    seve = Empleado("Seve", "Moz@")
    ana = Cliente("Ana", 25, specs=["Alegre", "Distraida"])
    eduardo = Cliente("Eduardo", 26)
    zoteldo = Cliente("Zoteldo", 28)
    simulador = Simulador()
    simulador.agregar_estanterias([estanteria])   \
        .agregar_mesas([mesa1, mesa2])    \
        .agregar_clientes([ana, eduardo, zoteldo])   \
        .agregar_empleados([seve])
    
    simulador.mostrar_universo()
    print("\n======================================================")

    seve.cargar_objeto(estanteria, servilletero)
    seve.cargar_objeto(estanteria, menu)
    print("Seve cargo un servilletero y menu de la estanteria:\n")
    simulador.mostrar_universo()
    print("\n======================================================")

    seve.dejar_objeto(mesa1, servilletero)
    print("Seve dejo un servilletero en la mesa 1:\n")
    simulador.mostrar_universo()
    print("\n======================================================")

    seve.asignar_mesa_a_cliente(eduardo, mesa1)
    print("Seve asigna a Eduardo a la mesa 1:\n")
    simulador.mostrar_universo()
    print("\n======================================================")

    ana.sentarse_en(mesa1)
    print("Ana se sentó en la mesa 1:\n")
    simulador.mostrar_universo()
    print("\n======================================================")

    eduardo.sentarse_en(mesa1)
    print("Eduardo se sentó en la mesa 1:\n")
    simulador.mostrar_universo()
    print("\n======================================================")

    seve.asignar_mesa_a_cliente(ana, mesa2)
    print("Seve asigna a Ana a la mesa 2:\n")
    simulador.mostrar_universo()
    print("\n======================================================")

    ana.pararse()
    print("\nAna se paró porque no estaba en la mesa correcta:\n")
    simulador.mostrar_universo()
    print("\n======================================================")

    seve.dejar_objeto(mesa2, menu)
    print("Seve dejo un menu en la mesa 2:\n")
    simulador.mostrar_universo()
    print("\n======================================================")

    ana.sentarse_en(mesa2)
    print("\nAna se sentó en la mesa 2:\n")
    simulador.mostrar_universo()
    print("\n======================================================")

    zoteldo.sentarse_en(mesa2)
    print("\nZoteldo intenta sentarse en la mesa 2 pero no pasa nada:\n")
    simulador.mostrar_universo()
    print("\n======================================================")

    zoteldo.sentarse_en(mesa1)
    print("\nZoteldo se sienta en la mesa 1:\n")
    simulador.mostrar_universo()
    print("\n======================================================")