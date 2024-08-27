import unittest
from ai_model import bot_protecao, salvar_programas_comuns, buscar_contramedida

class TestAiModel(unittest.TestCase):
    
    def test_buscar_contramedida(self):
        resultado = buscar_contramedida("programa_suspeito")
        self.assertIsInstance(resultado, str)  # Verifica se o resultado é uma string
    
    def test_salvar_programas_comuns(self):
        programas = {1234: "programa_exemplo"}
        try:
            salvar_programas_comuns(programas)
            self.assertTrue(True)  # Se não lançar exceção, o teste passa
        except Exception as e:
            self.fail(f"Erro ao salvar programas comuns: {e}")

if __name__ == '__main__':
    unittest.main()
