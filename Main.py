import datetime  # Se importa para poder hacer uso de la fecha actual
from Persona import Persona
from Producto import Producto
from Empleado import Empleado
from Mensajes import Mensajes
from Comentario import Comentario
from Pedido import Pedido
from Pedido_Producto import Pedido_Producto
from Util import Util


class Main:
    usuario_actual = None  # Usuario que se encuentra actualmente activo en la sesion
    mensajes = None  # Diccionario de mensajes
    datos_ficticios_agregados = 0  # Para validar si ya se insertaron datos ficticios
    datos_ficticios_txt_agregados = 0  # Para validar si ya se insertaron datos ficticios desde un txt
    breakOpciones = 0  # Sirve para mostrar varias veces los menus, nunca se cambiara sino que se pasara de un menu a otro
    pedido_pendiente = None  # El pedido actual que el usuario tiene

    @staticmethod
    def setIdioma():
        # Metodo para seleccionar el idioma

        print("\nLanguage:\n\n1. Español\n2. Inglés")

        lang = int(input("\n-> "))

        if lang == 1:
            Main.mensajes = Mensajes.mensajes_es
        elif lang == 2:
            Main.mensajes = Mensajes.mensajes_eng

        Main.menuPrincipal()

    @staticmethod
    def menuPrincipal():
        # Menu de inicio de la aplicacion
        print("\n-----------------------------------------------------")
        print(Main.mensajes["welcome_menu"])

        while Main.breakOpciones == 0:
            opcionSeleccionada = int(input("\n-> "))
            if opcionSeleccionada == 1:
                # Generar datos ficticios
                if Main.datos_ficticios_agregados == 0:
                    Util.generarDatosFicticios()
                    print(Main.mensajes["succes_dummy_data"])
                    Main.datos_ficticios_agregados = 1
                else:
                    print(Main.mensajes["dummy_data_added"])

                Main.menuPrincipal()

            elif opcionSeleccionada == 2:
                # Generar datos ficticios txt
                if Main.datos_ficticios_txt_agregados == 0:
                    Util.generarDatosFicticiosTxt()
                    print(Main.mensajes["succes_dummy_data"])
                    Main.datos_ficticios_txt_agregados = 1
                else:
                    print(Main.mensajes["dummy_data_added"])

                Main.menuPrincipal()

            elif opcionSeleccionada == 3:
                # Seleccionar tipo de usuario
                print("\n-----------------------------------------------------")
                print(Main.mensajes["user_type"])

                while Main.breakOpciones == 0:

                    opcionSeleccionada = int(input("\n-> "))

                    if opcionSeleccionada == 1:
                        Main.menuUsuariosLogReg()
                    elif opcionSeleccionada == 2:
                        Main.menuEmpleadosLog()
                    elif opcionSeleccionada == 3:
                        Main.menuPrincipal()
                    else:
                        print(Main.mensajes["wrong_option"])

            elif opcionSeleccionada == 4:
                # Salir de la aplicacion
                exit()

            else:
                # Opcion erronea
                print(Main.mensajes["wrong_option"])

    @staticmethod
    def menuUsuariosLogReg():
        # Menu de log in y registro de los usuarios
        print("\n-----------------------------------------------------")
        print(Main.mensajes["client_login_menu"])

        while Main.breakOpciones == 0:
            opcionSeleccionada = int(input("\n-> "))

            if opcionSeleccionada == 1 or opcionSeleccionada == 2:
                # Inicio de sesion o registro de un usuario
                Main.usuario_actual = Persona()
                operacion_completada = {}

                if opcionSeleccionada == 1:
                    # Inicio de sesion
                    email = input(Main.mensajes["email"])
                    password = input(Main.mensajes["user_password"])

                    Main.usuario_actual.setEmail(email)
                    Main.usuario_actual.setPassword(password)

                    operacion_completada = Main.usuario_actual.iniciar_sesion(Main.mensajes)

                elif opcionSeleccionada == 2:
                    # Registro
                    nombre = input(Main.mensajes["user_name"])
                    email = input(Main.mensajes["email"])
                    telefono = input(Main.mensajes["user_phone"])
                    direccion = input(Main.mensajes["user_address"])
                    password = input(Main.mensajes["user_password"])

                    operacion_completada = Main.usuario_actual.registrarse(nombre, email, telefono, direccion, password,
                                                                           Main.mensajes)

                if operacion_completada["exitoso"] == True:
                    print(operacion_completada["mensaje"])
                    Main.menuUsuariosOpciones()

                else:
                    print(operacion_completada["mensaje"])
                    Main.menuUsuariosLogReg()

            elif opcionSeleccionada == 3:
                # Volver atras
                Main.menuPrincipal()

            else:
                # Opcion erronea
                print(Main.mensajes["wrong_option"])

    @staticmethod
    def menuUsuariosOpciones():
        # Menu de opciones generales de los usuarios una vez iniciada sesion o registrados
        print("\n-----------------------------------------------------")
        print("\n" + Main.usuario_actual.getNombre() + Main.mensajes["client_menu"])

        while Main.breakOpciones == 0:
            opcionSeleccionada = int(input("\n-> "))

            if opcionSeleccionada == 1:
                # Ver productos
                if len(Producto.productos) == 0:
                    print(Main.mensajes["product_not_found"])
                    input(Main.mensajes["go_back_press_any_key"])
                    Main.menuUsuariosOpciones()

                else:

                    for producto_actual in Producto.productos:
                        print("\n-------------------------------------------------")
                        print(producto_actual.toString(Main.mensajes))
                        print("-------------------------------------------------")

                    input(Main.mensajes["go_back_press_any_key"])
                    Main.menuUsuariosOpciones()

            elif opcionSeleccionada == 2:
                # Seleccionar productos
                if len(Producto.productos) == 0:

                    print(Main.mensajes["product_not_found"])
                    input(Main.mensajes["go_back_press_any_key"])
                    Main.menuUsuariosOpciones()

                else:
                    for producto_actual in Producto.productos:
                        if producto_actual.getCantidadInventario() > 0:
                            print("\n-------------------------------------------------")
                            print(producto_actual.toString(Main.mensajes))
                            print("-------------------------------------------------")

                    id_producto_buscar = int(input(Main.mensajes["insert_product_id_select"]))
                    producto_seleccionado = Producto.seleccionarProducto(id_producto_buscar)

                    if producto_seleccionado != None:
                        print(Main.mensajes["select_product_menu"])
                        opcionSeleccionada = int(input("\n-> "))

                        if opcionSeleccionada == 1:
                            # Agregar a lista de deseos
                            info_lista_deseos = Main.usuario_actual.agregar_lista_deseos(producto_seleccionado,
                                                                                         Main.mensajes)
                            print(info_lista_deseos["mensaje"])
                            input(Main.mensajes["go_back_press_any_key"])
                            Main.menuUsuariosOpciones()

                        elif opcionSeleccionada == 2:
                            # Agregar a carrito de compras
                            if Main.pedido_pendiente == None:
                                Main.pedido_pendiente = Pedido(datetime.date.today(), Main.usuario_actual)

                            print(Main.mensajes["product_quantity"])
                            cantidad_venta = int(input("\n-> "))

                            resultado = Pedido_Producto.agregarProductoACarritoCompras(cantidad_venta,
                                                                                       Main.pedido_pendiente,
                                                                                       producto_seleccionado,
                                                                                       Main.mensajes)

                            print(resultado["mensaje"])
                            input(Main.mensajes["go_back_press_any_key"])
                            Main.menuUsuariosOpciones()

                        else:
                            Main.menuUsuariosOpciones()
                            pass

                    else:
                        print(Main.mensajes["product_not_found"])
                        input(Main.mensajes["go_back_press_any_key"])
                        Main.menuUsuariosOpciones()

            elif opcionSeleccionada == 3:
                # Crear comentario
                listaproductoscomentar = Pedido.productosAcomentar(Main.usuario_actual)
                for producto_actual in listaproductoscomentar:
                    print("\n-------------------------------------------------")
                    print(producto_actual.toString(Main.mensajes))
                    print("-------------------------------------------------")

                idSeleccionado = int(input(Main.mensajes["id_to_comment"]))
                if Producto.validarIdEnListaproductosAcomentar(idSeleccionado, listaproductoscomentar):
                    descripcion = input(Main.mensajes["the_comment"])
                    comentario = Comentario(descripcion, Main.usuario_actual,
                                            Producto.seleccionarProducto(idSeleccionado))

                else:
                    print(Main.mensajes["product_not_found"])

                input(Main.mensajes["go_back_press_any_key"])
                Main.menuUsuariosOpciones()

            elif opcionSeleccionada == 4:
                # Ver carrito de compras
                if Main.pedido_pendiente != None and len(Main.pedido_pendiente.getPedidoProductos()) > 0:
                    print(Main.mensajes["wish_list_carrito"])
                    print(Main.pedido_pendiente.toStringProductosCarrito(Main.mensajes))

                    # Menu del carrito de compras
                    print(Main.mensajes["buy_menu"])
                    opcionSeleccionada = int(input("\n-> "))

                    if opcionSeleccionada == 1:
                        Main.pedido_pendiente.comprar()
                        Main.pedido_pendiente = None
                        print(Main.mensajes["order_successfully"])
                        Main.menuUsuariosOpciones()
                    elif opcionSeleccionada == 2:
                        id_borrar = int(input(Main.mensajes["insert_product_id_delete"]))
                        resultado = Pedido_Producto.borrarProductoDeCarritoCompras(id_borrar, Main.pedido_pendiente,
                                                                                   Main.mensajes)
                        print(resultado)
                        input(Main.mensajes["go_back_press_any_key"])
                        Main.menuUsuariosOpciones()
                    elif opcionSeleccionada == 3:
                        Main.menuUsuariosOpciones()
                else:
                    print(Main.mensajes["empty_shopping_cart"])
                    input(Main.mensajes["go_back_press_any_key"])
                    Main.menuUsuariosOpciones()

            elif opcionSeleccionada == 5:
                # Ver lista de deseados
                if len(Main.usuario_actual.getListaDeseos()) == 0:
                    print(Main.mensajes["empty_wish_list"])
                    input(Main.mensajes["go_back_press_any_key"])
                    Main.menuUsuariosOpciones()

                else:
                    print(Main.mensajes["wish_list"])
                    lista_deseos = Main.usuario_actual.getListaDeseos()
                    for producto_actual in lista_deseos:
                        print("\n-------------------------------------------------")
                        print(producto_actual.toString(Main.mensajes))
                        print("-------------------------------------------------")

                    print(Main.mensajes["wish_list_menu"])
                    opcion_seleccionada = int(input("\n-> "))

                    if opcion_seleccionada == 1:
                        # Comprar (Lista de deseados)
                        id_producto_agregar = int(input(Main.mensajes["insert_product_id_buy"]))
                        producto_seleccionado = Producto.seleccionarProducto(id_producto_agregar)
                        if producto_seleccionado != None:
                            for prod_actual in Main.usuario_actual.getListaDeseos():
                                if prod_actual.getId() == id_producto_agregar:
                                    if Main.pedido_pendiente == None:
                                        Main.pedido_pendiente = Pedido(datetime.date.today(), Main.usuario_actual)

                                    print(Main.mensajes["product_quantity"])
                                    cantidad_venta = int(input("\n-> "))

                                    resultado = Pedido_Producto.agregarProductoACarritoCompras(cantidad_venta,
                                                                                               Main.pedido_pendiente,
                                                                                               producto_seleccionado,
                                                                                               Main.mensajes)

                                    print(resultado["mensaje"])
                                    input(Main.mensajes["go_back_press_any_key"])
                                    Main.menuUsuariosOpciones()
                                else:
                                    print(Main.mensajes["product_not_found_in_wish_list"])
                                    input(Main.mensajes["go_back_press_any_key"])
                                    Main.menuUsuariosOpciones()
                        else:
                            print(Main.mensajes["product_not_found"])
                            input(Main.mensajes["go_back_press_any_key"])
                            Main.menuUsuariosOpciones()

                    elif opcion_seleccionada == 2:
                        # Eliminar producto (Lista de deseados)
                        lista_deseos = Main.usuario_actual.getListaDeseos()
                        producto_eliminado = False
                        producto_a_eliminar = int(input(Main.mensajes["insert_product_id_delete"]))
                        for producto_en_lista in lista_deseos:
                            if producto_en_lista.getId() == producto_a_eliminar:
                                lista_deseos.remove(producto_en_lista)
                                producto_eliminado = True
                        if producto_eliminado == True:
                            print(Main.mensajes["product_deleted"])
                        else:
                            print(Main.mensajes["product_not_found_in_wish_list"])

                        input(Main.mensajes["go_back_press_any_key"])
                        Main.menuUsuariosOpciones()
                    elif opcion_seleccionada == 3:
                        # Salir al menu
                        Main.menuUsuariosOpciones()

            elif opcionSeleccionada == 6:
                # Ver pedidos realizados
                if len(Pedido.pedidos) > 0:
                    print(Main.mensajes["previous_orders"])
                    for pedido_actual in Pedido.pedidos:
                        if pedido_actual.getEstado() == "Realizado" or pedido_actual.getEstado() == "Anulado":
                            print(pedido_actual.toString(Main.mensajes))
                else:
                    print(Main.mensajes["order_not_found"])

                input(Main.mensajes["go_back_press_any_key"])
                Main.menuUsuariosOpciones()

            elif opcionSeleccionada == 7:
                # Desconectarse
                Main.usuario_actual = None
                Main.menuPrincipal()

            else:
                # Opcion erronea
                print(Main.mensajes["wrong_option"])
                Main.menuUsuariosOpciones()

    @staticmethod
    def menuEmpleadosLog():
        # Menu de inicio de sesíon para empleados
        print("\n-----------------------------------------------------")
        print(Main.mensajes["employee_login_menu"])

        while Main.breakOpciones == 0:
            opcionSeleccionada = int(input("\n-> "))

            if opcionSeleccionada == 1:
                # Inicio de sesion (Empleados)
                Main.usuario_actual = Empleado()
                operacion_completada = {}

                email = input(Main.mensajes["email"])
                password = input(Main.mensajes["user_password"])

                Main.usuario_actual.setEmail(email)
                Main.usuario_actual.setPassword(password)

                operacion_completada = Main.usuario_actual.iniciar_sesion(Main.mensajes)

                if operacion_completada["exitoso"] == True:
                    print(operacion_completada["mensaje"])

                    if Main.usuario_actual.getAdmin() == True:
                        Main.menuEmpleadosAdminOpciones()
                    else:
                        Main.menuEmpleadosOpciones()
                else:
                    print(operacion_completada["mensaje"])
                    Main.menuEmpleadosLog()
            else:
                Main.menuPrincipal()

    @staticmethod
    def menuEmpleadosAdminOpciones():
        print("\n-----------------------------------------------------")
        print("\nBienvenid@ " + Main.usuario_actual.getNombre() + "\n" + Main.mensajes["admin_menu"])

        while Main.breakOpciones == 0:
            opcionSeleccionada = int(input("\n-> "))
            resultado_operacion = None

            if opcionSeleccionada == 1 or opcionSeleccionada == 2:
                # Crear empleado o administrador
                print(Main.mensajes["enter_data_employee"])

                nombre = input(Main.mensajes["user_name"])
                email = input(Main.mensajes["email"])
                password = input(Main.mensajes["user_password"])
                telefono = input(Main.mensajes["user_phone"])
                direccion = input(Main.mensajes["user_address"])
                admin = opcionSeleccionada == 1

                nuevo_empleado = Empleado(nombre, email, password, telefono, direccion, admin)
                resultado_operacion = nuevo_empleado.guardarEmpleadoTxt(Main.mensajes)

            elif opcionSeleccionada == 3:
                # Cambiar el estado de los empleados
                for empleado in Empleado.empleados:
                    if empleado.getEmail() != Main.usuario_actual.getEmail():
                        print(empleado.toString(Main.mensajes))
                        print("------------------------------------------")

                id_empleado = int(input(Main.mensajes["insert_employee_id"]))
                resultado_operacion = Empleado.cambiarEstadoEmpleado(id_empleado, Main.mensajes)

            else:
                Main.menuEmpleadosOpciones(3, opcionSeleccionada)

            print(resultado_operacion["mensaje"])
            Main.menuEmpleadosAdminOpciones()

    @staticmethod
    def menuEmpleadosOpciones(opcion_inicial = 0, opcionSeleccionada = 0):
        if opcionSeleccionada == 0:
            print("\nBienvenid@ " + Main.usuario_actual.getNombre() + "\n" + Main.mensajes["employee_menu"])

        while Main.breakOpciones == 0:
            if opcionSeleccionada == 0:
                opcionSeleccionada = int(input("\n-> "))

            if opcionSeleccionada == (1 + opcion_inicial):
                # Crear productos (Empleado)
                print(Main.mensajes["enter_product_info"])
                nombre_producto = input(Main.mensajes["user_name"])
                valor_producto = float(input(Main.mensajes["value"]))
                descripcion_producto = input(Main.mensajes["description"])
                cantidad_inventario_producto = int(input(Main.mensajes["amount_inventory"]))

                producto = Producto(nombre_producto, valor_producto,
                                    descripcion_producto, cantidad_inventario_producto)
                print(producto.validarExistenciaEnLista(Main.mensajes))


            elif opcionSeleccionada == (2 + opcion_inicial):
                # Buscar productos por palabra (Empleado)
                nombre_producto = input(Main.mensajes["product_to_search"])
                lista_productos_buscados = Producto.buscarProductoNombre(nombre_producto)

                if len(lista_productos_buscados) > 0:
                    for producto_actual in lista_productos_buscados:
                        print("\n-------------------------------------------------")
                        print(producto_actual.toString(Main.mensajes))
                        print("-------------------------------------------------")
                    input(Main.mensajes["go_back_press_any_key"])
                else:
                    print(Main.mensajes["product_not_found"])

            elif opcionSeleccionada == (3 + opcion_inicial):
                # Actualizar productos (Empleado)

                for producto_actual in Producto.productos:
                    print("\n-------------------------------------------------")
                    print(producto_actual.toString(Main.mensajes))
                    print("-------------------------------------------------")

                id_producto_buscar = int(input(Main.mensajes["insert_product_id_update"]))
                producto_seleccionado = Producto.seleccionarProducto(id_producto_buscar)

                # Para saber si se devolvio algun producto de la seleccion por ID
                if producto_seleccionado != None:

                    print(Main.mensajes["enter_product_info"])
                    nombre_producto = input(Main.mensajes["user_name"])
                    valor_producto = float(input(Main.mensajes["value"]))
                    descripcion_producto = input(Main.mensajes["description"])
                    cantidad_inventario_producto = int(input(Main.mensajes["amount_inventory"]))

                    producto_seleccionado.actualizarProducto(nombre_producto, valor_producto, descripcion_producto,
                                                             cantidad_inventario_producto)
                    print(Main.mensajes["product_updated"])


                else:
                    print(Main.mensajes["product_not_found"])

            elif opcionSeleccionada == (4 + opcion_inicial):
                # Eliminar producto de la lista de productos (Empleado)
                for producto_actual in Producto.productos:
                    print("\n-------------------------------------------------")
                    print(producto_actual.toString(Main.mensajes))
                    print("-------------------------------------------------")

                id_producto_borrar = int(input(Main.mensajes["insert_product_id_delete"]))
                print(Producto.borrarProducto(id_producto_borrar, Main.mensajes))

            elif opcionSeleccionada == (5 + opcion_inicial):
                # Anular pedidos
                for pedido_actual in Pedido.pedidos:
                    if pedido_actual.getEstado() != "Anulado":
                        print(pedido_actual.toString(Main.mensajes))

                id_pedido_anular = int(input(Main.mensajes["id_order_to_cancel"]))
                resultado = Pedido.anularPedido(id_pedido_anular, Main.mensajes)
                print(resultado)

            elif opcionSeleccionada == (6 + opcion_inicial):
                # Ver pedidos del dia
                for pedido_actual in Pedido.pedidos:
                    if pedido_actual.getFecha() == datetime.date.today():
                        print(pedido_actual.toString(Main.mensajes))

            elif opcionSeleccionada == (7 + opcion_inicial):
                # Promedio y total de ventas del día
                promedio_ventas_dia = Pedido.valorPromedioYTotalVentasDia()

                if promedio_ventas_dia["promedio"] == 0:
                    print(Main.mensajes["no_orders_day"])
                else:
                    print(Main.mensajes["average_sales"] + str(promedio_ventas_dia["promedio"]))
                    print(Main.mensajes["total_sales"] + str(promedio_ventas_dia["total"]))

            elif opcionSeleccionada == (8 + opcion_inicial):
                # Desconectarse (Empleado)
                Main.usuario_actual = None
                Main.menuPrincipal()

            if opcion_inicial == 0:
                Main.menuEmpleadosOpciones()
            else:
                Main.menuEmpleadosAdminOpciones()


if __name__ == "__main__":
    Main.setIdioma()
