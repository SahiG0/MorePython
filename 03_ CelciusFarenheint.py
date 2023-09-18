

# Programa para hacer el paso de Farenheit a celcius y vice.


def fc(fahrenheit):
    return (fahrenheit - 32) * 5/9

# El def es una funcion 
# Pase de Farenheit a celcius 

def cf(celsius):
    return (celsius * 9/5) + 32

# Pase de celcius a Farenheit

def menu():
    Menu1 = '''
    ----------- Menu ----------------
    1. Convertir Celsius a Fahrenheit
    2. Convertir Fahrenheit a Celsius
    3. Salir
    '''
    return (print(Menu1))
    # El return sirve para llamar a el def 

def main():
    while True:
        menu()
        # Llamamos a el nombre del menu
        opcion = int(input("Selecciona una opción: "))
        
        if opcion == 1:
            celsius = float(input("Ingresa la temperatura en Celsius: "))
            fahrenheit = cf(celsius)
            print(f"{celsius} grados Celsius equivalen a {fahrenheit} grados Fahrenheit")
        elif opcion == 2:
            fahrenheit = float(input("Ingresa la temperatura en Fahrenheit: "))
            celsius = fc(fahrenheit)
            print(f"{fahrenheit} grados Fahrenheit equivalen a {celsius} grados Celsius")
        elif opcion == 3:
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")



main()
# Siempre llamar a los def fuera de si mismos para que funcionen