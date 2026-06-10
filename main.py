from models.objeto import Objeto
from models.mesa import Mesa
from models.cliente import Cliente
from models.empleado import Empleado

servilletero = Objeto("Servilletero")
mesa = Mesa(1, 2)
seve = Empleado("Seve", "Moz@")
maxi = Cliente("Maxi", 25)
maxi.agregar_caracteristica("enojad@")

seve.cargar_objeto(servilletero)

print(seve)
print(mesa)
print(f"{maxi}\n")

mesa.sentar_cliente(maxi)
seve.dejar_objeto(mesa, servilletero)

print(seve)
print(mesa)
print(f"{maxi}\n")