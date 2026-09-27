class Electrodomestico:
    COLOR_DEF = "blanco"
    CONSUMO_DEF = 'F'
    PRECIO_DEF = 100.0
    PESO_DEF = 5.0

    def __init__(self, precio_base=PRECIO_DEF, color=COLOR_DEF, consumo_energetico=CONSUMO_DEF, peso=PESO_DEF):
        self._precio_base = precio_base
        self._peso = peso
        self._color = self._comprobar_color(color)
        self._consumo_energetico = self._comprobar_consumo_energetico(consumo_energetico)

    def _comprobar_consumo_energetico(self, letra):
        letra = str(letra).upper()
        if letra in ("A", "B", "C", "D", "E", "F"):
            return letra
        return self.CONSUMO_DEF

    def _comprobar_color(self, color):
        colores_validos = ["blanco", "negro", "rojo", "azul", "gris"]
        color_lower = str(color).lower()
        if color_lower in colores_validos:
            return color_lower
        return self.COLOR_DEF

    def precio_final(self):
        incremento = 0
        
        # Tabla de Precios (Letra)
        consumos = {'A': 100, 'B': 80, 'C': 60, 'D': 50, 'E': 30, 'F': 10}
        incremento += consumos.get(self._consumo_energetico, 0)

        # Tabla de Precios (Tamaño/Peso)
        if 0 <= self._peso < 20:
            incremento += 10
        elif 20 <= self._peso < 50:
            incremento += 50
        elif 50 <= self._peso < 80:
            incremento += 80
        elif self._peso >= 80:
            incremento += 100

        return self._precio_base + incremento
    def get_precio_base(self): return self._precio_base
    def get_color(self): return self._color
    def get_consumo_energetico(self): return self._consumo_energetico
    def get_peso(self): return self._peso

class Lavadora(Electrodomestico):
    CARGA_DEF = 5.0
    def __init__(self, precio_base=Electrodomestico.PRECIO_DEF, color=Electrodomestico.COLOR_DEF, 
                 consumo_energetico=Electrodomestico.CONSUMO_DEF, peso=Electrodomestico.PESO_DEF, carga=CARGA_DEF):

        super().__init__(precio_base, color, consumo_energetico, peso)
        self._carga = carga

    def get_carga(self):
        return self._carga

    def precio_final(self):
        precio = super().precio_final()
        if self._carga > 30:
            precio += 50
        return precio

class Television(Electrodomestico):

    RESOLUCION_DEF = 20.0
    SINTONIZADOR_DEF = False

    
    def __init__(self, precio_base=Electrodomestico.PRECIO_DEF, color=Electrodomestico.COLOR_DEF, 
                 consumo_energetico=Electrodomestico.CONSUMO_DEF, peso=Electrodomestico.PESO_DEF, 
                 resolucion=RESOLUCION_DEF, sintonizador_tdt=SINTONIZADOR_DEF):
      
        super().__init__(precio_base, color, consumo_energetico, peso)
        
        self._resolucion = resolucion
        self._sintonizador_tdt = sintonizador_tdt

    def get_resolucion(self): return self._resolucion
    def get_sintonizador_tdt(self): return self._sintonizador_tdt

    def precio_final(self):
        precio = super().precio_final()
        
        if self._resolucion > 40:
            precio += (precio * 0.30)
            
        if self._sintonizador_tdt:
            precio += 50
            
        return precio

if __name__ == "__main__":
  
    lista_electrodomesticos = [
        Electrodomestico(precio_base=200, color="Verde", consumo_energetico='C', peso=60), # Verde pasará a blanco
        Lavadora(precio_base=150, peso=30), # Solo precio y peso, resto por defecto
        Television(precio_base=500, color="negro", consumo_energetico='E', peso=80, resolucion=42, sintonizador_tdt=False),
        Electrodomestico(), # Constructor por defecto
        Electrodomestico(precio_base=600, color="gris", consumo_energetico='D', peso=20),
        Lavadora(precio_base=300, color="blanco", consumo_energetico='Z', peso=40, carga=40), # Z pasará a F
        Television(precio_base=250, peso=70), 
        Lavadora(precio_base=400, color="rojo", consumo_energetico='A', peso=100, carga=15),
        Television(precio_base=200, color="naranja", consumo_energetico='C', peso=60, resolucion=30, sintonizador_tdt=True),
        Electrodomestico(precio_base=50, peso=10)
    ]
    suma_electrodomesticos = 0
    suma_lavadoras = 0
    suma_televisiones = 0

    for electro in lista_electrodomesticos:
        precio_actual = electro.precio_final()
        suma_electrodomesticos += precio_actual
        
        if isinstance(electro, Lavadora):
            suma_lavadoras += precio_actual
        elif isinstance(electro, Television):
            suma_televisiones += precio_actual

    print("\n--- REPORTE DE VENTAS ---")
    print(f"Total Lavadoras: ${suma_lavadoras:.2f}")
    print(f"Total Televisiones: ${suma_televisiones:.2f}")
    print(f"Total Electrodomésticos (Suma global): ${suma_electrodomesticos:.2f}")
