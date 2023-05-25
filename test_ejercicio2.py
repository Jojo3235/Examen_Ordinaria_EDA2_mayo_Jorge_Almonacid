from ejercicio2 import Pokemon
import unittest

class TestPokemon(unittest.TestCase):
    def test_str(self):
        poke1 = Pokemon('Charmander', 'Fuego', 39, 52, 43, 60, 50, 65, 16)
        self.assertEqual(str(poke1), "Pokemon Charmander de tipo Fuego con 39 puntos de salud, 52 puntos de ataque, 43 puntos de defensa, 60 puntos de ataque especial, 50 puntos de defensa especial y 65 puntos de velocidad.")

        poke2 = Pokemon('Squirtle', 'Agua', 44, 48, 65, 50, 64, 43, 17)
        self.assertEqual(str(poke2), "Pokemon Squirtle de tipo Agua con 44 puntos de salud, 48 puntos de ataque, 65 puntos de defensa, 50 puntos de ataque especial, 64 puntos de defensa especial y 43 puntos de velocidad.")

        poke3 = Pokemon('Bulbasaur', 'Planta', 45, 49, 49, 65, 65, 45, 15)
        self.assertEqual(str(poke3), "Pokemon Bulbasaur de tipo Planta con 45 puntos de salud, 49 puntos de ataque, 49 puntos de defensa, 65 puntos de ataque especial, 65 puntos de defensa especial y 45 puntos de velocidad.")

        poke4 = Pokemon('Pikachu', 'Electrico', 35, 55, 40, 50, 50, 90, 89)
        self.assertEqual(str(poke4), "Pokemon Pikachu de tipo Electrico con 35 puntos de salud, 55 puntos de ataque, 40 puntos de defensa, 50 puntos de ataque especial, 50 puntos de defensa especial y 90 puntos de velocidad.")

        poke5 = Pokemon('Eevee', 'Normal', 55, 55, 50, 45, 65, 55, 100)
        self.assertEqual(str(poke5), "Pokemon Eevee de tipo Normal con 55 puntos de salud, 55 puntos de ataque, 50 puntos de defensa, 45 puntos de ataque especial, 65 puntos de defensa especial y 55 puntos de velocidad.")