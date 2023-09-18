#More Godoy  
#12/04/2023 
#Profe Lui

print("hola usuario, este programa sirve para ordenar nombres alfabeticamente")
#Explico el programa
listNombres=[]
#Creo la lista

#Pido la cantidad de nombres que quieran ingresar
while True:
    try:
        cantidad=(int(input("ingrese la cantidad de nombres que desea ingresar: ")))
        for i in range (cantidad):
            Nombres=(str(input(f"ingrese el nombre {i+1}: ")))
            #Ingresan los nombres
            listNombres.append(Nombres)
        listNombres.sort()
        #Guarda y ordena los nombres
        print("Estos son los nombres que ingreso")
        print(listNombres)
        print("fin del programa")
        #Los muestra en orden y da fin al programa
        break
    except ValueError:
        print("ese no es un tipo de dato valido, vuelva a ingresar porfavor")
        #En caso de ingresar otro tipo de dato sale error y pide porfavor volver a ingresar


