#!/usr/bin/env python3

class Persona:
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        

    def saludo(self):
        print(f"\n[+] Tu nombre es {self.nombre}, tienes {self.edad} años y eres de género {self.sexo}.\n")


 # Datos de usuario
datos_usuario = input("Dime tu nombre: ")
edad_usuario = input("Dime tu edad: ").replace(",", ".")

try:
    # Intentar convertir a float
    edad_float = float(edad_usuario)
    # Comprobar si es entero
    if not edad_float.is_integer():
        print("No puedes poner un número con decimales en tu edad.")
        exit()
    edad_usuario = int(edad_float)
except ValueError:
    print("La edad debe ser un número entero.")
    exit()

sexo_usuario = input("Dime tu sexo: ")

# Sustituir género por sexo
if sexo_usuario.lower() == "masculino":
    sexo_usuario = "hombre"
elif sexo_usuario.lower() == "femenino":
    sexo_usuario = "mujer"
else:
    sexo_usuario = "otro"

persona = Persona(datos_usuario, edad_usuario, sexo_usuario)
persona.saludo()