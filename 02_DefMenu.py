import math
menu = '''
*********************************************
**              1- Rectangulo              **
***             2- Triangulo              ***
****            3- Circulo               ****
*****           4- Salir                *****
*********************************************
'''
def Rectangulo():
    altura=float(input("Ingrese la altura del rectangulo: "))
    base=float
    area= altura*base 
    print("El area del rectangulo es: ", area)

def Triangulo():
    altura=float(input("Ingrese la altura del triangulo: "))
    base=float
    area= altura*base 
    print("El area del triangulo es: ", area)

def Circulo():
    radio=float(input("ingrese el radio del circulo"))
    area= math.pi * radio **2
    print("El area del triangulo es: ", area)

def salit():
    print("fin del programa")
    exit


while True:
    print(menu)
    opcion = int(input("ingrese una opcion: "))
    if opcion == 1:
        Rectangulo()
    elif opcion == 2:
        Triangulo()
    elif opcion == 3:
        Circulo()
    elif opcion == 4:
        break



print("fin del programa")
    







