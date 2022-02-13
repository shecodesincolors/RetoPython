#Ejemplo 5
""""
from datetime import datetime

print("Ingresa tu dd/mm/aa para comprobar si esta fecha es válida o no lo es:")
while True:
    try:
        ValidarFecha=input('\nFecha(dd/mm/aa): ')
        fecha=datetime.strptime(ValidarFecha,"%d/%m/%Y")
        print("\nTu fecha es válida")
        
    except:
        print("\nLa fecha que ingresaste no es válida")
"""

#RETO
from posixpath import split
from pprint import pprint
padawans=[]

def inscripcionPadawans(nombre,apellido,edad,temas):
    temas= temas.lower().split(", ")
    mayorEdad= True if edad >= 18 else False
    try:
        padawans.append({"nombre":nombre, "apellido":apellido, "edad":edad, "temas":temas})
    except:
        return "No se agregaron los datos"
    return "\n\nPADAWAN REGISTRADA EXITOSAMENTE!\n"


while True:
    print('Directorio Padawan ¡Regístrate!')
    print("1.Agregar estudiante")
    print("2.Ver directorio") 
    print("3.Salir")
    
    opcion = int(input()) 
    if opcion == 1:
        nombre = str(input("Ingresa nombre estudiante:"))
        apellido= str(input("Apellido:"))
        edad = int(input("Ingresa edad:"))
        if edad>=18:
            print('\nEres mayor de edad\n')
        else:
            print('\nEres menor de edad\n')
        print("Los temas que puedes llevar son:Python,JavaScript,BBDD,JAVA y/o Linux\n")
        temas = str(input("Ingresa tema/s de tu elección:"))
        print(inscripcionPadawans(nombre,apellido,edad,temas),"\n\n")
    elif opcion == 2:
        print(padawans)

    elif opcion == 3:
        print("\nAdiós")
        break
    else:
        break
