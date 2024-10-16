nombres = ["Gabo","Sara","Jeimy","Maggy","Ximena"]
edades = [23,22,21]
aprobados = [True, False, True]


#El append es para añadir elementos a las listas

#nombres.append("Belen")
#edades.append(28)
#aprobados.append("True")

#print(nombres)
#print(edades)
#print(aprobados)

#otra funcion es insert que toma la posicion en cualquier elemento de la lista
#nombres.insert(0,"Carmen")
#edades.insert(0,"17")
#print(nombres)
#print(edades)

# Para eliminar podemos usar romove
#nombres.remove("Maggy") #Busca el valor desado y lo elimina
#otra opcion es clear pero este elimina todos los elementos de la lista
#edades.clear()
#print(edades)

#el index es para que me diga la posicion de algun elemento
#print(nombres.index("Ximena"))
#print(nombres)

#print("Gabriel" in nombres) #devuelve true o false para ver si esta el elemento dentreo de la lista
#print("Gabo" in nombres)

edades[1] +=10
print(edades)