# archivo = open ("alumnos.txt", "a") #a = anexar
# 
# archivo.write("\nJuan") #En esta linea agrega lo que queremos a la nota pero sin eliminar los anteriores 
# #no es necesario escribir 5 veces archivo.write para agregar cosas
# archivo.close()

#-----------------------------------------------------------------
archivo = open ("alumnos.txt", "w") #w = sobreescribir
archivo.write("Gabriel") #Borra todo el contenido del archivo y solo aagrega esto
archivo.close()
#-----------------------------------------------------------------
#Crear un nuevo archivo txt
#Tambien podemos crear un archivo txt asi
archivo = open ("alumnos1.txt", "w") #w = sobreescribir #Simplemente dando un nombre que no exista en este caso (alumnos1.txt)
#no existe pero al ejecutar se crea el archivo con lo que se indica
archivo.write("Bienvenido")
archivo.close()