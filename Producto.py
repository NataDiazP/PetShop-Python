class Producto():
    """
        Producto: Información de los productos ofertados en la tienda
        Atributos: id, nombre, descripcion, valor, cantidadInventario, empleado, pedidos, comentarios
    """

    contadorIds=0
    def __init__(self, empleado, id=0, nombre="", descripcion="", valor=0, cantidadInventario=0):
        Producto.contadorIds+=1
        self.setId(Producto.contadorIds)
        self.setNombre(nombre)
        self.setDescripcion(descripcion)
        self.setValor(valor)
        self.setCantidadInventario(cantidadInventario)
        self.setEmpleado(empleado)
        self.setPedidos([])
        self.setComentarios([])

    def setId(self, id):
        self._id = id

    def getId(self):
        return self._id

    def setNombre(self, nombre):
        self._nombre = nombre

    def getNombre(self):
        return self._nombre

    def setDescripcion(self, descripcion):
        self._descripcion = descripcion

    def getDescripcion(self):
        return self._descripcion

    def setValor(self, valor):
        self._valor = valor

    def getValor(self):
        return self._valor

    def setCantidadInventario(self, cantidadInventario):
        self._cantidadInventario = cantidadInventario

    def getCantidadInventario(self):
        return self._cantidadInventario

    def setEmpleado(self, empleado):
        self._empleado = empleado
        self._empleado.getProductos().append(self)

    def getEmpleado(self):
        return self._empleado

    def setPedidos(self, pedidos):
        self._pedidos = pedidos

    def getPedidos(self):
        return self._pedidos

    def setComentarios(self, comentarios):
        self._comentarios = comentarios

    def getComentarios(self):
        return self._comentarios

    def listarProductos(self):
        return "id: " + str(self.getId()) + "\nNombre: " + self.getNombre() + "\nValor: " + str(
            self.getValor()) + "\nDescripcion: " + self.getDescripcion() + "\nCantidad en Inventario: " + str(self.getCantidadInventario())

    @staticmethod
    def seleccionarProducto(numeroId,listaproductos):
        for productoActual in listaproductos:
            if productoActual.getId()== numeroId:
                return {"Encontrado" : True,
                        "Objeto": productoActual
                }
        return {"Encontrado": False,
                "Objeto" : None
        }


