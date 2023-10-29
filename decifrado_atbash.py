from tkinter import *
from tkinter import ttk

def regresar_menu(frame_atbash, frame_menu, menu_config):
  frame_atbash.pack_forget()
  # Mostrar el frame_menu con la configuración original
  frame_menu.pack(**menu_config)

def cifrado(mensaje_a_cifrar, etiqueta_resultado):

    resultado=''
    for caracter in mensaje_a_cifrar, etiqueta_resultado:
        if 'a'<= caracter<= 'z':
            reemplazo=chr(ord('z')-(ord(caracter)-ord('a')))
        elif 'A' <= caracter <='Z':
            reemplazo=chr(ord('Z')-(ord(caracter)-ord('A')))
        elif '0' <= caracter <= '9':
            reemplazo=chr(ord('9')-(ord(caracter)-ord('0')))
        else:
            reemplazo=caracter

        resultado+=reemplazo

    etiqueta_resultado.config(text="Texto ingresado: " + resultado)

def decifrado_atbash(ventana, frame_menu):

  frame_atbash = ttk.Frame(ventana)
  frame_atbash.pack(fill="both", expand=True)
  # Guardar la configuración original del frame_cesar
  menu_config = frame_atbash.pack_info()
  
  label = ttk.Label( frame_atbash, text = 'Decifrado Atbash',font=("Arial", 16, "bold"))
  label.pack()

  #Los input encargados de obtener la información

  mensaje_label = ttk.Label( frame_atbash, text = 'Mensaje a decifrar',font=("Arial", 10, "bold"))
  mensaje_label.pack(pady = 10)

  mensaje_a_cifrar = ttk.Entry(frame_atbash, width = 80)
  mensaje_a_cifrar.pack()

  boton_de_enviar = ttk.Button(frame_atbash, text='Enviar', width = 40, command=lambda: cifrado(mensaje_a_cifrar, etiqueta_resultado))
  boton_de_enviar.pack( pady = 10)

  button = ttk.Button(frame_atbash, text='Regresar', width=40,command=lambda: regresar_menu(frame_atbash, frame_menu, menu_config))
  button.pack()


  etiqueta_resultado = ttk.Label(frame_atbash, text="")
  etiqueta_resultado.pack()

  return frame_atbash

