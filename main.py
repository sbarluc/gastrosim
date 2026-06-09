from models.objeto import Objeto
from models.mesa import Mesa
from models.cliente import Cliente

mesa = Mesa(1, 2)

servilletero = Objeto("Servilletero")
vaso_sucio = Objeto("Vaso sucio")

mesa.ensuciar()
mesa.agregar_objeto(servilletero)
mesa.agregar_objeto(vaso_sucio)

ana = Cliente("Ana", 30)
ana.agregar_caracteristica("apurad@")
ana.agregar_caracteristica("vegetarian@")
mesa.sentar_cliente(ana)

print(mesa)
print(ana)

ana.pararse()
mesa.quitar_objeto(vaso_sucio)
mesa.limpiar()

print(mesa)
print(ana)