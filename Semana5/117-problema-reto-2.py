def letras_unicas(palabra):
    return sorted(set(palabra))

print(letras_unicas("entretenido"))


def letras_unicas2(palabra):

    lista = list(set(palabra))
    return sorted(lista)

print(letras_unicas2("entretenido"))