from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)
raiz = Tk()
raiz.geometry('300x200') # anchura x altura
# Asigna un color de fondo a la ventana. Si se omite
# esta línea el fondo será gris

raiz.configure(bg = 'beige')
# Asigna un título a la ventana

raiz.title('Algoritmo de las 8 reinas')

ttk.Button(raiz, text='Salir', command=quit).pack(side=BOTTOM)

raiz.mainloop()