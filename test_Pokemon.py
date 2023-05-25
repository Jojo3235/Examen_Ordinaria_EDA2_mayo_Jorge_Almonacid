import unittest
from Pokemon import Pokemon

class TestPokemon(unittest.TestCase):
    def test_creacion_pokemon(self):
        poke1 = Pokemon('Charmander', 'Fuego', 39, 52, 43, 60, 50, 65)
        self.assertEqual(poke1.nombre, 'Charmander')
        self.assertEqual(poke1.tipo, 'Fuego')
        self.assertEqual(poke1.ps, 39)
        self.assertEqual(poke1.ataque, 52)
        self.assertEqual(poke1.defensa, 43)
        self.assertEqual(poke1.ataque_especial, 60)
        self.assertEqual(poke1.defensa_especial, 50)
        self.assertEqual(poke1.velocidad, 65)

        poke2 = Pokemon('Squirtle', 'Agua', 44, 48, 65, 50, 64, 43)
        self.assertEqual(poke2.nombre, 'Squirtle')
        self.assertEqual(poke2.tipo, 'Agua')
        self.assertEqual(poke2.ps, 44)
        self.assertEqual(poke2.ataque, 48)
        self.assertEqual(poke2.defensa, 65)
        self.assertEqual(poke2.ataque_especial, 50)
        self.assertEqual(poke2.defensa_especial, 64)
        self.assertEqual(poke2.velocidad, 43)

        poke3 = Pokemon('Bulbasaur', 'Planta', 45, 49, 49, 65, 65, 45)
        self.assertEqual(poke3.nombre, 'Bulbasaur')
        self.assertEqual(poke3.tipo, 'Planta')
        self.assertEqual(poke3.ps, 45)
        self.assertEqual(poke3.ataque, 49)
        self.assertEqual(poke3.defensa, 49)
        self.assertEqual(poke3.ataque_especial, 65)
        self.assertEqual(poke3.defensa_especial, 65)
        self.assertEqual(poke3.velocidad, 45)

    def test_clasificacion(self):
        poke1 = Pokemon('Charmander', 'Fuego', 39, 52, 43, 60, 50, 65)
        self.assertEqual(poke1.clasificacion(), 'Charmander es de tipo Fuego')

        poke2 = Pokemon('Squirtle', 'Agua', 44, 48, 65, 50, 64, 43)
        self.assertEqual(poke2.clasificacion(), 'Squirtle es de tipo Agua')

        poke3 = Pokemon('Bulbasaur', 'Planta', 45, 49, 49, 65, 65, 45)
        self.assertEqual(poke3.clasificacion(), 'Bulbasaur es de tipo Planta')

        poke4 = Pokemon('Pikachu', 'Electrico', 35, 55, 40, 50, 50, 90)
        self.assertEqual(poke4.clasificacion(), 'Pikachu es de tipo Electrico')

        poke5 = Pokemon('Eevee', 'Normal', 55, 55, 50, 45, 65, 55)
        self.assertEqual(poke5.clasificacion(), 'Eevee es de tipo Normal')

        poke6 = Pokemon('Mewtwo', 'Psiquico', 106, 110, 90, 154, 90, 130)
        self.assertEqual(poke6.clasificacion(), 'Mewtwo es de tipo Psiquico')

        poke7 = Pokemon('Mew', 'Psiquico', 100, 100, 100, 100, 100, 100)
        self.assertEqual(poke7.clasificacion(), 'Mew es de tipo Psiquico')

        poke8 = Pokemon('Gengar', 'Fantasma', 60, 65, 60, 130, 75, 110)
        self.assertEqual(poke8.clasificacion(), 'Gengar es de tipo Fantasma')

        poke9 = Pokemon('Gyarados', 'Agua', 95, 125, 79, 60, 100, 81)
        self.assertEqual(poke9.clasificacion(), 'Gyarados es de tipo Agua')

        poke10 = Pokemon('Golem', 'Roca', 80, 120, 130, 55, 65, 45)
        self.assertEqual(poke10.clasificacion(), 'Golem es de tipo Roca')

        poke11 = Pokemon('Onix', 'Roca', 35, 45, 160, 30, 45, 70)
        self.assertEqual(poke11.clasificacion(), 'Onix es de tipo Roca')

        poke12 = Pokemon('Pidgeot', 'Volador', 83, 80, 75, 70, 70, 101)
        self.assertEqual(poke12.clasificacion(), 'Pidgeot es de tipo Volador')

        poke13 = Pokemon('Butterfree', 'Bicho', 60, 45, 50, 90, 80, 70)
        self.assertEqual(poke13.clasificacion(), 'Tipo bicho')
