def operaciones(a,b):
    return a+b,a-b,a*b,round(a/b,0)

#Desempaquetar
suma, resta, multiplicacion, div = operaciones(6,3)

print(suma, resta, multiplicacion,div)

print(suma)
print(resta)
print(multiplicacion)
print(div)