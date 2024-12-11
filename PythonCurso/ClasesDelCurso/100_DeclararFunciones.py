


def saludo():
    print("Hola")

saludo()

def saludo1(nombre):
    print("Hola, "+nombre)

saludo1("Gabo")
saludo1("Jazmin")
saludo1("Gabriela")


def saludo2(nombre, edad):
    print("Te llamas " +nombre+ " y tienes " + edad + " años.")

saludo2("Gabo", "25")
saludo2("Jazmin", "24")
saludo2("Elsi", "22")




def fuerza(peso):
    g=9.81
    print(peso*g)

fuerza(80)

def saludo3(nombre, edad):
    print("Te llamas " +nombre+ " y tienes " + str(edad) + " años.")
nom = "Gabriel"
edad = 33
saludo3(nom, edad)
