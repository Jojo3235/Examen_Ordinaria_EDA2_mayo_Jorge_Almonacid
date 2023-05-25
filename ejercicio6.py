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

def generar_pokemon() -> List[Pokemon]:
    # Generar 800 Pokemon con nivel aleatorio
    pokemon = []
    for i in range(800):
        pokemon.append(Pokemon(f"Pokemon {i}", "Agua", 100, 100, 100, 100, 100, 100, i))
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
        if p.tipo == "Tierra":
            mision_exploracion_bosque.append(p)
        elif p.tipo == "Fuego":
            mision_exterminacion_cueva.append(p)

    return mision_asalto, mision_exploracion, mision_exploracion_bosque, mision_exterminacion_cueva

def guardar_pokemon_csv(pokemon: List[Pokemon]) -> None:
    # Guardar los Pokemon en un archivo CSV
    with open('pokemon.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Nombre', 'Tipo', 'Nivel'])
        for p in pokemon:
            writer.writerow([p.nombre, p.tipo, p.nivel])

def main():
    #Cargar los pokemon del csv
    pokemon = []
    with open('pokemon.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            pokemon.append(Pokemon(row[0], row[1], 100, 100, 100, 100, 100, 100, int(row[2])))

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
