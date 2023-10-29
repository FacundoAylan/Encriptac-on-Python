from tkinter import *
from tkinter import ttk
from menu import menu

def mostrar_menu(frame_home, ventana):

    frame_home.pack_forget()  # Ocultar el frame_home
    #Creacion del frame del menu
    frame_menu = menu(ventana)
    frame_menu.pack(fill="both", expand=True)
    #oculta el menu
    frame_menu.pack()  # Mostrar el frame_menu


def home(ventana):
    frame_home = ttk.Frame(ventana)
    frame_home.pack(fill="both", expand=True)
  
    label = ttk.Label(frame_home, text='Bienvenido a la aplicación de mensajes secretos del grupo Programando.', font=("Arial", 16, "bold"))
    label.pack()
    button = ttk.Button(frame_home, text='Continuar', width=40, command=lambda: mostrar_menu(frame_home, ventana))
    button.pack()

    # Se agregan los nombres de los integrantes
    label_title = ttk.Label(frame_home, text='Creado por:')
    label_title.pack()
    label_name = ttk.Label(frame_home, text='Damian Ezequiel Casal')
    label_name.pack()
    label_name = ttk.Label(frame_home, text='Santiago Nicolas Bassedas')
    label_name.pack()
    label_name = ttk.Label(frame_home, text='Facundo Nunes')
    label_name.pack()
    label_name = ttk.Label(frame_home, text='Laiila Ayelen Leiva')
    label_name.pack()
    label_name = ttk.Label(frame_home, text='Facundo Aylan')
    label_name.pack()

    return frame_home
