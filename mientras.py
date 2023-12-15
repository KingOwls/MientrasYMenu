import os
isActive = True
rta = ""
while (isActive):
    os.system("cls")
    rta = input("Desea continuar con la ejecucion S(si) o enter (no)\n").upper()
    while (rta not in "S"):
        print ("Ha ingresado una opcion invalida")
        x= input("Presione enter para continuar....")
        #os.system("pause")
        #os.system("cls")
        rta = input("Desea continuar con la ejecucion S(si) o enter (no)\n").upper()
    if (bool(rta) == False):
        isActive = bool(rta)