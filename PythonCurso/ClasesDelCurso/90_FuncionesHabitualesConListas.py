edades = [23,25,27,28,23,42,23]

print(edades.count(23)) #El conunt es para contar cuantos elementos que queramos hay

edades1= [12,1,2,3,4,5,6]
edades.extend(edades1) #Agregamos nuevos elemetos quu queramos
print(edades)

edades2 = [23,25,27,28,23,42,23]
print(edades2.pop(0)) #Elminimanos la posicion de algun elemtno que queramos
print(edades2)

nombres = ["Gabo","Sara","Jeimy","Maggy","Ximena"]
nombres.reverse() #Imprime primero la ultima posicion
print(nombres)

nombres.sort() #acomoda por orden
print(nombres)
edades2.sort() #acomoda por numero

print(edades2)