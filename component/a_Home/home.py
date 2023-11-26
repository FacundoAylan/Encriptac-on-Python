import tkinter as tk
from component.b_Sesion.sesion import Sesion
from component.b_Sesion.create import Create
from component.c_Menu.menu import menu

def mostrar_menu(frame_home, ventana, component):

    frame_home.pack_forget()  # Ocultar el frame_home
    #Creacion del frame del menu
    frame_menu = component(ventana)
    frame_menu.pack(fill="both", expand=True)
    #oculta el menu

def home(ventana):

  frame_home = tk.Frame(ventana, bg="#2f343f")
  frame_home.pack( fill=tk.BOTH, expand=True)
  
  label = tk.Label(
      frame_home, 
      text='BIENVENIDO A LA APLICACIÓN DE MENSAJES SECRETOS DEL GRUPO PROGRAMANDO', 
      font=("Arial",14, "bold"),
      background="#2f343f",
      foreground='white',
      justify="left",
  )
  label.place(relx=0.01,rely=0.20, relwidth=0.98)

  button_1 = tk.Button(
    frame_home,
    text='Ingreso Usuario', 
    command=lambda: mostrar_menu(frame_home, ventana,Sesion)
  )
  button_1.config(
    width = 20,
    height = 2,
    bg = '#4a98ba',
    bd = 2,
    relief = 'flat',
    cursor = 'hand2'
  )
  button_1.place(relx=0.4, rely=0.3)

  button_2 = tk.Button(
      frame_home,
      text='Crear Usuario”', 
      width=40, 
      command=lambda: mostrar_menu(frame_home, ventana, Create)
  )
  button_2.config(
    width = 20,
    height = 2,
    bg = '#4a98ba',
    bd = 2,
    relief = 'flat',
    cursor = 'hand2'
  )
  button_2.place(relx=0.4, rely=0.41)
  # Se agregan los nombres de los integrantes
  label_title = tk.Label(
      frame_home, 
      text='Creado por:', 
      background='#007acc',
      foreground='white'
  )

  label_name = tk.Label(
      frame_home, 
      text='Damian Ezequiel Casal',
      background='#007acc',
      foreground='white'
  )

  label_name = tk.Label(
      frame_home, 
      text='Santiago Nicolas Bassedas',
      background='#007acc',
      foreground='white'
  )

  label_name = tk.Label(
      frame_home, 
      text='Facundo Nunes',
      background='#007acc',
      foreground='white'
  )

  label_name = tk.Label(
      frame_home, 
      text='Laiila Ayelen Leiva',
      background='#007acc',
      foreground='white'
  )

  label_name = tk.Label(
      frame_home, 
      text='Facundo Aylan',
      background='#007acc',
      foreground='white'
  )


  return frame_home
