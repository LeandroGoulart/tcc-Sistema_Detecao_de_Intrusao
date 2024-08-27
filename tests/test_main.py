import unittest
from main import main

class TestMain(unittest.TestCase):
    
    def test_main(self):
        try:
            main()  # Executa o script principal
            self.assertTrue(True)  # Se não lançar exceção, o teste passa
        except Exception as e:
            self.fail(f"Erro ao executar o main: {e}")

if __name__ == '__main__':
    unittest.main()
