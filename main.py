from models.objeto import Objeto
from models.mesa import Mesa
from models.cliente import Cliente
from models.empleado import Empleado

servilletero = Objeto("Servilletero")
estanteria = Objeto("Estanteria", [servilletero])
mesa1 = Mesa(1, 2)
mesa2 = Mesa(2, 2)
seve = Empleado("Seve", "Moz@")
ana = Cliente("Ana", 25)
eduardo = Cliente("Eduardo", 26)

print("Entes:\n==================")
print(seve)
print(ana)
print(eduardo)
print(mesa1)
print(mesa2)
print(estanteria)
print(servilletero)
print("==================")

seve.cargar_objeto(estanteria, servilletero)
print("\nSeve cargo un servilletero de la estanteria:")
print(seve)
print(estanteria)
print(servilletero)

seve.dejar_objeto(mesa1, servilletero)
print("\nSeve dejo un servilletero en la mesa 1:")
print(seve)
print(mesa1)

mesa1.asignar_cliente(ana)
print("\nAna se asigna a la mesa 1:")
print(ana)
print(mesa1)

ana.sentarse(mesa2)
print("\nAna se equivocó y se sentó en la mesa 2:")
print(ana)
print(mesa1)
print(mesa2)

ana.pararse()
print("\nAna se paró y esta esperando saber su mesa:")
print(ana)
print(mesa1)
print(mesa2)