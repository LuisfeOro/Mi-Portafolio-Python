def devolver_distintos(a, b , c):
    suma = a + b + c
    #Servira para ver si la suma es mayor o menor que 15
    lista = [a, b, c]
    #Para poder sacar el maximo y el minimo saviendo que hay funciones que lo haran

    if suma > 15:
        return max(lista)
    elif suma < 10:
        return min(lista)
    elif suma in range(10,15):
        return sorted(lista)[1]

#Se llama al funcion
print(devolver_distintos(8, 1, 4))