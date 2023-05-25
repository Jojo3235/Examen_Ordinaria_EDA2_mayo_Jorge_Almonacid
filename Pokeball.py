from datetime import datetime

class Pokeball:
    def __init__(self, peso, nombre, precio, fecha_fabricacion):
        self.peso = peso
        self.nombre = nombre
        self.precio = precio
        self.fecha_fabricacion = fecha_fabricacion
        print(f"Se ha creado la Pokeball {self.nombre} con éxito.")

    def __str__(self):
        return f"Pokeball {self.nombre}\n" \
               f"Peso: {self.peso} gramos\n" \
               f"Precio: {self.precio} monedas\n" \
               f"Fecha de fabricación: {self.fecha_fabricacion}"

