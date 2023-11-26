import tkinter as tk
from tkinter import ttk
from component.d_Cifrados.cifrado_cesar import cifrado_cesar
from component.d_Cifrados.cifrado_atbash import cifrado_atbash
from component.d_Cifrados.decifrado_cesar import decifrado_cesar
from component.d_Cifrados.decifrado_atbash import decifrado_atbash

def mostrar_cifrado(frame_menu, cifrado, ventana):
  #oculta el menu
  frame_menu.pack_forget()

  #Creacion del frame del menu
  opcion_cesar = cifrado(ventana,frame_menu)
  opcion_cesar.pack(fill="both", expand=True)# Mostrar el frame_menu

def menu(ventana):
  s = ttk.Style()
  # Puedes configurar el color de fondo como desees
  s.configure(
      'Custom.TFrame', 
      background='#2f343f',
      font=("Arial", 16, "bold"),
  )  
  frame_menu = ttk.Frame(ventana, style='Custom.TFrame')
  frame_menu.pack(fill="both", expand=True)
  label = ttk.Label(
    frame_menu, 
    text='Menu', 
    font=("Arial", 22, "bold"),
    background="#2f343f",
    foreground='#4a98ba'
  )
  label.pack(pady = 10)

  button = tk.Button(
    frame_menu, 
    text='Cifrar mensaje César', 
    command=lambda: mostrar_cifrado(frame_menu,cifrado_cesar, ventana)
  )
  button.config(
    width = 40,
    height = 1,
    bg = '#4a98ba',
    bd = 2,
    relief = 'flat',
    cursor = 'hand2',
  )
  button.pack(pady = 10)
  button = tk.Button(
    frame_menu, 
    text='Descifrar mensaje César', 
    command=lambda: mostrar_cifrado(frame_menu,decifrado_cesar, ventana)
  )
  button.config(
    width = 40,
    height = 1,
    bg = '#4a98ba',
    bd = 2,
    relief = 'flat',
    cursor = 'hand2',
  )
  button.pack(pady = 10)
  button = tk.Button(
    frame_menu, 
    text='Cifrar mensaje Atbash', 
    command=lambda: mostrar_cifrado(frame_menu,cifrado_atbash, ventana)
  )
  button.config(
    width = 40,
    height = 1,
    bg = '#4a98ba',
    bd = 2,
    relief = 'flat',
    cursor = 'hand2',
  )
  button.pack(pady = 10)
  button = tk.Button(
    frame_menu, 
    text='Descifrar mensaje Atbash', 
    command=lambda: mostrar_cifrado(frame_menu,decifrado_atbash, ventana)
  )
  button.config(
    width = 40,
    height = 1,
    bg = '#4a98ba',
    bd = 2,
    relief = 'flat',
    cursor = 'hand2',
  )
  button.pack(pady = 10)


  return frame_menu