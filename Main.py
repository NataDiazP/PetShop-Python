import datetime
from Persona import Persona
from Producto import Producto
from Empleado import Empleado
from Mensajes import Mensajes
from Comentario import Comentario
from Pedido import Pedido
from Pedido_Producto import Pedido_Producto
from Util import  Util

class Main:
    usuario_actual = None
    mensajes = None
    datos_ficticios_agregados = 0
    datos_ficticios_txt_agregados = 0
    breakOpciones = 0
    pedido_pendiente = None

    @staticmethod
    def setIdioma():

        print("\nLanguage:\n\n1. Español\n2. Inglés")

        lang = int(input("\n-> "))

        if lang == 1:
            Main.mensajes = Mensajes.mensajes_es
        elif lang == 2:
            Main.mensajes = Mensajes.mensajes_eng

        Main.menuPrincipal()

    @staticmethod
    def menuPrincipal():
        print("\n-----------------------------------------------------")
        print(Main.mensajes["welcome_menu"])

        while Main.breakOpciones == 0:
            opcionSeleccionada = int(input("\n-> "))
            if opcionSeleccionada == 1:
                if Main.datos_ficticios_agregados == 0:
                    Util.generarDatosFicticios()
                    print(Main.mensajes["succes_dummy_data"])
                    Main.datos_ficticios_agregados = 1
                else:
                    print(Main.mensajes["dummy_data_added"])

                Main.menuPrincipal()

            elif opcionSeleccionada == 2:
                if Main.datos_ficticios_txt_agregados == 0:
                    Util.generarDatosFicticiosTxt()
                    print(Main.mensajes["succes_dummy_data"])
                    Main.datos_ficticios_txt_agregados = 1
                else:
                    print(Main.mensajes["dummy_data_added"])

                Main.menuPrincipal()

            elif opcionSeleccionada == 3:
                print("\n-----------------------------------------------------")
                print(Main.mensajes["user_type"])

                while Main.breakOpciones == 0:

                    opcionSeleccionada = int(input("\n-> "))

                    if opcionSeleccionada == 1:
                        Main.menuUsuariosLogReg()
                    elif opcionSeleccionada == 2:
                        Main.menuEmpleados()
                    elif opcionSeleccionada == 3:
                        Main.menuPrincipal()
                    else:
                        print(Main.mensajes["wrong_option"])

            elif opcionSeleccionada == 4:

                exit()

            else:

                print(Main.mensajes["wrong_option"])

    @staticmethod
    def menuUsuariosLogReg():
        print("\n-----------------------------------------------------")
        print(Main.mensajes["client_login_menu"])

        while Main.breakOpciones == 0:
            opcionSeleccionada = int(input("\n-> "))

            if opcionSeleccionada == 1 or opcionSeleccionada == 2:
                Main.usuario_actual = Persona()
                operacion_completada = {}

                if opcionSeleccionada == 1:
                    email = input(Main.mensajes["email"])
                    password = input(Main.mensajes["user_password"])

                    Main.usuario_actual.setEmail(email)
                    Main.usuario_actual.setPassword(password)

                    operacion_completada = Main.usuario_actual.iniciar_sesion(Main.mensajes)

                elif opcionSeleccionada == 2:

                    nombre = input(Main.mensajes["user_name"])
                    email = input(Main.mensajes["email"])
                    telefono = input(Main.mensajes["user_phone"])
                    direccion = input(Main.mensajes["user_address"])
                    password = input(Main.mensajes["user_password"])

                    operacion_completada = Main.usuario_actual.registrarse(nombre, email, telefono, direccion, password, Main.mensajes)

                if operacion_completada["exitoso"] == True:
                    print(operacion_completada["mensaje"])
                    Main.menuUsuariosOpciones()

                else:
                    print(operacion_completada["mensaje"])
                    Main.menuUsuariosLogReg()

            elif opcionSeleccionada == 3:
                Main.menuPrincipal()

            else:
                print(Main.mensajes["wrong_option"])

    @staticmethod
    def menuUsuariosOpciones():
        print("\n-----------------------------------------------------")
        print("\n" + Main.usuario_actual.getNombre() + Main.mensajes["client_menu"])

        while Main.breakOpciones == 0:
            opcionSeleccionada = int(input("\n-> "))

            if opcionSeleccionada == 1:
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
                            info_lista_deseos = Main.usuario_actual.agregar_lista_deseos(producto_seleccionado, Main.mensajes)
                            print(info_lista_deseos["mensaje"])
                            input(Main.mensajes["go_back_press_any_key"])
                            Main.menuUsuariosOpciones()

                        elif opcionSeleccionada == 2:
                            #Agregar a carrito de compras
                            if Main.pedido_pendiente == None:
                                Main.pedido_pendiente = Pedido(datetime.date.today(), Main.usuario_actual)

                            print(Main.mensajes["product_quantity"])
                            cantidad_venta = int(input("\n-> "))

                            resultado = Pedido_Producto.agregarProductoACarritoCompras(cantidad_venta, Main.pedido_pendiente,
                                                                                         producto_seleccionado, Main.mensajes)

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

                listaproductoscomentar = Pedido.productosAcomentar(Main.usuario_actual)
                for producto_actual in listaproductoscomentar:
                    print("\n-------------------------------------------------")
                    print(producto_actual.toString(Main.mensajes))
                    print("-------------------------------------------------")

                idSeleccionado= int (input(Main.mensajes["id_to_comment"]))
                if Producto.validarIdEnListaproductosAcomentar(idSeleccionado,listaproductoscomentar):
                    descripcion=input(Main.mensajes["the_comment"])
                    comentario = Comentario(descripcion, Main.usuario_actual, Producto.seleccionarProducto(idSeleccionado))

                else:
                    print(Main.mensajes["product_not_found"])

                input(Main.mensajes["go_back_press_any_key"])
                Main.menuUsuariosOpciones()



            elif opcionSeleccionada == 4:

                if Main.pedido_pendiente != None and len(Main.pedido_pendiente.getPedidoProductos()) > 0:
                    print(Main.mensajes["wish_list_carrito"])
                    print(Main.pedido_pendiente.toStringProductosCarrito(Main.mensajes))

                    # Menu carrito de compras
                    print(Main.mensajes["buy_menu"])
                    opcionSeleccionada = int(input("\n-> "))

                    if opcionSeleccionada == 1:
                        Main.pedido_pendiente.comprar()
                        Main.pedido_pendiente = None
                        print(Main.mensajes["order_successfully"])
                        Main.menuUsuariosOpciones()
                    elif opcionSeleccionada == 2:
                        id_borrar = int(input(Main.mensajes["insert_product_id_delete"]))
                        resultado = Pedido_Producto.borrarProductoDeCarritoCompras(id_borrar,Main.pedido_pendiente,Main.mensajes)
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

                print(Main.mensajes["wish_list"])
                lista_deseos = Main.usuario_actual.getListaDeseos()
                for producto_actual in lista_deseos:
                    print("\n-------------------------------------------------")
                    print(producto_actual.toString(Main.mensajes))
                    print("-------------------------------------------------")


            elif opcionSeleccionada == 6:
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
                Main.usuario_actual = None
                Main.menuPrincipal()

            else:
                print(Main.mensajes["wrong_option"])
                Main.menuUsuariosOpciones()

    @staticmethod
    def menuEmpleados():
        print("\n-----------------------------------------------------")
        print(Main.mensajes["employee_login_menu"])

        while Main.breakOpciones == 0:
            opcionSeleccionada = int(input("\n-> "))

            if opcionSeleccionada == 1:
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
                    Main.menuEmpleados()
            else:
                Main.menuPrincipal()

    @staticmethod
    def printEmpleados():
        for empleado in Empleado.empleados:
            if empleado.getEmail() != Main.usuario_actual.getEmail():
                print(empleado.toString(Main.mensajes))
                print("------------------------------------------")

    @staticmethod
    def menuEmpleadosAdminOpciones():
        print("\n-----------------------------------------------------")
        print("\nBienvenid@ " + Main.usuario_actual.getNombre() + "\n" + Main.mensajes["admin_menu"])

        while Main.breakOpciones == 0:
            opcionSeleccionada = int(input("\n-> "))
            resultado_operacion = None

            if opcionSeleccionada == 1 or opcionSeleccionada == 2:
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
                Main.printEmpleados()

                id_empleado = int(input(Main.mensajes["insert_employee_id"]))
                resultado_operacion = Empleado.cambiarEstadoEmpleado(id_empleado, Main.mensajes)

            else:
                Main.menuEmpleadosOpciones(3, opcionSeleccionada)

            print(resultado_operacion["mensaje"])
            Main.menuEmpleadosAdminOpciones()

    @staticmethod
    def menuEmpleadosOpciones(opcion_inicial = 0, opcionSeleccionada = 0):
        print("\n-----------------------------------------------------")
        if opcionSeleccionada == 0:
            print("\nBienvenid@ " + Main.usuario_actual.getNombre() + "\n" + Main.mensajes["employee_menu"])

        while Main.breakOpciones == 0:
            if opcionSeleccionada == 0:
                opcionSeleccionada = int(input("\n-> "))

            if opcionSeleccionada == (1 + opcion_inicial):
                print(Main.mensajes["enter_product_info"])
                nombre_producto = input(Main.mensajes["user_name"])
                valor_producto = float(input(Main.mensajes["value"]))
                descripcion_producto = input(Main.mensajes["description"])
                cantidad_inventario_producto = int(input(Main.mensajes["amount_inventory"]))

                producto = Producto(nombre_producto, valor_producto,
                                    descripcion_producto, cantidad_inventario_producto)
                print(producto.validarExistenciaEnLista(Main.mensajes))


            elif opcionSeleccionada == (2 + opcion_inicial):
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
                id_producto_buscar = int(input(Main.mensajes["insert_product_id"]))
                producto_seleccionado = Producto.seleccionarProducto(id_producto_buscar)

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
                id_producto_borrar = int(input(Main.mensajes["insert_product_id"]))
                print(Producto.borrarProducto(id_producto_borrar, Main.mensajes))

            elif opcionSeleccionada == (5 + opcion_inicial):
                # Anular pedidos
                for pedido_actual in Pedido.pedidos:
                    if pedido_actual.getEstado() != "Anulado":
                        print(pedido_actual.toString(Main.mensajes))

                id_pedido_anular = int(input(Main.mensajes["id_order_to_cancel"]))
                resultado = Pedido.anularPedido(id_pedido_anular,Main.mensajes)
                print(resultado)


            elif opcionSeleccionada == (6 + opcion_inicial):
                for pedido_actual in Pedido.pedidos:
                    if pedido_actual.getFecha() == datetime.date.today():
                        print(pedido_actual.toString(Main.mensajes))


            elif opcionSeleccionada == (7 + opcion_inicial):
                Main.usuario_actual = None
                Main.menuPrincipal()

            if opcion_inicial == 0:
                Main.menuEmpleadosOpciones()
            else:
                Main.menuEmpleadosAdminOpciones()

if __name__ == "__main__":
    Main.setIdioma()
