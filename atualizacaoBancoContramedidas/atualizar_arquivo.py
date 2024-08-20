def atualizar_informacoes(versao_file, data_file, output_file):
    try:
        # Ler o conteúdo do arquivo versao.txt
        with open(versao_file, 'r') as vf:
            versao = vf.read().strip()

        # Ler o conteúdo do arquivo versao_data.txt
        with open(data_file, 'r') as df:
            data = df.read().strip()

        # Combinar as informações
        conteudo_combinado = f"Versão: {versao}\nData da Atualização: {data}"

        # Gravar as informações combinadas no arquivo versao_completa.txt
        with open(output_file, 'w') as of:
            of.write(conteudo_combinado)

        print(f"Arquivo {output_file} criado com sucesso!")

    except Exception as e:
        print(f"Erro ao combinar arquivos: {e}")