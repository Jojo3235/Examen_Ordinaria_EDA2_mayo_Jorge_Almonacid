import unittest
from datetime import datetime
from Pokeball import Pokeball

class TestPokeball(unittest.TestCase):
    def setUp(self):
        self.pokeball1 = Pokeball(100, "Pokeball normal", 200, datetime(2021, 8, 1))
        self.pokeball2 = Pokeball(150, "Pokeball de lujo", 500, datetime(2021, 7, 15))
        self.pokeball3 = Pokeball(80, "Pokeball de entrenamiento", 100, datetime(2021, 8, 10))

    def test_ordenar_pokeballs_por_fecha(self):
        pokeballs = [self.pokeball1, self.pokeball2, self.pokeball3]
        pokeballs_ordenadas = sorted(pokeballs, key=lambda x: x.fecha_fabricacion)
        self.assertEqual(pokeballs_ordenadas, [self.pokeball2, self.pokeball1, self.pokeball3])

    def test_modificar_precio_pokeball(self):
        self.pokeball2.precio = 600
        self.assertEqual(self.pokeball2.precio, 600)

if __name__ == '__main__':
    unittest.main()