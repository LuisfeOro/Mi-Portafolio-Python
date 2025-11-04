def contar_letras(palabra):
    #Voy a recibir un string
    contador = 0
    for letra in palabra:
        contador += 1

    return contador

print(contar_letras("Python"))