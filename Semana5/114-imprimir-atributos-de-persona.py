def mostrar_atributos(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")
        #.items porque llama a todos los articulos de un diccionario

mostrar_atributos(nombre= "Ana", edad=25, ciudad="Antigua Guatemala", carrera="Ingenieria")