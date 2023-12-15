#Presentacion de las listas que se pueden crear en python
numeros =[]
#Digitos
primos = [2, 3, 5, 7, 11, 13]
#Strings
diasLaborales = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
#Hibridas
fecha = [ "lunes", 27, "octubre", 1997]
#Conjuntos
peliculas = [["sendero de gloria", 1957], ["hannah y sus hermanas", 1986]]
#Conjunto de listas
directores = [["Stanley Kubrick", ["sendero de gloria", 1957]], ["woody Allen", ["hannah y sus hermanas", 1986]]]
#Ejemplo
materias =["Calculo"]
print (materias)
print(materias[0])
#Peticion de llenado
nombre = input("ingrese el Nombre:  ")
edad = int(input("ingrese la edad:  "))
persona = [nombre, edad]
print (persona)
#Arreglo de llenado
agenda =[]
for i in range(1,3):
    nombreF=input("ingrese el Nombre:  ")
    edadF = int(input("ingrese la edad:  "))
    personaF = [nombreF, edadF]
    agenda.append(personaF)
print(agenda)


#Metodo de agregado
num_list = [1,2,3,4,5,7]
print(f"Numeros en la Lista {num_list}")
num = int(input("Ingrese un numero a agregar a la lista: \n"))
index = int(input(f"Por favor ingrese un nuermo entre 0 a {len(num_list)-1}\n  Para agregarlo a la lista: \n"))
num_list.insert(index, num)
print(f"Numeros actualizados list {num_list}")


#Metodo de agregado hibrido
list_num =[]
list_num.extend([1,2])
print(list_num)
list_num.extend([3,4])
print(list_num)
list_num.extend(["ABC"])
print(list_num)

#Conjuntos
pares =[2,4,6]
impares =[1,3,5]
nums = pares + impares
print(nums)

#Seleccion especifica
pares =[2,4,6]
impares =[1,3,5]
nums = pares + impares
print(nums[0])

#Listas en Negativo
print(nums)
print(nums[2])
print(nums[-2])

#Listas en Negativo.V2
print(nums)
print(nums[4])
print(nums[-4])

#Eliminacion de Objetos
Letras =["A", "B", "C", "D", "E", "F", "G", "H"]
print(Letras)
del Letras[4]
print(Letras)
del Letras[1:4]
print(Letras)