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

    s = ttk.Style()
    # Puedes configurar el color de fondo como desees
    s.configure(
        'Custom.TFrame', 
        background='#007acc',
        font=("Arial", 16, "bold"),
    )  

    frame_home = ttk.Frame(ventana, style='Custom.TFrame')
    frame_home.pack( fill="both", expand=True)
  
    label = ttk.Label(
        frame_home, 
        text='Bienvenido a la aplicación de mensajes secretos del grupo Programando.', 
        font=("Arial", 16, "bold"),
        background="#007acc",
        foreground='white'
    )
    label.pack(pady = 20)
    button = ttk.Button(
        frame_home,
        text='Continuar', 
        width=40, 
        command=lambda: mostrar_menu(frame_home, ventana)
    )
    button.pack(pady = 10)

    # Se agregan los nombres de los integrantes
    label_title = ttk.Label(
        frame_home, 
        text='Creado por:', 
        background='#007acc',
        foreground='white'
    )
    label_title.pack(pady = 10)
    label_name = ttk.Label(
        frame_home, 
        text='Damian Ezequiel Casal',
        background='#007acc',
        foreground='white'
    )
    label_name.pack(pady = 5)
    label_name = ttk.Label(
        frame_home, 
        text='Santiago Nicolas Bassedas',
        background='#007acc',
        foreground='white'
    )
    label_name.pack(pady = 5)
    label_name = ttk.Label(
        frame_home, 
        text='Facundo Nunes',
        background='#007acc',
        foreground='white'
    )
    label_name.pack(pady = 5)
    label_name = ttk.Label(
        frame_home, 
        text='Laiila Ayelen Leiva',
        background='#007acc',
        foreground='white'
    )
    label_name.pack(pady = 5)
    label_name = ttk.Label(
        frame_home, 
        text='Facundo Aylan',
        background='#007acc',
        foreground='white'
    )
    label_name.pack(pady = 5)

    return frame_home
