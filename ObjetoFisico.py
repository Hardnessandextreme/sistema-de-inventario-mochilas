class ObjetoFisico:
    contador_objetos = 0

    @classmethod
    def generar_valor_id_objeto(cls):
        cls.contador_objetos += 1
        return cls.contador_objetos

    def __init__(self, nombre, peso):
        self._idObjeto = ObjetoFisico.generar_valor_id_objeto()
        self._nombre = nombre
        self._peso = peso

    def __str__(self):
        return f'{self._nombre} ({self._peso}kg)'


    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self, peso):
        self._peso = peso