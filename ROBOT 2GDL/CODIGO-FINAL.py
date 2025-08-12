import tkinter as tk
from tkinter import messagebox
import serial
import math

class InterfazControlServos:
    def __init__(self, master):
        self.master = master
        self.master.title("ROBOT FIESTA")
        
        self.label_titulo = tk.Label(master, text="ROBOT FIESTA", font=("Helvetica", 16))
        self.label_titulo.grid(row=0, column=0, columnspan=4, pady=10)
        
        self.boton_arriba = tk.Button(master, text="Arriba", command=self.mover_arriba)
        self.boton_abajo = tk.Button(master, text="Abajo", command=self.mover_abajo)
        self.boton_izquierda = tk.Button(master, text="Izquierda", command=self.mover_izquierda)
        self.boton_derecha = tk.Button(master, text="Derecha", command=self.mover_derecha)
        
        self.boton_arriba.grid(row=1, column=1, pady=10)
        self.boton_abajo.grid(row=3, column=1, pady=10)
        self.boton_izquierda.grid(row=2, column=0, pady=10)
        self.boton_derecha.grid(row=2, column=2, pady=10)
        
        self.label_entry1 = tk.Label(master, text="Angulo  1 'servo inferior':")
        self.label_entry1.grid(row=4, column=0, pady=5)
        self.entry_angulo1 = tk.Entry(master)
        self.entry_angulo1.grid(row=4, column=1, pady=5)
        
        self.label_entry2 = tk.Label(master, text="Ángulo 2 'servo superior':")
        self.label_entry2.grid(row=5, column=0, pady=5)
        self.entry_angulo2 = tk.Entry(master)
        self.entry_angulo2.grid(row=5, column=1, pady=5)
        
        self.boton_ajustar = tk.Button(master, text="Ajustar Ángulos", command=self.ajustar_angulos)
        self.boton_ajustar.grid(row=6, column=0, columnspan=2, pady=10)
        
        self.label_posicion = tk.Label(master, text="Posición: (x=0, y=0, z=0)")
        self.label_posicion.grid(row=7, column=0, columnspan=4, pady=10)
        
        self.serial_port = serial.Serial('COM3', 9600, timeout=1)
        
        # Bind de eventos de teclado
        master.bind("<Up>", lambda event: self.mover_arriba())
        master.bind("<Down>", lambda event: self.mover_abajo())
        master.bind("<Left>", lambda event: self.mover_izquierda())
        master.bind("<Right>", lambda event: self.mover_derecha())
    
    def mover_arriba(self):
        try:
            angulo2 = int(self.entry_angulo2.get() or 90) + 10
            if 0 <= angulo2 <= 180:
                self.enviar_comando('U')
                self.entry_angulo2.delete(0, tk.END)
                self.entry_angulo2.insert(0, str(angulo2))
                self.actualizar_posicion()
        except ValueError:
            pass
        
    def mover_abajo(self):
        try:
            angulo2 = int(self.entry_angulo2.get() or 90) - 10
            if 0 <= angulo2 <= 180:
                self.enviar_comando('D')
                self.entry_angulo2.delete(0, tk.END)
                self.entry_angulo2.insert(0, str(angulo2))
                self.actualizar_posicion()
        except ValueError:
            pass
        
    def mover_izquierda(self):
        try:
            angulo1 = int(self.entry_angulo1.get() or 90) + 10
            if 0 <= angulo1 <= 180:
                self.enviar_comando('L')
                self.entry_angulo1.delete(0, tk.END)
                self.entry_angulo1.insert(0, str(angulo1))
                self.actualizar_posicion()
        except ValueError:
            pass
        
    def mover_derecha(self):
        try:
            angulo1 = int(self.entry_angulo1.get() or 90) - 10
            if 0 <= angulo1 <= 180:
                self.enviar_comando('R')
                self.entry_angulo1.delete(0, tk.END)
                self.entry_angulo1.insert(0, str(angulo1))
                self.actualizar_posicion()
        except ValueError:
            pass
    
    def ajustar_angulos(self):
        try:
            nuevo_angulo1 = int(self.entry_angulo1.get())
            nuevo_angulo2 = int(self.entry_angulo2.get())
            
            if 0 <= nuevo_angulo1 <= 180 and 0 <= nuevo_angulo2 <= 180:
                comando = f'A {nuevo_angulo1} {nuevo_angulo2}'
                self.enviar_comando(comando)
                self.actualizar_posicion()
            else:
                messagebox.showerror("Error", "Los ángulos deben estar entre 0 y 180 grados")
        
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa valores enteros válidos para los ángulos")
    
    def enviar_comando(self, comando):
        self.serial_port.write(comando.encode())
        print(f"Enviado comando: {comando}")
    
    def actualizar_posicion(self):
        try:
            angulo1_rad = math.radians(float(self.entry_angulo1.get()))
            angulo2_rad = math.radians(float(self.entry_angulo2.get()))
            
            L1 = 7.0  # Cambiar los valores según tu configuración
            L2 = 10.0
            
            r = L2 * math.cos(angulo2_rad)
            x = r * math.cos(angulo1_rad)
            y = r * math.sin(angulo1_rad)
            z = L1 + L2 * math.sin(angulo2_rad)
            
            posicion = f"Posición: (x={x:.2f}, y={y:.2f}, z={z:.2f})"
            self.label_posicion.config(text=posicion)
        
        except ValueError:
            pass
    
    def __del__(self):
        self.serial_port.close()

def main():
    root = tk.Tk()
    interfaz = InterfazControlServos(root)
    root.mainloop()

if __name__ == "__main__":
    main()
