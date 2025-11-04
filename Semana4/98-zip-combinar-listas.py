productos = ["Teclado","Mouse","Pantalla"]
#Metodo Append
productos.append("Case")
precios = [150,99,1200,800]
for producto,precio in zip(productos,precios):
    print(f"{producto}: Q.{precio}")