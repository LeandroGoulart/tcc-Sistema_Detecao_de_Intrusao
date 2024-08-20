import unittest
import logging
from ai_model import detectar_anomalias  # Supondo que a função esteja definida em ai_model.py

class TestDeteccaoAnomalias(unittest.TestCase):
    def test_dados_validos(self):
        dados = [
            {"feature1": 1.0, "feature2": 2.0},
            {"feature1": 1.1, "feature2": 2.1},
            {"feature1": 0.9, "feature2": 1.9}
        ]
        params = {"n_estimators": 100, "contamination": 0.1}
        anomalias = detectar_anomalias(dados, params)
        self.assertEqual(len(anomalias), len(dados))

    def test_dados_invalidos(self):
        dados = [
            {"feature1": 1.0, "feature2": 2.0},
            {"feature1": 1.1},  # Item com número diferente de características
        ]
        params = {"n_estimators": 100, "contamination": 0.1}
        with self.assertRaises(ValueError):
            detectar_anomalias(dados, params)

if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR)
    unittest.main()