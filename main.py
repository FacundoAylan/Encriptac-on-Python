import os
import tkinter as tk
from tkinter import ttk
from component.a_Home.home import home

ruta_icono = os.path.join(os.path.dirname(__file__), "logo.ico")

def main ():
  ventana = tk.Tk()

  # Configurar el título de la ventana
  ventana.title('TP Grupal Parte 1 - Grupo: Programando')
  # Configurar las dimensiones de la ventana
  ventana.geometry('800x600')
  #Configurar el color del background
  ventana.configure(bg="#007acc")
  #Toma la ruta de la carpeta en la que me encuentro ubicado
  ruta_icono = os.path.join(os.path.dirname(__file__), "logo.png")
  # Cargar el archivo de imagen desde el disco.
  icono = tk.PhotoImage(file=ruta_icono)
  # ventana.iconbitmap(ruta_icono)
  # Establecerlo como ícono de la ventana.
  ventana.iconphoto(False, icono)

  # Crear y configurar el Frame
  home(ventana)

  ventana.mainloop()

if __name__ == '__main__':
  main()