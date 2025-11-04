class Alumno:
    # init inicializa los atributos de cada objeto
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

#innit es una funcion

class Maestro:
    def __init__(self, nombre, curso):
        self.nombre = nombre
        self.curso = curso

alumno_1 = Alumno("Ana", 19) #Crear objetos con nombre y edad
alumno_2 = Alumno("Luis", 22)
alumno_3 = Alumno("Tobias", 16)


maestro_1 = Maestro("Luis", "Python")

print(alumno_1.nombre, alumno_1.edad)
print(alumno_2.nombre, alumno_2.edad)
print(alumno_3.nombre, alumno_3.edad)