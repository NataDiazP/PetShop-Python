class Producto():
    """
        Producto: Información de los productos ofertados en la tienda
        Atributos: id, nombre, descripcion, valor, cantidad_inventario, pedidos_producto, comentarios
    """

    productos = [] # Lista de productos
    contador_ids = 0 # Contador de ids - AUTOINCREMENTABLE

    def __init__(self, nombre="", valor=0, descripcion="", cantidad_inventario=0):

        """
            Id: self._id
            Name: self._nombre
            Description: self._descripcion
            Price: self._valor
            Amount in inventory: self._cantidadInventario
        """

        Producto.contador_ids += 1
        self.setId(Producto.contador_ids)
        self.setNombre(nombre)
        self.setDescripcion(descripcion)
        self.setValor(valor)
        self.setCantidadInventario(cantidad_inventario)
        self.setPedidosProducto([])
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

    def setCantidadInventario(self, cantidad_inventario):
        self._cantidad_inventario = cantidad_inventario

    def getCantidadInventario(self):
        return self._cantidad_inventario

    def setPedidosProducto(self, pedidos_producto):
        self._pedidos_producto = pedidos_producto

    def getPedidosProducto(self):
        return self._pedidos_producto

    def setComentarios(self, comentarios):
        self._comentarios = comentarios

    def getComentarios(self):
        return self._comentarios

    def toString(self, mensajes):
        # Metodo para mostrar la informacion del producto
        info_producto = mensajes["ID"] + str(self.getId()) + mensajes["user_name"] + self.getNombre() + mensajes["value"] + str(
                        self.getValor()) + mensajes["description"] + self.getDescripcion() + mensajes["amount_inventory"] + str(
                        self.getCantidadInventario())

        if len(self.getComentarios()) > 0:
            # Se hace con el fin de saber si hay comentarios en dicho producto y agregarle al string que se va a devolver la parte de los comentarios
            acumComentarios = "\n-------------------------"

            for comentario_actual in self.getComentarios():
                acumComentarios += comentario_actual.toString()

            acumComentarios += "\n-------------------------"

            return info_producto + mensajes["comments"] + acumComentarios

        return info_producto

    def toStringCarrito(self, mensajes):
        # Metodo para mostrar la informacion del producto en el carrito de compras
        return mensajes["ID"] + str(self.getId()) + mensajes["user_name"] + self.getNombre() + mensajes["description"] + self.getDescripcion() + mensajes["value"] + str(self.getValor())

    def validarExistenciaEnLista(self, listamensajes):
        # Metodo que sirve para que cuando un empleado cree un producto se valide si dicho producto ya existe en la lista y de lo contrario lo agregue
        for productoActual in Producto.productos:
            # Se convierten el nombre y el nombre a buscar a minuscula para encontrar todas las coincidencias posibles
            if productoActual.getNombre().lower() == self.getNombre().lower():
                return listamensajes["product_with_same_name"]

        Producto.productos.append(self)
        return listamensajes["product_added"]

    def actualizarProducto(self, nombre, valor, descripcion, cantidad_inventario):
        # Sirve para actualizar el producto
        self._nombre = nombre
        self._valor = valor
        self._descripcion = descripcion
        self._cantidad_inventario = cantidad_inventario

    def validarCantidadInventario(self, cantidad_venta):
        # Devuelve true si hay suficiente cantidad en inventario, de lo contrario devuelve false
        return self._cantidad_inventario >= cantidad_venta

    def listarProductos(mensajes):
        lista_productos = ""

        for producto_actual in Producto.productos:
            lista_productos += "\n-------------------------------------------------"
            lista_productos += "\n" + producto_actual.toString(mensajes)

        return lista_productos

    @staticmethod
    def buscarProductoNombre(nombreBuscar):
        # Metodo que devuelve una lista con productos buscados mediante una palabra por un empleado
        listadoProductosBuscados = []
        for productoActual in Producto.productos:
            # Se busca en el nombre del producto en minuscula si contiene en algun sitio un string con el nombre a buscar
            if productoActual.getNombre().lower().find(nombreBuscar.lower()) != -1:
                listadoProductosBuscados.append(productoActual)
        return listadoProductosBuscados

    @staticmethod
    def seleccionarProducto(numeroId):
        # Metodo que devuelve un producto seleccionado por una ID
        for productoActual in Producto.productos:
            if productoActual.getId() == numeroId:
                return productoActual

        return None

    @staticmethod
    def borrarProducto(numeroId, mensajes):
        # Metodo que borra un producto de la lista de productos
        for productoActual in Producto.productos:
            if productoActual.getId() == numeroId:
                Producto.productos.remove(productoActual)
                return mensajes["product_deleted"]

        return mensajes["product_not_found"]

    @staticmethod
    def validarIdEnListaproductosAcomentar(id, lista):
        # Metodo para validar que un producto que se quiere comentar esta en la lista de productos comprados
        for producto_v in lista:
            if id == producto_v.getId():
                return True
        return False
