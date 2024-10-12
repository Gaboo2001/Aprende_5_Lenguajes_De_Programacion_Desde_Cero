

texto = "hi I am the Best"
print(len(texto)) # imprime el numero de caracteres de la cadena contando espacios
print("")

print(texto.capitalize()) #Convierte la primera letra a mayuscula y todo lo demas en minusculas

print(texto.replace("Best","mejor")) #remplaza una palaba o otra

print(texto.index("B")) #Imprime el lugar de la letra que estamos buscndo
print(texto.index("am")) #imprime donde se encuantra el primer valor en este caso a

print(texto.lower()) #todo a minusculas

print(texto.upper()) #todo a mayusculas

print(texto.islower()) #con el "is" se pregunta si todo esta en minuscuals y como no es asi da falso pero si se cambia toda la cadena a minisculas el resultado seria true

print (texto.upper().isupper()) #Aqui primero convertimos a mayusculas y despues es comparado preguntado si todo es mayusculas por lo tanto es true