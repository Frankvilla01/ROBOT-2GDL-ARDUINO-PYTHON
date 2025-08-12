import tkinter as tk
from tkinter import messagebox

class Interfaz:
    def __init__(self, master):
        self.master = master

        self.label_titulo = tk.Label(master, text="==ROBOT FIESTA==", bg="black", fg="white")
        self.label_titulo.grid(row=0, column=4, columnspan=2)

        self.label_cruceta = tk.Label(master, text="Direccion", bg="black", fg="white")
        self.label_cruceta.grid(row=2, column=2, columnspan=1)

        self.label_direccion = tk.Label(master, text="Ingresar angulos", bg="black", fg="white")
        self.label_direccion.grid(row=2, column=5, columnspan=1)

        self.boton_arriba = tk.Button(master, text="Mover arriba", bg="white", fg="black")
        self.boton_abajo = tk.Button(master, text="Mover abajo", bg="white", fg="black")
        self.boton_izquierda = tk.Button(master, text="Mover izquierda", bg="white", fg="black")
        self.boton_derecha = tk.Button(master, text="Mover derecha", bg="white", fg="black")

        self.entry_angulo1 = tk.Entry(master, bg="white", fg="black")
        self.entry_angulo2 = tk.Entry(master, bg="white", fg="black")

        self.boton_arriba.grid(row=3, column=2)
        self.boton_abajo.grid(row=4, column=2)
        self.boton_izquierda.grid(row=4, column=1)
        self.boton_derecha.grid(row=4, column=3)

        self.entry_angulo1.grid(row=3, column=6)
        self.entry_angulo2.grid(row=4, column=6)

        self.label_angulo1 = tk.Label(master, text="Angulo 1", bg="black", fg="white")
        self.label_angulo1.grid(row=3, column=5, columnspan=1)
        self.label_angulo2 = tk.Label(master, text="Angulo 2", bg="black", fg="white")
        self.label_angulo2.grid(row=4, column=5, columnspan=1)

        self.label_posicion = tk.Label(master, text="==Posición==", bg="black", fg="white", font=("bold", 12))
        self.label_posicion.grid(row=5, column=4, columnspan=2)

        self.label_valor_posicion = tk.Label(master, text="", bg="black", fg="white", font=("bold", 12))
        self.label_valor_posicion.grid(row=6, column=4, columnspan=2)

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Robot fiesta")
        self.ventana.config(bg="black")
        self.ventana.resizable(0,0)

        self.interfaz = Interfaz(self.ventana)

        self.ventana.mainloop()

if __name__ == "__main__":
    app = Aplicacion()