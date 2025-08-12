import tkinter as tk
from tkinter import messagebox

class Robot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

    def mover_arriba(self, angulo2):
        pass  # Aquí puedes agregar la lógica para mover el robot hacia arriba

    def mover_abajo(self, angulo2):
        pass  # Aquí puedes agregar la lógica para mover el robot hacia abajo

    def mover_izquierda(self, angulo1):
        pass  # Aquí puedes agregar la lógica para mover el robot hacia la izquierda

    def mover_derecha(self, angulo1):
        pass  # Aquí puedes agregar la lógica para mover el robot hacia la derecha

class Interfaz:
    def __init__(self, master, robot):
        self.master = master
        self.robot = robot

        self.entry_angulo1 = tk.Entry(master, bg="white", fg="black")
        self.entry_angulo1.grid(row=0, column=0)

        self.entry_angulo2 = tk.Entry(master, bg="white", fg="black")
        self.entry_angulo2.grid(row=1, column=0)

        self.boton_arriba = tk.Button(master, text="Mover arriba", bg="white", fg="black", command=self.mover_arriba)
        self.boton_abajo = tk.Button(master, text="Mover abajo", bg="white", fg="black", command=self.mover_abajo)
        self.boton_izquierda = tk.Button(master, text="Mover izquierda", bg="white", fg="black", command=self.mover_izquierda)
        self.boton_derecha = tk.Button(master, text="Mover derecha", bg="white", fg="black", command=self.mover_derecha)

        self.boton_arriba.grid(row=2, column=0)
        self.boton_abajo.grid(row=3, column=0)
        self.boton_izquierda.grid(row=4, column=0)
        self.boton_derecha.grid(row=5, column=0)

    def mover_arriba(self):
        try:
            angulo2 = int(self.entry_angulo2.get())
            self.robot.mover_arriba(angulo2)
        except ValueError:
            messagebox.showerror("Error", "El ángulo debe ser un número entero")

    def mover_abajo(self):
        try:
            angulo2 = int(self.entry_angulo2.get())
            self.robot.mover_abajo(angulo2)
        except ValueError:
            messagebox.showerror("Error", "El ángulo debe ser un número entero")

    def mover_izquierda(self):
        try:
            angulo1 = int(self.entry_angulo1.get())
            self.robot.mover_izquierda(angulo1)
        except ValueError:
            messagebox.showerror("Error", "El ángulo debe ser un número entero")

    def mover_derecha(self):
        try:
            angulo1 = int(self.entry_angulo1.get())
            self.robot.mover_derecha(angulo1)
        except ValueError:
            messagebox.showerror("Error", "El ángulo debe ser un número entero")

class Aplicacion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Robot fiesta")
        self.ventana.config(bg="black")
        self.ventana.resizable(0,0)

        self.robot = Robot()
        self.interfaz = Interfaz(self.ventana, self.robot)

        self.ventana.mainloop()

if __name__ == "__main__":
    app = Aplicacion()