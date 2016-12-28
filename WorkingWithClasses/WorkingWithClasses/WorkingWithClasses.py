class Perro(object):
    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad

    def ladra(self):
        print(self.nombre, "dice Woof!")

mascota = Perro("Max", "Poodle", 3)
#mascota.ladra()

print ("Clase:", mascota.__class__)
print ("Tipo:", type(mascota))
