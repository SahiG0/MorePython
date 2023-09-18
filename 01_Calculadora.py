#Hacer uma calculadora con un menu para elegir
#Def para definir mis operaciones


def Suma(a, b):
    return(a + b)

def Resta(a, b):
    return(a - b)
    
def Multiplicacion(a, b):
    return(a * b)

def Division(a, b):
    while True: #While por sin alguien loko kiere venir a dividil pol cero tu sabe
        try:
            return(a / b)
        except  ZeroDivisionError:
            print("¡Error!, no se puede dividir un numero en 0, porfavor ingresa otro valor.")

while True: #Menu 
    print("****** Menu ******")
    print("1- Suma")
    print("2- Resta")
    print("3- Multiplicacion")
    print("4- Division")

    opcion = int(input("Polfabol elija una opcion del menu: "))
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))

    if opcion == 1:
        print("La suma es: ", Suma(num1, num2))
    elif opcion == 2:
        print("La resta es: ", Resta(num1, num2))
    elif opcion == 3:
        print("La multiplicacion es: ", Multiplicacion(num1, num2))
    elif opcion == 4:
        print("La division es: ", Division(num1, num2))
    else:
        print("Opcion invalida mi loko")
        



 
    

