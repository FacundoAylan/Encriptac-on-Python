from tkinter import *
from tkinter import ttk

def regresar_menu(frame_atbash, frame_menu, menu_config):
  frame_atbash.pack_forget()
  # Mostrar el frame_menu con la configuración original
  frame_menu.pack(**menu_config)

def cifrado(mensaje_a_cifrar, etiqueta_resultado):

  texto = mensaje_a_cifrar.get()  # Obtener el texto del widget Entry
  texto_cifrado = ""

  for caracter in texto:
      if 'a' <= caracter <= 'z':
          caracter_cifrado = chr(ord('z') - (ord(caracter) - ord('a')))
      elif 'A' <= caracter <= 'Z':
          caracter_cifrado = chr(ord('Z') - (ord(caracter) - ord('A')))
      elif '0' <= caracter <= '9':
          caracter_cifrado=chr(ord('9')-(ord(caracter)-ord('0')))
      else:
          caracter_cifrado = caracter 

      texto_cifrado += caracter_cifrado
  etiqueta_resultado.config(text="Texto ingresado: " + texto_cifrado)


def cifrado_atbash(ventana, frame_menu):

  frame_atbash = ttk.Frame(ventana)
  frame_atbash.pack(fill="both", expand=True)
  # Guardar la configuración original del frame_cesar
  menu_config = frame_atbash.pack_info()
  
  label = ttk.Label( frame_atbash, text = 'Cifrado Atbash',font=("Arial", 16, "bold"))
  label.pack()

  #Los input encargados de obtener la información

  mensaje_label = ttk.Label( 
    frame_atbash, 
    text = 'Mensaje a cifrar',
    font=("Arial", 10, "bold")
  )
  mensaje_label.pack(pady = 10)

  mensaje_a_cifrar = ttk.Entry(frame_atbash, width = 80)
  mensaje_a_cifrar.pack()

  boton_de_enviar = ttk.Button(
    frame_atbash, 
    text='Enviar', 
    width = 40, 
    command=lambda: cifrado(mensaje_a_cifrar, etiqueta_resultado)
  )
  boton_de_enviar.pack( pady = 10)

  button = ttk.Button(
    frame_atbash, 
    text='Regresar', 
    width=40,
    command=lambda: regresar_menu(frame_atbash, frame_menu, menu_config)
  )
  button.pack()


  etiqueta_resultado = ttk.Label(frame_atbash, text="")
  etiqueta_resultado.pack()

  return frame_atbash

