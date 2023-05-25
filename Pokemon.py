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
#fuego, agua, planta, dragon, hada, veneno, acero, psiquico, bicho, roca, tierra, volador, fantasma, normal, lucha, hielo, electrico
    def clasificacion(self):
        if self.tipo.lower() == 'planta':
            print("Tipo planta")
        elif self.tipo.lower() == 'fuego':
            print("Tipo fuego")
        elif self.tipo.lower() == 'agua':
            print("Tipo agua")    
        elif self.tipo.lower() == 'dragon':
            print("Tipo dragon")
        elif self.tipo.lower() == 'hada':
            print("Tipo hada")
        elif self.tipo.lower() == 'veneno':
            print("Tipo veneno")
        elif self.tipo.lower() == 'acero':
            print("Tipo acero")    
        elif self.tipo.lower() == 'psiquico':
            print("Tipo psiquico")
        elif self.tipo.lower() == 'bicho':
            print("Tipo bicho")
        elif self.tipo.lower() == 'roca':
            print("Tipo roca")
        elif self.tipo.lower() == 'tierra': 
            print("Tipo tierra")
        elif self.tipo.lower() == 'volador':
            print("Tipo volador")
        elif self.tipo.lower() == 'fantasma':
            print("Tipo fantasma")
        elif self.tipo.lower() == 'normal':
            print("Tipo normal")
        elif self.tipo.lower() == 'lucha':
            print("Tipo lucha")
        elif self.tipo.lower() == 'hielo':
            print("Tipo hielo")
        elif self.tipo.lower() == 'electrico':
            print("Tipo electrico")
        else:
            print("Tipo desconocido")