#Solicitar al usuario ingresar un texto cualquiera

texto = input("Por favor ingrese una palabra, oracion o texto: ")
texto_lowercase = texto.lower()

#Solicitar al usuario ingreasr 3 letras a su eleccion
print("A continuacion se te pediran 3 letras: ")
letra1 = input("Ingresa primera letra: ")
letra2 = input("Ingresa segunda letra: ")
letra3 = input("Ingresa tercera letra: ")
lista1 = [letra1, letra2, letra3]

#Analisis 1: Cuantas veces aparece cada una de las letras que eligio?
print(f"La letra {letra1} aparece {texto_lowercase.count(letra1)} veces")
print(f"La letra {letra2} aparece {texto_lowercase.count(letra2)} veces")
print(f"La letra {letra3} aparece {texto_lowercase.count(letra3)} veces")

#Analisis 2: Cuantas palabras hay a lo largo de todo el texto?
cantidad = texto_lowercase.split(" ")
print(cantidad)
print(f"El texto ingresado tiene un total de {len(cantidad)} palabras")

#Analisis 3: Cual es la primera letra del texto y la ultima? Index
print(f"La primera letra del texto es {texto_lowercase[0]} y la ultima letra del texto es {texto_lowercase[- 1]}")


#Analisis 4: Invertir el texto, Usar Join, PENDIENTE
print(cantidad[::-1].join(", "))

#Analisis 5: La palabra Python se encuentra dentro del texto?
tiene_python = "python" in texto_lowercase
print(f"El texto ingresado incluye la palabra python? {tiene_python}")