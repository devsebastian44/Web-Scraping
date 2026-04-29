import unittest
from unittest.mock import patch, MagicMock
from src.scraping import validar_url, obtener_contenido_web


class TestWebScraper(unittest.TestCase):

    def test_validar_url_correcta(self):
        """Prueba de URL válida"""
        self.assertTrue(validar_url("https://google.com"))
        self.assertTrue(validar_url("http://example.org"))

    def test_validar_url_incorrecta(self):
        """Prueba de URL inválida"""
        self.assertFalse(validar_url("not_a_url"))

    @patch("builtins.print")
    @patch("src.scraping.requests.Session.get")
    def test_obtener_contenido_web_exitoso(self, mock_get, mock_print):
        """Prueba de conexión HTTP exitosa simulada"""
        # Configurar el mock
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = b"<html><body><h1>Test</h1></body></html>"
        mock_get.return_value = mock_response

        # Ejecutar función
        response = obtener_contenido_web("https://example.com")

        # Aserciones
        self.assertIsNotNone(response)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Test", response.content)
        mock_get.assert_called_once_with("https://example.com", timeout=10)

    @patch("builtins.print")
    @patch("src.scraping.requests.Session.get")
    def test_obtener_contenido_web_error(self, mock_get, mock_print):
        """Prueba de error HTTP simulado"""
        from requests.exceptions import ConnectionError

        # Configurar el mock para lanzar excepción
        mock_get.side_effect = ConnectionError("Connection refused")

        # Ejecutar función
        response = obtener_contenido_web("https://example.com")

        # Aserciones
        self.assertIsNone(response)


if __name__ == "__main__":
    unittest.main()
