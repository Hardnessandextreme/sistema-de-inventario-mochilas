(EN CONSTANTE ACTUALIZACION)

# Sistema de Inventario de Mochilas

El Sistema de Inventario de Mochilas basado en pesos es una aplicación Python que permite gestionar objetos físicos que pueden ser almacenados en diferentes tipos de mochilas. Los objetos tienen un atributo de peso en kilogramos, y las mochilas tienen una capacidad máxima también expresada en kilogramos. El sistema garantiza que los objetos almacenados en una mochila no excedan su límite de peso.

## Clases

## - `ObjetoFisico`

Esta clase representa los objetos físicos que se pueden almacenar en las mochilas. Cada objeto tiene un nombre y un peso en kilogramos. Los objetos se crean como instancias de esta clase con la siguiente sintaxis:

```python
objeto = ObjetoFisico(nombre='Nombre del Objeto', peso=peso_en_kg)
```

### Atributos:
- nombre: El nombre del objeto.
- peso: El peso del objeto en kilogramos.
- _idObjeto: Un identificador único generado automáticamente para cada objeto creado.

### Métodos:
- __str__(): Devuelve una representación en forma de cadena del objeto con el formato "nombre (peso kg)".
- generar_valor_id_objeto(): Método de clase que genera un identificador único para cada objeto creado.

#### Ejemplo de uso:
```python
# Crear un objeto físico llamado "Manzana" con peso de 0.02 kg.
manzana = ObjetoFisico(nombre='Manzana', peso=0.02)

# Mostrar el objeto físico en la consola.
print(manzana)
```

## - `Mochila`
Esta clase representa las mochilas en las que se almacenarán los objetos físicos. Cada mochila tiene un nombre, una capacidad máxima (expresada en kilogramos) y una lista de objetos almacenados en ella. Las mochilas se crean como instancias de esta clase con la siguiente sintaxis:

```python
mochila = Mochila(nombre='Nombre de la Mochila', capacidad=capacidad_en_kg, objetosAlmacenados=lista_de_objetos)
```

### Métodos de Mochila
- __str__(): Devuelve una representación en forma de cadena de la mochila con el formato "nombre - Capacidad: peso_actual/ capacidad_maxima".
- meterObjeto(objetosAlmacenados): Agrega un objeto físico a la mochila, verificando que no exceda la capacidad máxima. Si excede el peso, muestra un mensaje indicando que no es posible agregarlo.
- quitarObjeto(idObjeto): Elimina un objeto físico de la mochila según su ID.
- comprobarPeso(): Calcula y devuelve el peso total de los objetos en la mochila.

### Ejemplo de Uso:
```python
# Crear una mochila pequeña con nombre "Mochila1" y sin objetos almacenados.
mochila_pequena = MochilaPequena(nombre='Mochila1', objetosAlmacenados=[])

# Crear un objeto físico llamado "Manzana" con peso de 0.02 kg.
manzana = ObjetoFisico(nombre='Manzana', peso=0.02)

# Agregar la "Manzana" a la mochila pequeña.
mochila_pequena.meterObjeto(manzana)

# Mostrar el contenido de la mochila.
print(mochila_pequena)
```

# Funcionalidades
El sistema incluye las siguientes funcionalidades:
- Crear objetos físicos y mochilas con sus atributos específicos.
- Agregar objetos físicos a las mochilas, considerando su peso y la capacidad máxima.
- Quitar objetos de las mochilas según su ID.
- Verificar si el peso total de los objetos en una mochila no excede su capacidad máxima.

Este sistema de inventario de mochilas es ideal para prácticas de programación orientada a objetos (POO) y ofrece una base sólida para extender y agregar más funcionalidades según las necesidades del proyecto.
