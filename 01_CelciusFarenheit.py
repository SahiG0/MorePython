#Este programa realiza la conversion de celcius a farenheit o viceversa    
def PCF(celcius):
    return (celcius * 9 / 5) + 32

def PFC(farenheit):
    return (farenheit - 32) * 5 / 9


while True:
            
            def Menu(string):
                '''
                -----------------Mᴇɴᴜ-------------------
                |  1. Pᴀsᴀᴊᴇ ᴅᴇ ᴄᴇʟᴄɪᴜs ᴀ ғᴀʀᴇɴʜᴇɪᴛ    |
                |  2. Pᴀsᴀᴊᴇ ᴅᴇ ғᴀʀᴇɴʜᴇɪᴛ ᴀ ᴄᴇʟᴄɪᴜs    |
                |  3. Sᴀʟɪʀ                            |
                ----------------------------------------
                '''
            opcion = int(input("Ingrese el pasaje a relizar: "))
            if opcion == 1:
                celcius = float(input("Ingrese la temperatura en grados celcius: "))
                farenheit = PCF(celcius)
                print("El resultado del pasaje de t° de celcius a Farenheit es: ", celcius)
            elif opcion == 2:
                farenheit = float(input("Ingrese la tempereratura en grados farenheit: "))
                celcius = PFC(farenheit)
                print("El resultado del pasaje de t° de farenehit a celcius es: ", farenheit)
            elif opcion == 3:
                print("Bai loko")
                break

    

