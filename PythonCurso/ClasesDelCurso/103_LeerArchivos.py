archivo=open("alumnos.txt", "r")
print(archivo.readable())
#print(archivo.read()) #Leer todo el contenido
print(archivo.readline()) #readline lee el archivo por cada linea
print(archivo.readline())

#for alumno in archivo.readlines():
    #print(alumno)

archivo.close()

