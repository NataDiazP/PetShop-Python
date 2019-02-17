from Empleado import Empleado
from Producto import Producto
from Persona import Persona

class Util:

    @staticmethod
    def generarDatosFicticiosTxt():
        archivo = open("empleados.txt", "r")

        for linea in archivo:
            datos = linea.split(";")

            empleado = Empleado(datos[0], datos[1], datos[2], datos[3], datos[4], bool(datos[5]), bool(datos[6]))
            Empleado.empleados.append(empleado)

        archivo.close()

    @staticmethod
    def generarDatosFicticios():
        p1 = Producto("Lana de oveja virgen", 10000, "Bufandas?", 20)
        p2 = Producto("Escroto de tigre afgano", 54000, "Reinel, por qué pusiste esto aqui?")
        p3 = Producto("Bigotes de lemur lampiño", 2300, "Calvo pero serio", 100)
        p4 = Producto("Aceite omega 3 de bagre", 50000, "Del cauca lo mejor", 5)
        p5 = Producto("Colita de Pinscher", 1000000, "Recien cortada", 1)
        p6 = Producto("Caminador para tortuga paralitica", 30000, "Useless", 50)


        Producto.productos.append(p1)
        Producto.productos.append(p2)
        Producto.productos.append(p3)
        Producto.productos.append(p4)
        Producto.productos.append(p5)
        Producto.productos.append(p6)


        u1 = Persona("prueba", "prueba@gmail.com", "123", "123", "123")

        Persona.personas.append(u1)
