# Proyecto Semana 5: Juego de Ahorcado
## Hola, me llamo Luis y les estare presentando mi quinto Proyecto del curso de Python de la Academa Fibonnacci

En el siguiente proyecto el objetivo principal es crear un programa que simule el juego de ahorcado.

El programa 

1. Una funcion generara una palabra al azar definida en un listado previo
2. Una funcoin convertira la palabra secreta en guiones, los cuales sera iran mostrando conforme se vayan adivinando las letras
3. Una funcion verificara que el texto ingresado sea parte del abecedario
4. Se le brindaran 7 vidas a nuestro usuario
5. Se imprimira un mensaje de bienvenida
6. Se generaran funciones en donde el usuario ingresara palabras y se validara si acierta o no
7. Se le restaran vidas si se equivoca y cuando llegue a 0 sera GAME OVER

- - - 
## Juego de Ahorcado

```
from random import choice

#Funcion para elegir la palabra al azar
def palabra_al_azar():
    return choice(["chile","calabaza","vestido","sandalias","responsabilidad","guatemala"])

print(palabra_al_azar())

#Funcion para convertir la palabra a guiones
def convertir_guiones(palabra_secreta):
    #Lista vacia []
    guiones = []
    for n in palabra_secreta:
        guiones.append("_")
    return guiones

palabra_secreta = palabra_al_azar()
print(palabra_secreta)
print(convertir_guiones(palabra_secreta))

#Funcion para verificar si se ingresa una letra
def verificar():
    letra = "%"
    while letra not in "abcdefghijklmnopqrstuvwxyz":
        letra = input("Ingresa una letra: ")

    return letra

#Comienzo del juego

palabra_secreta = list(palabra_al_azar())
guiones = convertir_guiones(palabra_secreta) #comparando letras con guones
lista_incorrectas = []
vidas = 7

print("""
BIENVENIDO AL JUEGO DEL AHORCADO
EL JUEGO TRATA DE QUE ADIVINESLAS PALABRAS
PUEDES ESCRIBIR UNA LETRA PARA DARTE UNA PISTA
EL JUEGO TE DIRA EN DONDE APARECE LA LETRA PARA REDUCIR LA PALABRA
TIENES 7 VIDAS
""")

#Ciclo infinito para poner letras
while True:
    intento = verificar()
    if intento in palabra_secreta:
        for n in range(len(palabra_secreta)):
            if intento == palabra_secreta[n]:
                guiones[n] = intento
                print(guiones)
        if guiones == palabra_secreta:
            print("Felicidades Adivinaste!")
            palabra = "".join(palabra_secreta)
            print(f"La palabra es {palabra}")
    else:
        lista_incorrectas.append(intento)
        print("Lista de intentos incorrectos")
        print(lista_incorrectas)
        vidas -= 1

        if vidas == 0:
            print("GAME OVER")
            palabra = "".join(palabra_secreta)
            print(f"La palabra era {palabra}")
            break

```

[Juego de Ahorcado](https://github.com/LuisfeOro/Mi-Portafolio-Python/blob/main/Proyectos/proyecto_semana5-ahorcado.py)

Muchas gracias
