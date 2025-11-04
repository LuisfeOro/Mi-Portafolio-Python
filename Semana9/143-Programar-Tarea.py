import time
from datetime import datetime

def tarea():
    print("👌 Tarea Ejecutada", datetime.now())

hora_objetivo = "20:16"

while True:
    hora_actual = datetime.today().strftime("%H:%M") #Para que me convierta la hora objetivo a un fotrmato que quiero
    if hora_actual == hora_objetivo:
        tarea()
        break

    time.sleep(30)