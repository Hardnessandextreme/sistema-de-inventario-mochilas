class Mochila:
    def __init__(self, nombre, capacidad, objetosAlmacenados):
        self._nombre = nombre
        self._capacidad = capacidad
        self._objetosAlmacenados = []

        peso_total = sum(objeto.peso for objeto in objetosAlmacenados)
        if peso_total <= capacidad:
            self._objetosAlmacenados = objetosAlmacenados
        else:
            print('Excediste la capacidad de la mochila')

    def __str__(self):
        objetosAlmacenados_str = ''
        for numero, objeto in enumerate(self._objetosAlmacenados, 1):
            objetosAlmacenados_str += f'{numero}. {objeto}\n'
        return (f'{self._nombre} - Capacidad: {self.comprobarPeso()}/{self._capacidad}\n'
                f'{objetosAlmacenados_str}\n')

    def meterObjeto(self, objetosAlmacenados):
        pesoTotal = self.comprobarPeso() + objetosAlmacenados.peso
        if pesoTotal < self._capacidad:
            self._objetosAlmacenados.append(objetosAlmacenados)
        else:
            print('Excediste la capacidad de la mochila.')

    def quitarObjeto(self, idObjeto):
        if 0 < idObjeto < len(self._objetosAlmacenados):
            self._objetosAlmacenados.pop(idObjeto)
        else:
            print('Id de objeto no valida')

    def comprobarPeso(self):
        peso_total = sum(objeto.peso for objeto in self._objetosAlmacenados)
        return float(peso_total)

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def capacidad(self):
        return self._capacidad

    @capacidad.setter
    def capacidad(self, capacidad):
        self._capacidad = capacidad

    @property
    def objetosAlmacenados(self):
        return self._objetosAlmacenados

    @objetosAlmacenados.setter
    def objetosAlmacenados(self, objetosAlmacenados):
        self._objetosAlmacenados = objetosAlmacenados

class MochilaPequena(Mochila):
    def __init__(self, nombre, objetosAlmacenados):
        capacidad = 1.5
        super().__init__(nombre, capacidad, objetosAlmacenados)


class MochilaMediana(Mochila):
    def __init__(self, nombre, objetosAlmacenados):
        capacidad = 3.5
        super().__init__(nombre, capacidad, objetosAlmacenados)


class MochilaGrande(Mochila):
    def __init__(self, nombre, objetosAlmacenados):
        capacidad = 7.2
        super().__init__(nombre, capacidad, objetosAlmacenados)
