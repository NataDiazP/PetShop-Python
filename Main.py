from Persona import Persona

opcion = int(input("Bienvenido a PetShop.\n\n1) Iniciar sesión\n2) Registrarse\n3) Salir\n\nSeleccione una opcion: "))


while opcion > 3 or opcion < 1:
    opcion=int(input("\nOpcion invalida, por favor seleccione nuevamente una opcion: "))
  
if opcion == 1 or opcion == 2:
    
    usuario_actual = Persona()
    
    if opcion == 1:
        
        usuario_actual.iniciar_sesion()

    else:
        usuario_actual.registrarse()



elif opcion == 3:
        
    exit
        


