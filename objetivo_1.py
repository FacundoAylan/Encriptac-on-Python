from tkinter import *
from tkinter import ttk

def cifrado_cesar(mensaje_a_cifrar, clave_de_cifrado, etiqueta_resultado):
    texto = mensaje_a_cifrar.get()  # Obtener el texto del Entry
    desplazamiento = int(clave_de_cifrado.get())

    resultado = ""
    
    for caracter in texto:
        if caracter.isalpha():  # Verificar si el caracter es una letra
            mayuscula = caracter.isupper()  # Verificar si es mayúscula
            caracter = caracter.lower()  # Convertir a minúscula para el cifrado
            
            codigo = ord(caracter) - ord('a')  # Convertir a un valor entre 0 y 25
            codigo = (codigo + desplazamiento) % 26  # Aplicar el desplazamiento
            print(codigo)
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


def mensaje_cifrado(ventana):

  frame = ttk.Frame(ventana)
  frame.pack(fill="both", expand=True)
  
  label = ttk.Label( frame, text = 'Encriptación de mensajes',font=("Arial", 16, "bold"))
  label.pack()

  #Los input encargados de obtener la información

  mensaje_label = ttk.Label( frame, text = 'Mensaje a cifrar',font=("Arial", 10, "bold"))
  mensaje_label.pack(pady = 10)

  mensaje_a_cifrar = ttk.Entry(frame, width = 80)
  mensaje_a_cifrar.pack()

  clave_label = ttk.Label( frame, text = 'Clave de cifrado',font=("Arial", 10, "bold"))
  clave_label.pack(pady = 10)

  clave_de_cifrado = ttk.Entry(frame, width = 80)
  clave_de_cifrado.pack()

  boton_de_enviar = ttk.Button(frame, text='Enviar', width = 40, command=lambda: cifrado_cesar(mensaje_a_cifrar, clave_de_cifrado, etiqueta_resultado))
  boton_de_enviar.pack( pady = 10)


  etiqueta_resultado = ttk.Label(frame, text="")
  etiqueta_resultado.pack()

  return frame