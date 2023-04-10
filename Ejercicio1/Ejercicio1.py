"""a. El día siguiente
Enunciado: modelar lo siguiente. Una empresa es propietaria de varios edificios y emplea a varios empleados. Un edificio está necesariamente ubicado en una ciudad y una ciudad está formada por varios edificios. Empresa, empleado, ciudad y edificio tienen cada uno un nombre. Estas ciudades incluyen New York, donde se encuentran los edificios A y B, y Los Ángeles, donde está el edificio C. Estos tres edificios son propiedad de YooHoo! que emplea a los Sres. Martin, Salim y la Sra. Xing.

Una vez definidas estas entidades, imagine que su programa es una película estadounidense de catástrofes, en la que se destruye New York. Implemente este evento para que todas las entidades del juego tengan en cuenta las consecuencias de este cataclismo.
"""

class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre
    #hago la funcion asignar_empresa pq quiero y para no liarme
    def asignar_empresa(self, empresa):
        self.empresa = empresa
    def __del__(self):
        print("Empleado", self.nombre ,"destruido")

class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
    def asignar_empleados(self, empleados):
        self.empleados = empleados
    def asignar_edificios(self, edificios):
        self.edificios = edificios
    def __del__(self):
        for empleado in self.empleados:
            del(empleado)
        print("Empresa", self.nombre ,"destruida")
        
class Edificio:
    def __init__(self, nombre):
        self.nombre = nombre
    def asignar_ciudad(self, ciudad):
        self.ciudad = ciudad     
#hago la funcion asignar_empresa pq quiero y para no liarme
    def asignar_empresa(self, empresa):
        self.empresa = empresa
    def __del__(self):
        del(self.empresa)
        print("Edificio", self.nombre ,"destruido")

class Ciudad:
    def __init__(self, nombre):
        self.nombre = nombre
    def asignar_edificios(self, edificios):
        self.edificios = edificios 
    def __del__(self):
        for edificio in self.edificios:
            del(edificio)
        print("Ciudad", self.nombre ,"destruida")   

empleadoM = Empleado("Martin")
empleadoS = Empleado("Salim")
empleadoX = Empleado("Xing")

empresaYH = Empresa("YooHoo!")

edificioA = Edificio("A")
edificioB = Edificio("B")
edificioC = Edificio("C")

ciudadNY = Ciudad("New York")
ciudadLA = Ciudad("Los Angeles")

ciudadNY.asignar_edificios([edificioA, edificioB])
edificioA.asignar_ciudad(ciudadNY)
edificioB.asignar_ciudad(ciudadNY)

ciudadLA.asignar_edificios([edificioC])
edificioC.asignar_ciudad(ciudadLA)

empresaYH.asignar_edificios([edificioA, edificioB, edificioC])
empresaYH.asignar_empleados([empleadoM, empleadoS, empleadoX])
 
empleadoM.asignar_empresa(empresaYH)
empleadoS.asignar_empresa(empresaYH)
empleadoX.asignar_empresa(empresaYH)

edificioA.asignar_empresa(empresaYH)
edificioB.asignar_empresa(empresaYH)
edificioC.asignar_empresa(empresaYH)

del(ciudadNY)
