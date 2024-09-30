import unittest
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from main import seleccionarNumeroBitllets, seleccionarBitllet, introduirDiners, seleccionarZones, retornarCanvi, \
    calcularPreuTotal, TCASUAL, SENZILL, TJOVE


class TestTicketMachine(unittest.TestCase):

    def test_calcularPreuTotal(self):
        # Probar el cálculo del precio total
        self.assertAlmostEqual(calcularPreuTotal(SENZILL, 1, 1), 2.40)
        self.assertAlmostEqual(calcularPreuTotal(SENZILL, 2, 1), 3.00)  # 2.40 * 1.25
        self.assertAlmostEqual(round(calcularPreuTotal(TCASUAL, 3,2),2), 35.47)  # 11.35 * 1.25^2 * 2

    @patch('builtins.input', side_effect=[5.00, 5.00, 5.00])  # Simulando entradas de monedas
    def test_introduirDiners(self, mock_input):
        # Comprobar que la función retorna el valor correcto
        self.assertEqual(introduirDiners(5.00), 5.00)

    @patch('builtins.input', side_effect=['1'])  # Simulando selección de bitllet
    def test_seleccionarBitllet(self, mock_input):
        self.assertIn(seleccionarBitllet(), range(1, 6))

    @patch('builtins.input', side_effect=['3'])  # Simulando selección de zones
    def test_seleccionarZones(self, mock_input):
        self.assertEqual(seleccionarZones(), 3)

    @patch('builtins.input', side_effect=['2'])  # Simulando selección de bitllets
    def test_seleccionarNumeroBitllets(self, mock_input):
        self.assertEqual(seleccionarNumeroBitllets(), 2)

    @patch('sys.stdout', new_callable=StringIO)  # Para capturar la salida
    def test_retornarCanvi(self, mock_stdout):
        retornarCanvi(10.00, 7.50)
        self.assertIn("Canvi a tornar: 2.50 €", mock_stdout.getvalue())