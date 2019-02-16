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
        p1 = Producto("Collar para perro", 10000, "Un bonito collar verde para perro ", 20)
        p2 = Producto("Gimnasio para gato", 54000, "Una cosa de locos")
        p3 = Producto("Chunky", 2300, "para gatos fit ", 100)

        Producto.productos.append(p1)
        Producto.productos.append(p2)
        Producto.productos.append(p3)


        u1 = Persona("prueba", "prueba@gmail.com", "123", "123", "123")

        Persona.personas.append(u1)
