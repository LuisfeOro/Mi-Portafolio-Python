class Padre():
    def trabajo(self):
        print("Trabajo en la construccion")


class Madre():
    def trabajo(self):
        print("Trabajo en el Hospital")


class Hija(Madre, Padre):
    pass

amanda = Hija()
amanda.trabajo()