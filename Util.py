import datetime
from Empleado import Empleado
from Producto import Producto
from Persona import Persona
from Pedido import Pedido
from Comentario import Comentario
from Pedido_Producto import Pedido_Producto

class Util:

    @staticmethod
    def generarDatosFicticiosTxt():
        # Metodo para generar los datos ficticios desde el archivo txt "empleados.txt"
        archivo = open("empleados.txt", "r")
        # Leemos una a una las lineas del archivo
        for linea in archivo:
            # Guardamos una lista de partir las lineas por ;
            datos = linea.split(";")

            # Creamos un objeto con todos los datos leidos de cada una de las lineas
            empleado = Empleado(datos[0], datos[1], datos[2], datos[3], datos[4], bool(datos[5]), bool(datos[6]))
            Empleado.empleados.append(empleado)

        archivo.close()

    @staticmethod
    def generarDatosFicticios():
        # Metodo para generar los datos ficticios
        u1 = Persona("Prueba", "prueba@gmail.com", "3089647558", "Avenida siempre viva", "123")
        u2 = Persona("Prueba2", "prueba2@gmail.com", "4541694", "Cerro el volador", "123")

        p1 = Producto("Lana de oveja virgen", 10000, "Bufandas?", 20)
        p2 = Producto("Bigotes de lemur lampiño", 2300, "Calvo pero serio", 100)
        p3 = Producto("Aceite omega 3 de bagre", 50000, "Del cauca lo mejor", 5)
        p4 = Producto("Colita de Pinscher", 1000000, "Recien cortada", 1)
        p5 = Producto("Caminador para tortuga", 30000, "Useless", 50)

        c1 = Comentario("Me sirvio para rebajar.", u1, p3)
        c2 = Comentario("No sirve para nada!!!!!!!!.", u2, p3)
        c3 = Comentario("Me hice tremendo almuerzo con esto.", u1, p4)

        ped1 = Pedido(datetime.date.today(), u1, 0, "Pendiente")

        ped_pro1 = Pedido_Producto(5, ped1, p1)
        ped_pro2 = Pedido_Producto(10, ped1, p2)
        ped_pro3 = Pedido_Producto(2, ped1, p3)
        ped_pro4 = Pedido_Producto(1, ped1, p4)
        ped_pro5 = Pedido_Producto(30, ped1, p5)

        ped1.calcularValorTotal()
        ped1.comprar()

        Persona.personas.append(u1)
        Persona.personas.append(u2)

        Producto.productos.append(p1)
        Producto.productos.append(p2)
        Producto.productos.append(p3)
        Producto.productos.append(p4)
        Producto.productos.append(p5)
