import unittest
from atualizacao_contramedidas.atualizar_contramedidas import atualizar_contramedidas

class TestAtualizarContramedidas(unittest.TestCase):
    
    def test_atualizar_contramedidas(self):
        resultado = atualizar_contramedidas()
        self.assertTrue("Dados atualizados com sucesso." in resultado or "Erro ao atualizar dados." in resultado)

if __name__ == '__main__':
    unittest.main()
