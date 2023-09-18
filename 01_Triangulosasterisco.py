
#Hacer un programa donde el usuario ingrese un numero entero y se transforme en un triangulo

# con ese numero de lineas y lo muestre con un menu de asteriscos

# Las variables no pueden comenzar con mayusculas

print("Hola usuario este programa hace triangulos con numeros enteros")
cosito = "*"
lineas = int(input("Ingrese la cantidad de lineas que van a conformar a su triangulo: "))

for i in range(lineas):
    print(cosito)
    cosito = cosito * 2