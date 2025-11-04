#Union, Interseccion, Diferencia, Diferencia simetrica

conjunto_1 = {1,2,3,6,7,8,9}
conjunto_2 = {2,4,6,8,10,12,14}
#Los unes
print(f"Union de conjuntos {conjunto_1.union(conjunto_2)}")
#Agrega solo los repetidos
print(f"Interseccion de conjuntos {conjunto_1.intersection(conjunto_2)}")
#A los elementos del elemento 1 le quita los del 2 y viceversa
print(f"Diferencia de conjuntos {conjunto_1.difference(conjunto_2)}")

#Va tomar los repetidos y los elemina.
print(f"Diferencia simetrica de conjuntos {conjunto_1.symmetric_difference(conjunto_2)}")