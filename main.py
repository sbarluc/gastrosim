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

mesa.sentar_cliente(ana)

print(mesa)

mesa.quitar_objeto(vaso_sucio)
mesa.limpiar()

mesa.ensuciar()

print(mesa)