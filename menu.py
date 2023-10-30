from tkinter import *
from tkinter import ttk
from cifrado_cesar import cifrado_cesar
from cifrado_atbash import cifrado_atbash
from decifrado_cesar import decifrado_cesar
from decifrado_atbash import decifrado_atbash

def mostrar_cifrado(frame_menu, cifrado, ventana):
  #oculta el menu
  frame_menu.pack_forget()

  #Creacion del frame del menu
  opcion_cesar = cifrado(ventana,frame_menu)
  opcion_cesar.pack(fill="both", expand=True)
  opcion_cesar.pack()  # Mostrar el frame_menu

def menu(ventana):
  s = ttk.Style()
  # Puedes configurar el color de fondo como desees
  s.configure(
      'Custom.TFrame', 
      background='#007acc',
      font=("Arial", 16, "bold"),
  )  
  frame_menu = ttk.Frame(ventana, style='Custom.TFrame')
  frame_menu.pack(fill="both", expand=True)
  label = ttk.Label(
    frame_menu, 
    text='Menu', 
    font=("Arial", 16, "bold"),
    background="#007acc",
    foreground='white'
  )
  label.pack(pady = 10)

  button = ttk.Button(
    frame_menu, 
    text='Cifrar mensaje César', 
    width=40,
    command=lambda: mostrar_cifrado(frame_menu,cifrado_cesar, ventana)
  )
  button.pack(pady = 10)
  button = ttk.Button(
    frame_menu, 
    text='Descifrar mensaje César', 
    width=40,
    command=lambda: mostrar_cifrado(frame_menu,decifrado_cesar, ventana)
  )
  button.pack(pady = 10)
  button = ttk.Button(
    frame_menu, 
    text='Cifrar mensaje Atbash', 
    width=40,
    command=lambda: mostrar_cifrado(frame_menu,cifrado_atbash, ventana)
  )
  button.pack(pady = 10)
  button = ttk.Button(
    frame_menu, 
    text='Descifrar mensaje Atbash', 
    width=40,
    command=lambda: mostrar_cifrado(frame_menu,decifrado_atbash, ventana)
  )
  button.pack(pady = 10)


  return frame_menu