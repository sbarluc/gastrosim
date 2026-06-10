from models.objeto import Objeto
from models.mesa import Mesa
from models.cliente import Cliente
from models.empleado import Empleado

servilletero = Objeto("Servilletero")
estanteria = Objeto("Estanteria", [servilletero])
mesa1 = Mesa(1, 2)
mesa2 = Mesa(1, 2)
seve = Empleado("Seve", "Moz@")
ana = Cliente("Ana", 25)

print(seve)

seve.cargar_objeto(estanteria, servilletero)

print(seve)
print(mesa1)
print(f"{ana}\n")

mesa1.sentar_cliente(ana)
seve.dejar_objeto(mesa1, servilletero)

print(seve)
print(mesa1)
print(mesa2)
print(f"{ana}\n")

mesa2.sentar_cliente(ana)

print(seve)
print(mesa1)
print(mesa2)
print(f"{ana}\n")