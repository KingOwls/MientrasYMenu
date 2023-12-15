import os
alumnos = []
isActive = True
menu = "1.Registrar alimno\n2.Registrar Notas\n3.Salir\n"
subMenuNotas = ["1. Parciales", "2.Quices", "3. Trabajos", "4. Regresar al menu principal"]
opMenu=0
while isActive:
    os.system("cls")
    try:
        opMenu= int(input(menu))
    except ValueError:
        print("Error al dato de ingreso")
        os.system("pause")
    else:
        if(opMenu== 1 ):
            rta = "S"
            while(rta in ["S", "s"]):
                codigo = input("ingrese el Codigo del Estudiante: ")
                nombre = input("ingrese el Nombre del Estudiante: ")
                edad = int(input("ingrese la edad del Estudiante: "))
                alumno = [codigo, nombre, edad, [], [], []]
                alumnos.append(alumno)
                print(alumnos)
                os.system("pause")
                rta = input("Desea registrar otro alumno S(si) o N (no)").upper()



        elif(opMenu== 2 ):
            opNotas = 0
            isActiveGrades = True
            while isActiveGrades:
                os.system("cls")
                for i, item in enumerate(subMenuNotas):
                    print(f"{i+1}. {item}")
                try:
                    opNotas = int(input(":)  "))                
                except ValueError:
                    print("Error al dato de ingreso")
                    os.system("pause")
                else:
                    if(opNotas==1):
                        print("Parciales")
                    elif(opNotas==2):
                        print("Quices")
                    elif(opNotas==3):
                        print("Trabajos")
                    elif(opNotas==4):
                        isActiveGrades = False
                    else:
                        print("opcion invadila")

        elif(opMenu==3):
            os.system("cls")
            print("gracias por usar nuestro sistema")
            isActive = False
        else:
            os.system("cls")
            print("opcion invadila")
    os.system("pause")