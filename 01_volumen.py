print("Este programa sirve para calcular el volumen de una caja")

ancho = int(input(" Ingrese el ancho: "))
largo = int(input(" Ingrese el largo: "))
alto = 1

while True:
    iteraciones = int(input("ingrese la cantidad de iteraciones: "))
    for i in range(iteraciones):
        alto = alto + 1
        volumen = (ancho - 2 * alto) * (largo - 2 * alto) * alto
        print("El volumen de la caja es: ", volumen)
        print("fin")