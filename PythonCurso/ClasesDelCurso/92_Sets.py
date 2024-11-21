nombres1 = {"Cristiano", "Henry", "Neymar", "Mbappe", "Salah"} #La diferecia de set con listas
# es que aqui no tiene indices y se ordenan en aleatorio

#nombres.add = {"Messi"}
print(nombres1)
#print(nombres1[0])#Esta linea da error porque al no tener indice y buscar el indice 0 no existe en el set


############################################################

nombres2 = {"Cristiano", "Henry", "Neymar", "Mbappe", "Salah",22,34,54,True}
#En el set puedes agrgar elementos de cualquier tipo string, numeros, boleanos
print(nombres2)

##########################################################################
nombres3 = {"Cristiano", "Henry", "Neymar", "Mbappe", "Salah"}
nombres3.add ("Jimenez") #Aqui añadimos un alemento al set
print(nombres3)
print(len(nombres3)) #El len me da el conteo de elementos
############################################################################
nombres4 = {"Cristiano", "Henry", "Neymar", "Mbappe", "Salah"}
edades = {21,22,32,45,22}
nombres4.update(edades) #Aqui añade al set las edades
print(nombres4)

#############################################################################33
nombres5 = {"Cristiano", "Henry", "Neymar", "Mbappe", "Salah"}
nombres5.remove("Neymar") #Con remove se elimina el elemento
nombres5.discard("Ronaldo")
print(nombres5)