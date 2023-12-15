import os
isActive = True
rta = ""
menu = "1. Sumar\n 2. resta \n 3. multiplication \n 0. salida\n"
while isActive:
    try:
        os.system("cls")
        rta = int(input(menu))
    except ValueError:
        print("Error en el dato")
    else:
        if rta == 1:
            print("Sumando")
        elif rta == 2:
            print("Restando")
        elif rta == 3:
            print("Multiplicando")
        elif(rta == 0):
            print("Ok adios")
            isActive = False
        else:
            print("Opcion invalida...")
            os.system("pause")
        os.system("pause")
    