class Pokemon:
    def __init__(self, nombre, tipo, ps, ataque, defensa, ataque_especial, defensa_especial, velocidad):
        self.nombre = nombre
        self.tipo = tipo
        self.ps = ps
        self.ataque = ataque
        self.defensa = defensa
        self.ataque_especial = ataque_especial
        self.defensa_especial = defensa_especial
        self.velocidad = velocidad
        print(f"Se ha creado el Pokemon {self.nombre} de tipo {self.tipo} con éxito.")

    def clasificacion(self):
        if self.tipo == "Agua":
            return "Tipo agua"
        elif self.tipo == "Fuego":
            return "Tipo fuego"
        elif self.tipo == "Planta":
            return "Tipo planta"
        elif self.tipo == "Electrico":
            return "Tipo electrico"
        elif self.tipo == "Normal":
            return "Tipo normal"
        elif self.tipo == "Psiquico":
            return "Tipo psiquico"
        elif self.tipo == "Fantasma":
            return "Tipo fantasma"
        elif self.tipo == "Roca":
            return "Tipo roca"
        elif self.tipo == "Volador":
            return "Tipo volador"
        elif self.tipo == "Bicho":
            return "Tipo bicho"
        elif self.tipo == "Tierra":
            return "Tipo tierra"
        elif self.tipo == "Hielo":
            return "Tipo hielo"
        elif self.tipo == "Lucha":
            return "Tipo lucha"
        elif self.tipo == "Veneno":
            return "Tipo veneno"
        elif self.tipo == "Acero":
            return "Tipo acero"
        elif self.tipo == "Dragon":
            return "Tipo dragon"
        elif self.tipo == "Siniestro":
            return "Tipo siniestro"
        elif self.tipo == "Hada":
            return "Tipo hada"
        else:
            return "Tipo de Pokemon no reconocido."