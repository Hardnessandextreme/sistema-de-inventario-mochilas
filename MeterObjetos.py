from Mochila import *
from ObjetoFisico import *

objeto1 = ObjetoFisico(nombre='Laptop', peso=2.5)
objeto2 = ObjetoFisico(nombre='Arbol', peso=1000.23)

aMochila1 = [objeto1, objeto1]

mochila1 = MochilaPequena(nombre='Mochila de camisa', objetosAlmacenados=aMochila1)


# mochila1.meterObjeto(objeto2)

print(mochila1)