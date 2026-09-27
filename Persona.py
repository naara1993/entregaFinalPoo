class Persona:
    #constantes
    INFRAPESO=1
    PESO_IDEAL=0
    SOBREPESO=1

def __init__(self,nombre="",edad=0,sexo="H",peso=0.0,altura=0.0):
    self.nombre=nombre
    self.edad=edad
    self.sexo=sexo
    self.peso=peso
    self.altura=altura
    self.__DNI = self.__genera_DNI()

def __comprobar_sexo(self,sexo):
    Sexo= sexo.upper()
    if Sexo=="H" or Sexo=="M":
        return Sexo
    return "H"

def __genera_DNI(self):
        # Genera un número aleatorio de 8 cifras y le asigna una letra
        num_dni = random.randint(0, 99999999)
        resto = num_dni % 23
        letras = 'TRWAGMYFPDXBNJZSQVHLCKE'
        letra_correspondiente = letras[resto]
        return f"{num_dni:08d}{letra_correspondiente}"

def calcular_IMC(self):
        if self.__altura == 0:
            return self.INFRAPESO
        imc = self.__peso / (self.__altura ** 2)
        if imc < 20:
            return self.INFRAPESO
        elif 20 <= imc <= 25:
            return self.PESO_IDEAL
        else:
            return self.SOBREPESO

def es_mayor_de_edad(self):
        return self.__edad >=18

def __str__(self):
        return f"Nombre: {self.__nombre}\nEdad: {self.__edad}\nSexo: {self.__sexo}\nPeso: {self.__peso} kg\nAltura: {self.__altura} m\nDNI: {self.__DNI}"

def set_nombre(self, nombre): self.__nombre = nombre
def set_edad(self, edad): self.__edad = edad
def set_sexo(self, sexo): self.__sexo = self.__comprobar_sexo(sexo)
def set_peso(self, peso): self.__peso = peso
def set_altura(self, altura): self.__altura = altura

if __name__ == "__main__":
    print("--- INGRESO DE DATOS ---")
    nombre_input = input("Introduce el nombre: ")
    edad_input = int(input("Introduce la edad: "))
    sexo_input = input("Introduce el sexo (H/M): ")
    peso_input = float(input("Introduce el peso (kg): "))
    altura_input = float(input("Introduce la altura (m): "))

    
    persona1 = Persona(nombre_input, edad_input, sexo_input, peso_input, altura_input)
    
    persona2 = Persona(nombre_input, edad_input, sexo_input)
    
    persona3 = Persona()
    persona3.set_nombre("Laura")
    persona3.set_edad(25)
    persona3.set_sexo('M')
    persona3.set_peso(60.5)
    persona3.set_altura(1.68)

    lista_personas = [persona1, persona2, persona3]
    
    for i, p in enumerate(lista_personas, start=1):
        print(f"\nResultados Persona {i}:")
        print(p) 


        resultado_imc = p.calcular_IMC()
        if resultado_imc == Persona.INFRAPESO:
            print("Estado de peso: Por debajo de su peso ideal (-1)")
        elif resultado_imc == Persona.PESO_IDEAL:
            print("Estado de peso: En su peso ideal (0)")
        else:
            print("Estado de peso: Tiene sobrepeso (1)")
            
        if p.es_mayor_de_edad():
            print("Edad: Es mayor de edad.")
        else:
            print("Edad: Es menor de edad.")