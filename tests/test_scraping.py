import unittest
from src.scraping import validar_url

class TestWebScraper(unittest.TestCase):
    def test_validar_url_correcta(self):
        """Prueba una URL válida"""
        self.assertTrue(validar_url("https://google.com"))

    def test_validar_url_incorrecta(self):
        """Prueba una URL inválida"""
        self.assertFalse(validar_url("not_a_url"))

    def test_asset_classification(self):
        """Prueba de clasificación de activos JS/CSS"""
        pass

if __name__ == '__main__':
    unittest.main()
