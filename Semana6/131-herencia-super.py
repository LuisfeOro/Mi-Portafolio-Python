class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

class Admin(Usuario):
    def __init__(self, nombre, nivel):
        super().__init__(nombre)
        self.nivel = nivel


root_1 = Admin("root 1", 10)
root_2 = Admin("root 2", 5)
root_3 = Admin("root 3", 3)
root_4 = Admin("root 4", 1)

print(root_1.nombre, root_1.nivel)
print(root_2.nombre, root_2.nivel)
print(root_3.nombre, root_3.nivel)
print(root_4.nombre, root_4.nivel)