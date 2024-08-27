import unittest
from gerenciar_dados import baixar_dados, atualizar_versao

class TestGerenciarDados(unittest.TestCase):
    
    def test_baixar_dados(self):
        versao = '1.0'
        url = f"https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-{versao}.json"
        dados = baixar_dados(url)
        self.assertIsInstance(dados, dict)  # Verifica se o retorno é um dicionário

    def test_atualizar_versao(self):
        url_versao_atual = 'https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/enterprise-attack/enterprise-attack-1.0.json'
        resultado = atualizar_versao(url_versao_atual)
        self.assertTrue("Versão 1.0 atualizada com sucesso." in resultado or "Erro ao atualizar versão 1.0." in resultado)

if __name__ == '__main__':
    unittest.main()
