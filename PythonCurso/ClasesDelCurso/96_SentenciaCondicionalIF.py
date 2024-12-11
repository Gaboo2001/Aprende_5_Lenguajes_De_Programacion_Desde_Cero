num1= 10
num2 = 7
if num1>num2:
    print("el numero " + str(num1) + " es mayor que el número " + str(num2))

num1= 10
num2 = 7
if num1<num2:
    print("el numero " + str(num1) + " es mayor que el número " + str(num2)) #Esto no se imprime porque no
    #se cumple la condicion
##################################################################################
print("-------------------------------------------------------------------------------")
num3 = 10
num4 = 10
if num3 > num4:
    print("El numero " + str(num3) + " es mayor que el numero " + str (num4))
else:
    print("El numero " + str (num3) + " es mayor que el numero " + str(num4)) #ESTO SIMPRE SE VA A ACUMPLIR
    #UNQUE NO SEA VERDADERO COMO EN ESTE CASO LOS NUMEROS SON IGUALES PERO IMPRIME QUE ALGUNO ES MAYOR QUE
#####################################################################################33
print("-------------------------------------------------------------------------------")
num5 = 6
num6 = 5
if num5 > num6:
    print("El numero " + str(num5) + " es mayor que el numeroo " + str (num6)) #Se va imprimir esto porque 6 es mayor a 5
elif num5 < num6:
    print("El numero "+ str(num6)+ " es mayor que el numero " +str(num5)) #NO se sumple porque  5 no es mayor que 6
else:
    print("El numero " + str (num3) + " es mayor que el numero " + str(num4)) # Esto tampoco se cumple

print()

#Segundo camino
num5 = 4
num6 = 5
if num5 > num6:
    print("El numero " + str(num5) + " es mayor que el numeroo " + str (num6)) #No se cumple
elif num5 < num6:
    print("El numero "+ str(num6)+ " es mayor que el numeroaa " +str(num5)) #Se cumple porque 4 es menor a 5
else:
    print("El numero " + str (num3) + " es mayor que el numero " + str(num4)) # Esto tampoco se cumple

print()
#Tercer camino
num5 = 5
num6 = 5
if num5 > num6:
    print("El numero " + str(num5) + " es mayor que el numeroo " + str (num6)) #No se cumple
elif num5 < num6:
    print("El numero "+ str(num6)+ " es mayor que el numeroaa " +str(num5)) #No se cumple
else:
    print("Los dos numeros son iguales") #Esto se cumple


print("-------------------------------------------------------------------------------")
num6 = 100
num7 = 1011
num8 = 1
#NOTA HAY QUE IR JUGANDO CON ESTOS NUMEROS PARA VER QUE CONDICION SE CUMPLE
print(num6)
print(num7)
print(num8)

if num6 >= num7 and num6>= num8:
    print("El numero mayor " + str (num6) +" es el mayor" " IF")
elif num7 >= num6 and num7 >= num8:
    print("El numero mayor " + str (num7) +" es el mayor" " ELIF")
else:
    print("El numero mayor " + str (num8) +" es el mayor") #Como no se cumplen ninguna de las anteriores condiciones entra esta


print("-------------------------------------------------------------------------------")
num9 = 2
if num9 < 10:
    print("El numero es menor que 10")
elif num9 < 20:
    print("El numero es menor que 20")
elif num9 < 30: #LOS  "ELIF" SE PUEDEN USAR LAS VECES QUE QUERAMOS
    print("El numero es menor que 30")
else:
    print("El numero es mayor que 30")
#PARA ESTE ULTIMO EJEMPLO SE PUEDE VER QUE USAMOS AL ASIGANARLE EL NUMERO 2 AL NUM9 SE CUMPLEN 3 CONDICIONES PERO SOLO IMPRIME 1 QUE ES LA DE MENOR QUE 10
#ESTO PASA PORQUE EL CODIGO SE LEE HACIA ABAJO ENTONCES CUANDO LA PRIMERA CONDICION SE CUMPLE SE LANZA ESA
