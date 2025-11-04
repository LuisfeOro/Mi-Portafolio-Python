import numpy as np
from sklearn.linear_model import LogisticRegression

horas_estudio = np.array([[2],[4],[6],[8],[10]])
resultado = np.array([0,0,1,1,1])

modelo = LogisticRegression()

modelo.fit(horas_estudio, resultado)

pred = modelo.predict([[5]])
print("Aprobo el estudiante con 7 horas de estudio?", "Si" if pred[0] else "No")
