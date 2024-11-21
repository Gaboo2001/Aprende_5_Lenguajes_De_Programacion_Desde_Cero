alumnos = {"Gabo": 23, "Pedro": 26, "laura":24}
alumnos["Gabo"] = 18 #Aqui actualizamos el valor de un elemento
print(alumnos)
alumnos ["Rubi"] = 27 #Aqui añadimos un valor completo desde el nombre hasta el valor
print(alumnos)
del alumnos ["Pedro"] #con "del" eliminamos el valor que encuentre igual
print(alumnos)

print("Gabo" in alumnos) #Devuelve un valor bool en caso de que si exista la coincidencia da true
print("Ronaldo" in alumnos) #Este da false porque no existe ronaldo dentro del diccionario
