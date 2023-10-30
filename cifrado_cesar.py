from tkinter import *
from tkinter import ttk

def regresar_menu(frame_cesar, frame_menu, menu_config):
  frame_cesar.pack_forget()
  # Mostrar el frame_menu con la configuración original
  frame_menu.pack(**menu_config)

def cifrado(mensaje_a_cifrar, clave_de_cifrado, etiqueta_resultado):

  texto = mensaje_a_cifrar.get()  #Obtener el texto del Entry
  desplazamiento = int(clave_de_cifrado.get())

  resultado = ""
  
  for caracter in texto:
      if caracter.isalpha():  # Verificar si el caracter es una letra
          mayuscula = caracter.isupper()  # Verificar si es mayúscula
          caracter = caracter.lower()  # Convertir a minúscula para el cifrado
          
          codigo = ord(caracter) - ord('a')  # Convertir a un valor entre 0 y 25
          codigo = (codigo + desplazamiento) % 26  # Aplicar el desplazamiento
          caracter_cifrado = chr(codigo + ord('a'))  # Convertir de nuevo a letra
          
          if mayuscula:  # Restaurar mayúscula si era originalmente mayúscula
              caracter_cifrado = caracter_cifrado.upper()
          
          resultado += caracter_cifrado
      elif caracter.isnumeric():
        # Si es un número
        num_original = int(caracter)
        num_cifrado = (num_original + desplazamiento) % 10
        resultado += str(num_cifrado) 
      else:
          resultado += caracter  # Mantener caracteres no alfabéticos sin cambios

  etiqueta_resultado.config(text="Texto ingresado: " + resultado)

    
def cifrado_cesar(ventana, frame_menu):

  frame_cesar = ttk.Frame(ventana)
  frame_cesar.pack(fill="both", expand=True)
  # Guardar la configuración original del frame_cesar
  menu_config = frame_cesar.pack_info()
  
  label = ttk.Label( 
    frame_cesar, text = 'Encriptación de mensajes',
    font=("Arial", 16, "bold")
  )
  label.pack()

  #Los input encargados de obtener la información

  mensaje_label = ttk.Label( 
    frame_cesar, 
    text = 'Mensaje a cifrar',
    font=("Arial", 10, "bold")
  )
  mensaje_label.pack(pady = 10)

  mensaje_a_cifrar = ttk.Entry(frame_cesar, width = 80)
  mensaje_a_cifrar.pack()

  clave_label = ttk.Label( 
    frame_cesar, 
    text = 'Clave de cifrado',
    font=("Arial", 10, "bold")
  )
  clave_label.pack(pady = 10)

  clave_de_cifrado = ttk.Entry(frame_cesar, width = 80)
  clave_de_cifrado.pack()

  boton_de_enviar = ttk.Button(
    frame_cesar, 
    text='Enviar', 
    width = 40, 
    command=lambda: cifrado(mensaje_a_cifrar, clave_de_cifrado, etiqueta_resultado)
  )
  boton_de_enviar.pack( pady = 10)

  button = ttk.Button(
    frame_cesar, 
    text='Regresar', 
    width=40,command=lambda: regresar_menu(frame_cesar, frame_menu, menu_config)
  )
  button.pack()


  etiqueta_resultado = ttk.Label(frame_cesar, text="")
  etiqueta_resultado.pack()

  return frame_cesar

