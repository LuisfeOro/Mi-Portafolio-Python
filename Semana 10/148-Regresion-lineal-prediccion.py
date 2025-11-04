import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

data = pd.DataFrame({
    "tamano_m2": [50, 60, 80, 100, 120],
    "precio": [15000, 18000, 23000, 28000, 33000] #es un diccionario
})

x = data[["tamano_m2"]] #2 porque se es buscando la clave, valuar este valor y que se le asigne el del grupo

y = data[["precio"]]

modelo = LinearRegression()

modelo.fit(x, y) #Entrenando al modelo

tamano = int(input("Ingresa el tamano de la casa (m2): "))

nuevo = pd.DataFrame({"tamano_m2": [tamano]})
prediccion = modelo.predict(nuevo)
print(f"La prediccion para una casa de {tamano} m2 es {prediccion}")

plt.scatter(x, y, color = "blue", label = "Datos Reales")
plt.plot(x, modelo.predict(x), color = "red", label = "Linea de Regresion") #Esto es para cada uino de los puintos
plt.xlabel("Tamano (m2)")
plt.ylabel("Precio ($)")
plt.legend()

plt.show()