import random
import string
#variables

def menu1(): 
    print("bienvenidos al menu extraño")
    print("1_ contraseña con numeros y letras")
    print("2_ contrasena con numeros letras y caracteres especiales")
    print("3_ contraseña con")

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena
longitud_contrasena = int(input("Ingrese la longitud deseada para la contraseña: "))
contrasena_segura = generar_contrasena(longitud_contrasena)
print("La contraseña segura generada es:", contrasena_segura)

