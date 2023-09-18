a=2
b=5
print(a)

def suma(a, b, c):
    c=10
    a=15
    print(a+b+c)
    return(c)

suma()
print(a)
print(suma())

a=int(input("ingrese el primer numero: "))
b=int(input("ingrese el segundo numero"))


def menu():
    opcion=int(input("ingrese 1 para sumar y 2 para restar"))
    if opcion==1:
        suma()
        print(suma())
def suma():
    
    return(a+b)

def resta():
    return(a-b)

print(suma())
print(resta())