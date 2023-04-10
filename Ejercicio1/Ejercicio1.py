"""a. El día siguiente
Enunciado: modelar lo siguiente. Una empresa es propietaria de varios edificios y emplea a varios empleados. Un edificio está necesariamente ubicado en una ciudad y una ciudad está formada por varios edificios. Empresa, empleado, ciudad y edificio tienen cada uno un nombre. Estas ciudades incluyen New York, donde se encuentran los edificios A y B, y Los Ángeles, donde está el edificio C. Estos tres edificios son propiedad de YooHoo! que emplea a los Sres. Martin, Salim y la Sra. Xing.

Una vez definidas estas entidades, imagine que su programa es una película estadounidense de catástrofes, en la que se destruye New York. Implemente este evento para que todas las entidades del juego tengan en cuenta las consecuencias de este cataclismo.
"""

class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
    def asignar_empleados(self, empleados):
        self.empleados = empleados
    def asignar_edificios(self, edificios):
        self.edificios = edificios
        
class Edificio:
    def __init__(self, nombre):
        self.nombre = nombre
    def asignar_ciudad(self, ciudad):
        self.ciudad = ciudad     

class Ciudad:
    def __init__(self, nombre):
        self.nombre = nombre
    def asignar_edificios(self, edificios):
        self.edificios = edificios    

empleadoM = Empleado("Martin")
empleadoS = Empleado("Salim")
empleadoX = Empleado("Xing")

empresaYH = Empresa("YooHoo!")

edificioA = Edificio("A")
edificioB = Edificio("B")
edificioC = Edificio("C")

ciudadNY = Ciudad("New York")
ciudadLA = Ciudad("Los Angeles")

