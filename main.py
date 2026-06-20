from models.objeto import Objeto
from models.mesa import Mesa
from models.estanteria import Estanteria
from models.cliente import Cliente
from models.empleado import Empleado

servilletero = Objeto("Servilletero")
estanteria = Estanteria([servilletero])
mesa1 = Mesa(2)
mesa2 = Mesa(2)
seve = Empleado("Seve", "Moz@")
ana = Cliente("Ana", 25, specs=["Alegre", "Distraida"])
eduardo = Cliente("Eduardo", 26)

print("Entes:\n")
print(seve)
print(ana)
print(eduardo)
print(mesa1)
print(mesa2)
print(estanteria)
print(servilletero)
print("======================================================")

seve.cargar_objeto(estanteria, servilletero)
print("\nSeve cargo un servilletero de la estanteria:")
print(seve)
print(estanteria)

seve.dejar_objeto(mesa1, servilletero)
print(f"Seve dejo un servilletero en la mesa {mesa1.id}:")
print(seve)
print(mesa1)

seve.asignar_mesa_a_cliente(eduardo, mesa1)
print(f"Seve asigna a Eduardo a la mesa {mesa1.id}:")
print(mesa1)
print(eduardo)

ana.sentarse_en(mesa1)
print(f"Ana se sentó en la mesa {mesa1.id}:")
print(ana)
print(mesa1)

eduardo.sentarse_en(mesa1)
print(f"Eduardo se sentó en la mesa {mesa1.id}:\n")
print(eduardo)
print(ana)
print(mesa1)

seve.asignar_mesa_a_cliente(ana, mesa2)
print(f"Seve asigna a Ana a la mesa {mesa2.id}:")
print(ana)
print(mesa1)
print(mesa2)

ana.pararse()
print("\nAna se paró porque no estaba en la mesa correcta:")
print(ana)
print(eduardo)
print(mesa1)
print(mesa2)

ana.sentarse_en(mesa2)

print(f"\nAna se sentó en la mesa {mesa2.id}:")
print(ana)
print(eduardo)
print(mesa1)
print(mesa2)