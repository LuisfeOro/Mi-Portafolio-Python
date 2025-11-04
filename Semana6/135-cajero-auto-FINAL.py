class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):

    def __init__(self, nombre, apellido, numero_cuenta, balance=0):
        #herencia coni super
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Cliente: {self.nombre} | Apellido: {self.apellido}\nNumero de Cuenta: {self.numero_cuenta}\nBalance: {self.balance}\n Balance de Cuenta: {self.balance}"
    def depositar(self, monto_deposito):
        self.balance += monto_deposito
        print("Deposito Aceptado")

    def retirar(self, monto_retiro):
        if self.balance >= monto_retiro:
            self.balance -= monto_retiro
            print("Retiro Aceptado")
        else:
            print("No tienes disponibilidad")


def crear_cliente():
    nombre_cl = input("Ingrese su nombre: ")
    apellido_cl = input("Ingrese su apellido: ")
    numero_cuenta = input("Ingrese el numero de cuenta: ")
    cliente = Cliente(nombre_cl, apellido_cl, numero_cuenta) #Creacion del objeto o instancia
    return cliente

def inicio():
    mi_cliente = crear_cliente()
    print(mi_cliente)
    opcion = ''
    while opcion != 'S':
        print("Elige depositar(D), Retirar(R), o Salir(S)")
        opcion = input().upper()
        if opcion == 'D':
            monto_dep = int(input("Ingrese el monto a depositar: "))
            mi_cliente.depositar(monto_dep)
        elif opcion == 'R':
            monto_ret = int(input("Ingrese el monto a retirar: "))
            mi_cliente.retirar(monto_ret)

        print(mi_cliente)

    print("Gracias por utilizar el banco PYTHON")

inicio()