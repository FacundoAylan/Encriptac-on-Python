from tkinter import *
from tkinter import ttk
from objetivo_1 import mensaje_cifrado


def main ():
  ventana = Tk()

  # Configurar el título de la ventana
  ventana.title('Encriptación')
  # Configurar las dimensiones de la ventana
  ventana.geometry('800x600')
  #Configurar el color del background
  ventana.config(bg='black')

  # Crear y configurar el Frame
  frame = mensaje_cifrado(ventana)

  ventana.mainloop()

if __name__ == '__main__':
  main()