from models.objeto import Objeto
from models.mesa import Mesa
from models.estanteria import Estanteria
from models.cliente import Cliente
from models.empleado import Empleado

servilletero = Objeto("Servilletero")
menu = Objeto("Menu")
estanteria = Estanteria([servilletero, menu])
mesa1 = Mesa(2)
mesa2 = Mesa(1)
seve = Empleado("Seve", "Moz@")
ana = Cliente("Ana", 25, specs=["Alegre", "Distraida"])
eduardo = Cliente("Eduardo", 26)
zoteldo = Cliente("Zoteldo", 28)

print("Entes:")
print(seve)
print(ana)
print(eduardo)
print(zoteldo)
print(mesa1)
print(mesa2)
print(estanteria)
print(servilletero)
print(menu)
print("======================================================")

seve.cargar_objeto(estanteria, servilletero)
seve.cargar_objeto(estanteria, menu)
print("\nSeve cargo un servilletero y menu de la estanteria:")
print(seve)
print(estanteria)

seve.dejar_objeto(mesa1, servilletero)
print("Seve dejo un servilletero en la mesa 1:")
print(seve)
print(mesa1)

seve.asignar_mesa_a_cliente(eduardo, mesa1)
print("Seve asigna a Eduardo a la mesa 1:")
print(mesa1)
print(eduardo)

ana.sentarse_en(mesa1)
print("Ana se sentó en la mesa 1:")
print(ana)
print(mesa1)

eduardo.sentarse_en(mesa1)
print("Eduardo se sentó en la mesa 1:\n")
print(eduardo)
print(ana)
print(mesa1)

seve.asignar_mesa_a_cliente(ana, mesa2)
print("Seve asigna a Ana a la mesa 2:")
print(ana)
print(mesa1)
print(mesa2)

ana.pararse()
print("\nAna se paró porque no estaba en la mesa correcta:")
print(ana)
print(eduardo)
print(mesa1)
print(mesa2)

seve.dejar_objeto(mesa2, menu)
print("Seve dejo un menu en la mesa 2:")
print(seve)
print(mesa2)

ana.sentarse_en(mesa2)
print("\nAna se sentó en la mesa 2:")
print(ana)
print(eduardo)
print(mesa1)
print(mesa2)

zoteldo.sentarse_en(mesa2)
print("\nZoteldo intenta sentarse en la mesa 2 pero no pasa nada:")
print(zoteldo)
print(mesa2)

zoteldo.sentarse_en(mesa1)
print("\nZoteldo se sienta en la mesa 1:")
print(zoteldo)
print(mesa1)