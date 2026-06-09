from models.objeto import Objeto
from models.mesa import Mesa
from models.cliente import Cliente

mesa = Mesa(1, 2)

servilletero = Objeto("Servilletero")
lata = Objeto("Lata")

mesa.agregar_objeto(servilletero)
maxi = Cliente("Maxi", 25)
maxi.agregar_caracteristica("enojad@")

print(mesa)
print(f"{maxi}\n")

mesa.sentar_cliente(maxi)
mesa.agregar_objeto(lata)
mesa.ensuciar()

print(mesa)
print(f"{maxi}\n")