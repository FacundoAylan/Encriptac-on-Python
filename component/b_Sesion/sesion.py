import tkinter as tk
from component.c_Menu.menu import menu

def regresar_menu(frame_usuario, frame_inicio, ventana):
  frame_usuario.pack_forget()
  # Mostrar el frame_menu con la configuración original
  frame_inicio(ventana)

def Sesion(ventana):

  frame_sesion = tk.Frame(ventana, bg="#2f343f")
  frame_sesion.pack( fill=tk.BOTH, expand=True)

  label = tk.Label(
    frame_sesion, 
    text='Inicio de sesion',
    font=("Arial", 22, "bold"),
    background="#2f343f",
    foreground='#4a98ba'
  )
  label.place(relx=0.01,rely=0.05, relwidth=0.98)

  label_name = tk.Label(
    frame_sesion, 
    text='Usuario',
    font=("Arial", 16, "bold"),
    background="#2f343f",
    foreground='white'
  )
  label_name.place(relx=-0.2,rely=0.16, relwidth=0.98)
  usuario = tk.Entry(frame_sesion, width=55)
  usuario.place(relx=0.24,rely=0.21)

  label_password = tk.Label(
    frame_sesion, 
    text='Contraseña',
    font=("Arial", 16, "bold"),
    background="#2f343f",
    foreground='white'  
  )

  label_password.place(relx=-0.18,rely=0.28, relwidth=0.98)
  password = tk.Entry(frame_sesion, width=55)
  password.place(relx=0.24,rely=0.33)

  button_get = tk.Button(
    frame_sesion, 
    text='Ingresar',
    command=lambda: regresar_menu(frame_sesion, menu, ventana)  
  )
  button_get.config(
    width = 20,
    height = 1,
    bg = '#4a98ba',
    bd = 2,
    relief = 'flat',
    cursor = 'hand2'
  )
  button_get.place(relx=0.4,rely=0.4)

  return frame_sesion