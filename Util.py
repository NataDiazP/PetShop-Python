from Empleado import Empleado
from Producto import Producto

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
        p1 = Producto(nombre="Collar para perro", valor=10000, descripcion="Un bonito collar verde para perro")
        p2 = Producto(nombre="Gimnasio para gato", valor=54000, descripcion="Una cosa de locos ")

        Producto.productos.append(p1)
        Producto.productos.append(p2)
