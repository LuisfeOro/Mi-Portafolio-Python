"""
Ejercicio
Los mayores de edad pueden beber
Los mayores pueden entrar
Los mayores de 30 no pueden entrar a discotecas
Los de 20 y 35 tienen entrada gratis
"""

edad = int(input("Ingrese su Edad: "))
print(f"Puede beber: {edad>=18}")
print(f"Puede entrar: {edad>=18 and edad<=30}")
print(f"Tiene entrada gratis: {edad==20 or edad==25}")

diccionario = {True:"Si", False:"No"}
print(f"Puede beber: {diccionario[edad>=18]}")
print(f"Puede entrar: {diccionario[edad>=18 and edad<=30]}")
print(f"Tiene entrada gratis: {diccionario[edad==20 or edad==25]}")