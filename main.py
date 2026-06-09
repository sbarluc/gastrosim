from models.mesa import Mesa
from models.cliente import Cliente

mesa = Mesa(1, 2)

ana = Cliente("Ana", 30)
pedro = Cliente("Pedro", 25)

mesa.sentar_cliente(ana)
mesa.sentar_cliente(pedro)

mesa.ensuciar()

print(mesa)