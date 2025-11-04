estudiante = {"nombre":"Ana","edad":25, "carrera":"Ingenieria"}
estudiante["carrera"] = "Medicina"
print(f"Carrera del estudiante: {estudiante['carrera']}")
#Crude, Create, Modify, Delete
estudiante["carrera"] = input("Ingrese la carrera: ")
print(f"Carrera del estudiante: {estudiante['carrera']}")