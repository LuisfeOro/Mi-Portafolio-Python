#Queremos llegar hasta n
n = int(input("Ingrese hasta donde desee sumar: "))
suma = 0
for i in range(1, n+1):
    suma += i
    print(suma)
    input("Press enter to continue...")