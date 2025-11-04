nombre = input("Ingresa tu nombre: ")
ingresos = float(input((f"Buenos días {nombre}, por favor ingrese sus ingresos de este mes: ")))
comisiones = float(round(ingresos * 0.13, 2))
total = round(ingresos + comisiones,2)

print(f"Excelente señor/a {nombre}, su venta total fue de Q.{ingresos} por lo que al sumar las comisiones de Q.{comisiones} se quedaría con un Ingreso total de Q.{total}")