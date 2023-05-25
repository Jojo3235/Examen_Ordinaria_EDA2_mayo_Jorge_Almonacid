import csv
from typing import List

class Pokemon:
    def __init__(self, nombre: str, tipo: str, hp: int, ataque: int, defensa: int, velocidad: int, sp_atk: int, sp_def: int, nivel: int):
        self.nombre = nombre
        self.tipo = tipo
        self.hp = hp
        self.ataque = ataque
        self.defensa = defensa
        self.velocidad = velocidad
        self.sp_atk = sp_atk
        self.sp_def = sp_def
        self.nivel = nivel

def cargar_pokemon_csv() -> List[Pokemon]:
    # Cargar los Pokemon desde el archivo CSV
    pokemon = []
    with open('pokemon.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Saltar la primera fila (encabezados)
        for row in reader:
            nombre, tipo, nivel = row
            hp = 100
            ataque = 100
            defensa = 100
            velocidad = 100
            sp_atk = 100
            sp_def = 100
            nivel = int(nivel)
            pokemon.append(Pokemon(nombre, tipo, hp, ataque, defensa, velocidad, sp_atk, sp_def, nivel))

    return pokemon

def cargar_pokemon_tablas_hash(pokemon: List[Pokemon]) -> tuple:
    # Crear las tablas hash
    tabla_nivel = {}
    tabla_tipo = {}

    # Cargar los Pokemon en las tablas hash
    for p in pokemon:
        nivel_key = p.nivel % 1000
        if nivel_key not in tabla_nivel:
            tabla_nivel[nivel_key] = []
        tabla_nivel[nivel_key].append(p)

        tipo_key = p.tipo[0]
        if tipo_key not in tabla_tipo:
            tabla_tipo[tipo_key] = []
        tabla_tipo[tipo_key].append(p)

    return tabla_nivel, tabla_tipo

def eliminar_fantasma(tabla_nivel: dict) -> None:
    # Verificar si el Pokemon Fantasma de nivel 187 está cargado
    fantasma_187 = None
    if 187 in tabla_nivel:
        for p in tabla_nivel[187]:
            if p.tipo == "Fantasma":
                fantasma_187 = p
                tabla_nivel[187].remove(p)
                print(f"Se ha eliminado el Pokemon {p.nombre} de nivel 187.")

def obtener_misiones(pokemon: List[Pokemon]) -> tuple:
    # Obtener los Pokemon terminados en 78 y 37
    mision_asalto = []
    mision_exploracion = []
    for p in pokemon:
        if p.nivel % 100 == 78:
            mision_asalto.append(p)
        elif p.nivel % 100 == 37:
            mision_exploracion.append(p)

    # Obtener los Pokemon de tipo Tierra y Fuego
    mision_exploracion_bosque = []
    mision_exterminacion_cueva = []
    for p in pokemon:
        if p.tipo.lower() == "tierra":
            mision_exploracion_bosque.append(p)
        elif p.tipo.lower() == "fuego":
            mision_exterminacion_cueva.append(p)

    return mision_asalto, mision_exploracion, mision_exploracion_bosque, mision_exterminacion_cueva

def main():
    pokemon = cargar_pokemon_csv()
    tabla_nivel, tabla_tipo = cargar_pokemon_tablas_hash(pokemon)

    # Obtener los Pokemon para las misiones
    mision_asalto, mision_exploracion, mision_exploracion_bosque, mision_exterminacion_cueva = obtener_misiones(pokemon)

    # Mostrar los Pokemon para cada misión
    print("Pokemon para la misión de asalto:")
    for p in mision_asalto:
        print(p.nombre)

    print("Pokemon para la misión de exploración:")
    for p in mision_exploracion:
        print(p.nombre)

    print("Pokemon para la misión de exploración del bosque:")
    for p in mision_exploracion_bosque:
        print(p.nombre)

    print("Pokemon para la misión de exterminación de la cueva:")
    for p in mision_exterminacion_cueva:
        print(p.nombre)

if __name__ == "__main__":
    main()