
#Esta carpeta esta destinada a aprender a hacer una Lista, guaradar variables, hacer un while, for y aprender a tabular el programa

print("Hola, ingrese 10 numeros porfavor")
#print para poder pedir 10 numeros
listNumeros = []
while True:
    try:

        for i in range (10):#recordar de cerrar el for con :
            numeros=(int(input(f"ingrese el numero {i+1}: ")))
            listNumeros.append(numeros)
#Utilizamos .appen para guardar los Numeros
        listNumeros.reverse()
        print("Estos son los numeros que nos diste.Gracias por tu ayuda terricola ahora que tenemos mas informacion de tu planeta podremos aprender mas, muajajaj >:D")
        print(listNumeros)
        #Si queremos poner un mensaje tenemos que poner otro print y no escribir en el de listnumeros
        #El print y el sort de la lista tienen q ir afuera del for porque si no nos muestra todo el tiempo la lista
        break
    except ValueError:
        print("Ese no es un numero entero, ingresa uno nuevamente y soy re buena en matematicas ")
#El while sirve por si ponemos variables no compatibles con nuestro programa las ignore



