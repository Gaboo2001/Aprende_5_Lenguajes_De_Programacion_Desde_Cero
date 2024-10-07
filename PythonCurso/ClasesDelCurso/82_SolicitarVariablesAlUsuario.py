#Forma comun de pedir datos
edad = input ("Introduce tu edad: ")
nombre = input("Introduce tu nombre: ")
print("Tu nombre es " + nombre + " y tienes " + edad + " años")


print("//////////////////////////////////////////")

edad1 = int (input("Introduce tu edad: "))
nombre1 = input("Introduce tu nombre: ")
print("Tu nombre es " + nombre1 + " y tienes " + str(edad1) + " años") #el str en edad es el casteo que se esta haciendo para
#edad porque al principio al declarar edad1 la estoy casteando como int y para imprimir el input debe de ser string (str)

