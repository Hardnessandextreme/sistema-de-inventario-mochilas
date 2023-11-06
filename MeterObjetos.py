from Mochila import *
from ObjetoFisico import *

objeto1 = ObjetoFisico(nombre='Laptop', peso=0.5)
objeto2 = ObjetoFisico(nombre='Caja de cigarrillos', peso=0.2)
objeto3 = ObjetoFisico(nombre='Blunt de marihuana', peso=0.1)
objeto4 = ObjetoFisico(nombre='Pistola 9mm', peso=1.3)

aMochila1 = [objeto1, objeto2, objeto3]

mochila1 = MochilaGrande(nombre='Mochila de camisa', objetosAlmacenados=aMochila1)


# mochila1.meterObjeto(objeto2)
mochila1.quitarObjeto(0)


print(mochila1)
mochila1.meterObjeto(objeto4)
print(mochila1)
mochila1.quitarObjeto(0)
print(mochila1)