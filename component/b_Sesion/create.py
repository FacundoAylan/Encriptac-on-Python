import tkinter as tk
from tkinter import ttk
from component.c_Menu.menu import menu
import csv

def guardar_en_csv(usuario,contraseña,pregunta,respuesta):
    usuario = usuario.get()
    contraseña = contraseña.get()
    pregunta = pregunta.get()
    respuesta = respuesta.get()
    with open('datos.csv', mode='a', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        escritor_csv.writerow([usuario, contraseña,pregunta,respuesta])

def regresar_menu(frame_usuario, frame_inicio, ventana):
  frame_usuario.pack_forget()
  # Mostrar el frame_menu con la configuración original
  frame_inicio(ventana)
def regresar_sesion(frame_usuario,frame_inicio,ventana, create):
  frame_usuario.pack_forget()
  # Mostrar el frame_menu con la configuración original
  frame_inicio(ventana, frame_inicio,create)

def Create(ventana, create, sesion):

  opciones = [
    'Apellido de su abuela materna',
    'Nombre de tu mascota',
    'Nombre de tu mejor amigo/amiga',
    'Cantante preferido',
    'Ciudad preferida'
  ]
  selected_option = tk.StringVar()
  frame_create = tk.Frame(ventana, bg="#2f343f")
  frame_create.pack( fill=tk.BOTH, expand=True)

  label = tk.Label(
    frame_create, 
    text='Crear usuario',
    font=("Arial", 22, "bold"),
    background="#2f343f",
    foreground='#4a98ba'
  )
  label.place(relx=0.01,rely=0.05, relwidth=0.98)

  label_name = tk.Label(
    frame_create, 
    text='Usuario',
    font=("Arial", 16, "bold"),
    background="#2f343f",
    foreground='white'
  )
  label_name.place(relx=-0.2,rely=0.16, relwidth=0.98)
  usuario = tk.Entry(frame_create, width=55)
  usuario.place(relx=0.24,rely=0.21)

  label_contraseña = tk.Label(
    frame_create, 
    text='Contraseña',
    font=("Arial", 16, "bold"),
    background="#2f343f",
    foreground='white'  
  )

  label_contraseña.place(relx=-0.18,rely=0.28, relwidth=0.98)
  contraseña = tk.Entry(frame_create, width=55)
  contraseña.place(relx=0.24,rely=0.33)
  label_select = tk.Label(
    frame_create, 
    text='Pregunta de seguridad',
    font=("Arial", 16, "bold"),
    background="#2f343f",
    foreground='white'  
  )
  label_select.place(relx=-0.11,rely=0.4, relwidth=0.98)
  pregunta = ttk.Combobox(ventana, textvariable=selected_option, values=opciones, width=54)
  pregunta.set("Seleccionar opción")
  pregunta.place(relx=0.24,rely=0.45)

  label_respuesta = tk.Label(
    frame_create, 
    text='respuesta',
    font=("Arial", 16, "bold"),
    background="#2f343f",
    foreground='white'  
  )

  label_respuesta.place(relx=-0.19,rely=0.51, relwidth=0.98)
  respuesta = tk.Entry(frame_create, width=55)
  respuesta.place(relx=0.24,rely=0.56)

  button_get = tk.Button(
    frame_create, 
    text='Crear',
    # command=lambda: regresar_menu(frame_create, menu, ventana) 
    command=lambda: guardar_en_csv(usuario,contraseña,pregunta,respuesta) 
  )
  button_get.config(
    width = 20,
    height = 1,
    bg = '#4a98ba',
    bd = 2,
    relief = 'flat',
    cursor = 'hand2'
  )
  button_get.place(relx=0.4,rely=0.62)
  
  button_prev = tk.Button(
    frame_create, 
    text='Iniciar sesion',
    # command=lambda: regresar_menu(frame_create, menu, ventana) 
    command=lambda: regresar_sesion(frame_create, sesion, ventana,create)
  ) 
  button_prev.config(
    width = 20,
    height = 1,
    bg = '#4a98ba',
    bd = 2,
    relief = 'flat',
    cursor = 'hand2'
  )
  button_prev.place(relx=0.4,rely=0.69)

  return frame_create