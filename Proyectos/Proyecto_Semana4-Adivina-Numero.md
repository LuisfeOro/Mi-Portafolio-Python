# Proyecto Semana 4: Adivinador de Numero
## Hola, me llamo Luis y les estare presentando mi cuarto Proyecto del curso de Python de la Academa Fibonnacci

En el siguiente proyecto el objetivo principal es realizar un programa que genere un numero secreto, y se le solicite al usuario adivinarlo con un limite de vidas

- - - 
## Adivinador de Numero

```
#Input y nombre por default
#Instrucciones
#Variables de maximo y minimo, 1 y 100
#Intendos, VIDAS 8
#Necesitamos random para obtene run numero entre 1 y 100
#Contador de intentos
#While para hacer que el juego funcione mientras tenga vidas
#If para verificar si acerto o no

#Bibliotecas con funciones especiales.
from random import randint
#Saludo e inicio del juego
nombre = input("Cual es tu nombre? ")
print(f"Bueno, {nombre}, he pensado en numero entre 1 y 100.")
print("Tienes solo 8 intentos para adivinar")

#Numero secreto aleatorio
numero_secreto = randint(1,100)
print(numero_secreto)
intentos = 0
vidas = 0
max_intentos = 8

#Ciclo de intentos
while vidas < max_intentos:
    intentos = int(input("Ingresa un valor entre 1 y 100: "))
    if intentos <1 or intentos>100:
        print("Numero no permitido")
    elif intentos < numero_secreto:
        print("Incorrecto, el numero secreto es mayor")
    elif intentos > numero_secreto:
        print("Incorrecto, el numero secreto es menor")
    else:
        print(f"Haz ganado, el numero secreto era {numero_secreto}")
        break

    vidas += 1
    #Vidas se va a ir incrementando

```

[Adivinador Numero](https://github.com/LuisfeOro/Mi-Portafolio-Python/blob/main/Proyectos/proyecto_semana4-Adivina-Numero.py)

Muchas gracias
