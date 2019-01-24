from Persona import Persona
from Mensajes import Mensajes

class Main:
	personas = []

	@staticmethod
	def setIdioma():
		print("""
			1. Español
			2. Inglés
		""")

		lang = int(input())

		if lang == 2:
			return Mensajes.mensajes_eng

		return Mensajes.mensajes_es

	@staticmethod
	def menu():
		sw = 1
		lang = Main.setIdioma()
		
		while sw == 1:
			print(lang["welcome"])
			print(lang["login"])
			print(lang["sign_up"])
			print(lang["exit"])
			print(lang["menu_msg"])

			opcion = int(input())

			if opcion == 1:
				 print(Persona.iniciar_sesion(lang))

			elif opcion == 2:				
				Persona.registrarse(persona)
				
			elif opcion == 3:
				sw = 0
			else:
				print(lang["wrong_option"])

if __name__ == "__main__":
	Main.menu()