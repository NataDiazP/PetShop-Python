import datetime
from Persona import Persona
from Producto import Producto
from Empleado import Empleado
from Mensajes import Mensajes
from Comentario import Coment
from Pedido import Pedido
from Pedido_Producto import Pedido_Producto

class Main:
    usuario_actual = None
    personas = []
    productos = []
    empleados = []
    mensajes = None
    datos_ficticios_agregados = 0
    datos_ficticios_txt_agregados = 0
    breakOpciones = 0

    @staticmethod
    def setIdioma():

        print("""
			1. Español
			2. Inglés
		""")

        lang = int(input("\n-> "))

        if lang == 1:
            Main.mensajes = Mensajes.mensajes_es
        elif lang == 2:
            Main.mensajes = Mensajes.mensajes_eng

        Main.menuPrincipal()

    @staticmethod
    def menuPrincipal():
        print(Main.mensajes["welcome_menu"])

        while Main.breakOpciones == 0:
            opcionSeleccionada = int(input("\n-> "))
            if opcionSeleccionada == 1:
                if Main.datos_ficticios_agregados == 0:
                    Main.datosFicticios()
                    print(Main.mensajes["succes_dummy_data"])
                    Main.datos_ficticios_agregados = 1
                else:
                    print(Main.mensajes["dummy_data_added"])

                Main.menuPrincipal()

            elif opcionSeleccionada == 2:
                if Main.datos_ficticios_txt_agregados == 0:
                    Main.generarDatosFicticiosTxt()
                    print(Main.mensajes["succes_dummy_data"])
                    Main.datos_ficticios_txt_agregados = 1
                else:
                    print(Main.mensajes["dummy_data_added"])

                print(Main.datos_ficticios_txt_agregados)

                Main.menuPrincipal()
            elif opcionSeleccionada == 3:

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

                    operacion_completada = Main.usuario_actual.iniciar_sesion(Main.personas, Main.mensajes)

                elif opcionSeleccionada == 2:

                    nombre = input(Main.mensajes["user_name"])
                    email = input(Main.mensajes["email"])
                    telefono = input(Main.mensajes["user_phone"])
                    direccion = input(Main.mensajes["user_address"])
                    password = input(Main.mensajes["user_password"])

                    operacion_completada = Main.usuario_actual.registrarse(nombre, email, telefono, direccion, password, Main.personas,
                                                                      Main.mensajes)

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

        print("\n" + Main.usuario_actual.getNombre() + Main.mensajes["client_menu"])

        while Main.breakOpciones == 0:
            opcionSeleccionada = int(input("\n-> "))

            if opcionSeleccionada == 1:
                if len(Main.productos) == 0:
                    print(Main.mensajes["product_not_found"])
                    input(Main.mensajes["go_back_press_any_key"])
                    Main.menuUsuariosOpciones()

                else:

                    for producto_actual in Main.productos:
                        print("------------------------------------------")
                        print(producto_actual.listarProductos(Main.mensajes))
                        print("------------------------------------------")

                    input(Main.mensajes["go_back_press_any_key"])
                    Main.menuUsuariosOpciones()

            elif opcionSeleccionada == 2:
                if len(Main.productos) == 0:

                    print(Main.mensajes["product_not_found"])
                    input(Main.mensajes["go_back_press_any_key"])
                    Main.menuUsuariosOpciones()

                else:
                    id_producto_buscar = int(input(Main.mensajes["insert_product_id"]))
                    producto_seleccionado = Producto.seleccionarProducto(id_producto_buscar, Main.productos)

                    if producto_seleccionado != None:
                        print(Main.mensajes["select_product_menu"])
                        opcionSeleccionada = int(input("\n-> "))

                        if opcionSeleccionada == 1:
                            info_lista_deseos = Main.usuario_actual.agregar_lista_deseos(producto_seleccionado, Main.mensajes)
                            print(info_lista_deseos["mensaje"])
                            input(Main.mensajes["go_back_press_any_key"])
                            Main.menuUsuariosOpciones()

                        elif opcionSeleccionada == 2:
                            pedido1=Pedido(datetime.date.today(), Main.usuario_actual)
                            cantidadventa = input(Main.mensajes["howmanyunities"])
                            if producto_seleccionado.getCantidadInventario() >= cantidadventa:
                                pedidoproducto1 = Pedido_Producto(cantidadventa, pedido1, producto_seleccionado)
                            info_lista_carrito = Main.usuario_actual.agregar_lista_carrito(producto_seleccionado, Main.mensajes, cantidadventa)
                            print(info_lista_carrito["mensaje"])
                            input(Main.mensajes["go_back_press_any_key"])
                            Main.menuUsuariosOpciones()

                        else:
                            Main.menuUsuariosOpciones()
                            pass

                    else:
                        print(Main.mensajes["product_not_found"])
                        input(Main.mensajes["go_back_press_any_key"])
                        Main.menuUsuariosOpciones()

            elif opcionSeleccionada == 4:
                print(Main.mensajes["wish_list_carrito"])
                lista_carrito = Main.usuario_actual.getListaCarrito()
                for producto_actual in lista_carrito:
                    print("------------------------------------------")
                    print(producto_actual.listarProductos(Main.mensajes))
                    print("------------------------------------------")
                opcionSeleccionada = input(Main.mensajes["make_order"])
                while Main.breakOpciones == 0:

                    if opcionSeleccionada == 1:
                        print("total compra = "+ valortotalcompra)
                input(Main.mensajes["go_back_press_any_key"])
                Main.menuUsuariosOpciones()


            elif opcionSeleccionada == 5:
                print(Main.mensajes["wish_list"])
                lista_deseos = Main.usuario_actual.getListaDeseos()
                for producto_actual in lista_deseos:
                    print("------------------------------------------")
                    print(producto_actual.listarProductos(Main.mensajes))
                    print("------------------------------------------")
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

                operacion_completada = Main.usuario_actual.iniciar_sesion(Main.empleados, Main.mensajes)

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
        for empleado in Main.empleados:
            if empleado.getEmail() != Main.usuario_actual.getEmail():
                print(empleado.listarEmpleado(Main.mensajes))
                print("------------------------------------------")

    @staticmethod
    def menuEmpleadosAdminOpciones():
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
                resultado_operacion = nuevo_empleado.crearEmpleado(Main.empleados, Main.mensajes)

            elif opcionSeleccionada == 3:
                Main.printEmpleados()

                id_empleado = int(input(Main.mensajes["insert_employee_id"]))
                resultado_operacion = Empleado.cambiarEstadoEmpleado(id_empleado, Main.empleados, Main.mensajes)

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
                print(Main.mensajes["enter_product_info"])
                nombre_producto = input(Main.mensajes["user_name"])
                valor_producto = float(input(Main.mensajes["value"]))
                descripcion_producto = input(Main.mensajes["description"])
                cantidad_inventario_producto = int(input(Main.mensajes["amount_inventory"]))

                producto = Producto(nombre_producto, valor_producto,
                                    descripcion_producto, cantidad_inventario_producto)
                print(producto.crearProducto(Main.productos, Main.mensajes))

                input(Main.mensajes["go_back_press_any_key"])

            elif opcionSeleccionada == (2 + opcion_inicial):
                nombre_producto = input(print(Main.mensajes["product_to_search"]))
                lista_productos_buscados = Producto.buscarProductoNombre(nombre_producto, Main.productos)

                if len(lista_productos_buscados) > 0:
                    for producto_actual in lista_productos_buscados:
                        print("------------------------------------------")
                        print(producto_actual.listarProductos(Main.mensajes))
                        print("------------------------------------------")
                    input(Main.mensajes["go_back_press_any_key"])
                else:
                    print(Main.mensajes["product_not_found"])
                    input(Main.mensajes["go_back_press_any_key"])

            elif opcionSeleccionada == (3 + opcion_inicial):
                id_producto_buscar = int(input(Main.mensajes["insert_product_id"]))
                producto_seleccionado = Producto.seleccionarProducto(id_producto_buscar, Main.productos)

                if producto_seleccionado != None:

                    print(Main.mensajes["enter_product_info"])
                    nombre_producto = input(Main.mensajes["user_name"])
                    valor_producto = float(input(Main.mensajes["value"]))
                    descripcion_producto = input(Main.mensajes["description"])
                    cantidad_inventario_producto = int(input(Main.mensajes["amount_inventory"]))

                    producto_seleccionado["objeto"].actualizarProducto(nombre_producto, valor_producto, descripcion_producto,
                                                                  cantidad_inventario_producto)
                    print(Main.mensajes["product_updated"])

                    input(Main.mensajes["go_back_press_any_key"])

                else:
                    print(Main.mensajes["product_not_found"])
                    input(Main.mensajes["go_back_press_any_key"])

            elif opcionSeleccionada == (4 + opcion_inicial):
                id_producto_borrar = int(input(Main.mensajes["insert_product_id"]))
                print(Producto.borrarProducto(id_producto_borrar, Main.productos, Main.mensajes))
                input(Main.mensajes["go_back_press_any_key"])

            # TODO: Añadir las tres opciones que faltan aqui

            elif opcionSeleccionada == (7 + opcion_inicial):
                Main.usuario_actual = None
                Main.menuPrincipal()

            if opcion_inicial == 0:
                Main.menuEmpleadosOpciones()
            else:
                Main.menuEmpleadosAdminOpciones()

    @staticmethod
    def generarDatosFicticiosTxt():
        archivo = open("empleados.txt", "r")

        for linea in archivo:
            datos = linea.split(";")

            empleado = Empleado(datos[0], datos[1], datos[2], datos[3], datos[4], bool(datos[5]), bool(datos[6]))
            Main.empleados.append(empleado)

        archivo.close()

    @staticmethod
    def datosFicticios():

        p1 = Producto("Collar para perro", 10000,
                      "Un bonito collar verde para perro ", 20)
        p2 = Producto("Gimnasio para gato", 54000, "Una cosa de locos", 50)
        p3 = Producto("Chunky", 2300, "para gatos fit ", 100)

        Main.productos.append(p1)
        Main.productos.append(p2)
        Main.productos.append(p3)

if __name__ == "__main__":
    Main.setIdioma()
