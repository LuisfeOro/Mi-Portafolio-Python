import tkinter as tk

import ventana
from PIL import Image, ImageTk

#Esto es para poder agregar una imagen a mi interfaz


#Crear ventana principal
ventana = tk.Tk()
ventana.title("Ventana Principal")

#Cargar la imagen
imagen = Image.open("fondo.png")
imagen = imagen.resize((800,600)) #Para poner dimensiones
imagen_fondo = ImageTk.PhotoImage(imagen)

#Crear un Canvas
canvas = tk.Canvas(ventana, width=800, height=600)
canvas.pack(fill="both", expand=True)

#Colocar imagen en el canvas
canvas.create_image(400,0, image=imagen_fondo, anchor="n") #Crea una imagen


#Colocar otros widgets en el canvas
label = tk.Label(ventana, text="Texto en la ventana", bg="white")
label_window = canvas.create_window(400,300,window=label)

#Ciclo raiz

ventana.mainloop()