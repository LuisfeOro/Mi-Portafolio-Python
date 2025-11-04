class Animal:
    vivo = True

    def hablar(self):
        print("Sonido por defecto")

class Gato(Animal):
    #Sobreescribir un metodo se refiere a
    #Voy a nomnbrar un metodo igual a de la clase padre, pero le sobrescibire su funcion

    def hablar(self):
        print("Miau!")

animal_1 = Animal()
gato_1 = Gato()
animal_1.hablar()
gato_1.hablar()