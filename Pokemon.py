class Pokemon:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        print(f"Se ha creado el Pokemon {self.nombre} de tipo {self.tipo} con éxito.")

    def clasificacion(self):
        if self.tipo == "Agua":
            print("Este Pokemon es de tipo Agua y su clasificación es: PS: 45, Ataque: 49, Defensa: 49, Ataque Especial: 65, Defensa Especial: 65, Velocidad: 45")
        elif self.tipo == "Fuego":
            print("Este Pokemon es de tipo Fuego y su clasificación es: PS: 39, Ataque: 52, Defensa: 43, Ataque Especial: 60, Defensa Especial: 50, Velocidad: 65")
        elif self.tipo == "Planta":
            print("Este Pokemon es de tipo Planta y su clasificación es: PS: 45, Ataque: 49, Defensa: 49, Ataque Especial: 65, Defensa Especial: 65, Velocidad: 45")
        else:
            print("Tipo de Pokemon no reconocido.")