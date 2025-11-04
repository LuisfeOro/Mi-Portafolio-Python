nombre = input("Cual es tu nombre?")
ventas = float(input("A cuanto asciende el monto de tus ventas?"))
comision = ventas*0.13
total = comision + ventas
print(f"El total de comisiones de tus ventas es {round(comision,2)}\nEl total devengado es Q {round(total,2)}")
