# Proyecto Semana 3: Analizador de Texto
## Hola, me llamo Luis y les estare presentando mi tercer Proyecto del curso de Python de la Academa Fibonnacci

En el siguiente proyecto el objetivo principal es crear un programa que le solicite al usuario un texto cualquiera. 

El programa realizara las siguientes funciones:
1. Numero de veces que apareceran las 3 letras que el usuario elija de su texto copiado
2. La cantidad de palabras que hay a lo largo del texto
3. Indicar cual es la primera y ultima letra del texto copiado
4. Invertir el texto ingresado
5. Indicar si aparece la palabra "Python" en base a un booleano

- - - 
## Analizador de texto

```
texto = input("Ingresa texto: ").lower()
#Me gusta estudiar Python, en Academia Fibonacci

letra_1 = input("Ingresa la primera letra: ").lower()
letra_2 = input("Ingresa la segunda letra: ").lower()
letra_3 = input("Ingresa la tercera letra: ").lower()
#convertir las letras a 1 lista
lista = [letra_1, letra_2, letra_3]
#print(texto)
#print(lista)

#Cuantas veces aparecen las letras que se eligieron.
#Almacenar en una lista
print(f"La letra {letra_1}: aparece {texto.count(lista[0])} veces en el texto")
print(f"La letra {letra_2}: aparece {texto.count(lista[1])} veces en el texto")
print(f"La letra {letra_3}: aparece {texto.count(lista[2])} veces en el texto")

#Cuantas palabras hay en el texto
#Convertir un string en lista
texto_lista = texto.split(" ")
print(f"El texto tiene {len(texto_lista)} palabras")

#Primera y ultima letra del texto
print(f"La primera letra del texto es: {texto[0]}")
print(f"La ultima letra del texto es: {texto[-1]}")

#Texto invertido
print((" ".join(texto_lista[::-1])))

#Aparece Python?
resultado = {True: "Si",False:"No"}
print(f'La palabra "python" aparece en el texto? {resultado["python" in texto.lower()]}')

```

[Analizador Texto](https://github.com/LuisfeOro/Mi-Portafolio-Python/blob/main/Proyectos/proyecto_semana3-Analizador-texto.py)

Muchas gracias

