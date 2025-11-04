# Programa Creador de Nombres
primer_nombre = input("Ingresa tu primer nombre: ")
apellido = input("Ingresa tu apellito: ")

# Crear el nombre completo
nombre_completo = primer_nombre + " " + apellido

# Mostrar diferentes variaciones del nombre
print("Tu nombre completo es: " + nombre_completo)
print("Si solo usas tus iniciales, tu nombre ser a: " + primer_nombre[0] + " "+ apellido[0)
print("Una version divertida de tu nombre podria ser: " + primer_nombre[::-1] + " "+ apellido[::-1])
