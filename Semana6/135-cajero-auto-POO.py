class Persona:
    def __init__(self, nombre: str, apellido: str):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre: str, apellido: str, numero_cuenta: str, balance_inicial: float = 0.0):
        #COnstructor creado para cliente
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance_inicial = float(balance_inicial)

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}\nCuenta: {self.numero_cuenta}\nBalance: Q.{self.balance_inicial:.2f}"

    def depositar(self, monto: float):
        self.balance_inicial += monto


    def retirar(self, monto: float):
        monto = float(monto)

        if monto <= self.balance_inicial:

            self.balance_inicial -= monto
            return True

        return False

def crear_cliente():

    print(" *** Creando Cliente *** ")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    numero_cuenta = input("Numero cuenta: ")
    balance_inicial = input("Balance inicial: ")

    return Cliente(nombre, apellido, numero_cuenta, balance_inicial=0)

def inicio():
    cliente = crear_cliente()
    print("Cliente creado")
    print(cliente)

inicio()