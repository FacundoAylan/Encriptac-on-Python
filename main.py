import tkinter as tk
from tkinter import ttk
from home import home

def main ():
  ventana = tk.Tk()

  # Configurar el título de la ventana
  ventana.title('TP Grupal Parte 1 - Grupo: Programando')
  # Configurar las dimensiones de la ventana
  ventana.geometry('800x600')
  #Configurar el color del background
  ventana.config(bg='black')
  #agrego el logo de la aplicacion
  # ventana.iconbitmap("logo.ico")

  # Crear y configurar el Frame
  frame = home(ventana)

  ventana.mainloop()

if __name__ == '__main__':
  main()