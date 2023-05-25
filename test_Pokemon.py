import unittest
from Pokemon import Pokemon

class TestPokemon(unittest.TestCase):
    def test_creacion_pokemon(self):
        poke1 = Pokemon('Charmander', 'Fuego', 39, 52, 43, 60, 50, 65, 17)
        self.assertEqual(poke1.nombre, 'Charmander')
        self.assertEqual(poke1.tipo, 'Fuego')
        self.assertEqual(poke1.ps, 39)
        self.assertEqual(poke1.ataque, 52)
        self.assertEqual(poke1.defensa, 43)
        self.assertEqual(poke1.ataque_especial, 60)
        self.assertEqual(poke1.defensa_especial, 50)
        self.assertEqual(poke1.velocidad, 65)

        poke2 = Pokemon('Squirtle', 'Agua', 44, 48, 65, 50, 64, 43, 16)
        self.assertEqual(poke2.nombre, 'Squirtle')
        self.assertEqual(poke2.tipo, 'Agua')
        self.assertEqual(poke2.ps, 44)
        self.assertEqual(poke2.ataque, 48)
        self.assertEqual(poke2.defensa, 65)
        self.assertEqual(poke2.ataque_especial, 50)
        self.assertEqual(poke2.defensa_especial, 64)
        self.assertEqual(poke2.velocidad, 43)

        poke3 = Pokemon('Bulbasaur', 'Planta', 45, 49, 49, 65, 65, 45, 15)
        self.assertEqual(poke3.nombre, 'Bulbasaur')
        self.assertEqual(poke3.tipo, 'Planta')
        self.assertEqual(poke3.ps, 45)
        self.assertEqual(poke3.ataque, 49)
        self.assertEqual(poke3.defensa, 49)
        self.assertEqual(poke3.ataque_especial, 65)
        self.assertEqual(poke3.defensa_especial, 65)
        self.assertEqual(poke3.velocidad, 45)

    def test_clasificacion(self):
        poke1 = Pokemon('Charmander', 'Fuego', 39, 52, 43, 60, 50, 65, 43)
        self.assertEqual(poke1.clasificacion(), 'Tipo fuego')

        poke2 = Pokemon('Squirtle', 'Agua', 44, 48, 65, 50, 64, 43, 50)
        self.assertEqual(poke2.clasificacion(), 'Tipo agua')

        poke3 = Pokemon('Bulbasaur', 'Planta', 45, 49, 49, 65, 65, 45, 80)
        self.assertEqual(poke3.clasificacion(), 'Tipo planta')

        poke4 = Pokemon('Pikachu', 'Electrico', 35, 55, 40, 50, 50, 90, 12)
        self.assertEqual(poke4.clasificacion(), 'Tipo electrico')

        poke5 = Pokemon('Eevee', 'Normal', 55, 55, 50, 45, 65, 55, 32)
        self.assertEqual(poke5.clasificacion(), 'Tipo normal')

        poke6 = Pokemon('Mewtwo', 'Psiquico', 106, 110, 90, 154, 90, 130, 234)
        self.assertEqual(poke6.clasificacion(), 'Tipo psiquico')

        poke7 = Pokemon('Mew', 'Psiquico', 100, 100, 100, 100, 100, 100, 23)
        self.assertEqual(poke7.clasificacion(), 'Tipo psiquico')

        poke8 = Pokemon('Gengar', 'Fantasma', 60, 65, 60, 130, 75, 110, 23)
        self.assertEqual(poke8.clasificacion(), 'Tipo fantasma')

        poke9 = Pokemon('Gyarados', 'Agua', 95, 125, 79, 60, 100, 81, 23)
        self.assertEqual(poke9.clasificacion(), 'Tipo agua')

        poke10 = Pokemon('Golem', 'Roca', 80, 120, 130, 55, 65, 45, 5)
        self.assertEqual(poke10.clasificacion(), 'Tipo roca')

        poke11 = Pokemon('Onix', 'Roca', 35, 45, 160, 30, 45, 70, 23)
        self.assertEqual(poke11.clasificacion(), 'Tipo roca')

        poke12 = Pokemon('Pidgeot', 'Volador', 83, 80, 75, 70, 70, 101, 563)
        self.assertEqual(poke12.clasificacion(), 'Tipo volador')

        poke13 = Pokemon('Butterfree', 'Bicho', 60, 45, 50, 90, 80, 70, 23)
        self.assertEqual(poke13.clasificacion(), 'Tipo bicho')
