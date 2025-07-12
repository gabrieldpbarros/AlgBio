import time
from typing import Dict
from Bio import Entrez

def processArchives() -> Dict[str, str]:
    """ Baixa e processa os arquivos fasta, armazenando em um dicionário com cabeçalho do arquivo como chave e sequência como item """
    Entrez.email = "beatriz.ormond@unifesp.br"

    sequencias = {}
    lista_ids = ['AY423387.1', 'AY423388.1', 'AB253429.1', 'AF004456', 'K03455.1']

    for id in lista_ids:
        print(f"Processando o ID: {id}")
        with Entrez.efetch (db = 'nucleotide', id = id, rettype = 'fasta', retmode = 'text') as handle:
            seq = handle.read()
        time.sleep(1) # Espera 1 seg para outro download

        nome_arquivo = f"{id}.fasta"
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write(seq)

        cabecalho = ''
        sequencia = ''

        with open(nome_arquivo, 'r') as arquivo:
                linhas = arquivo.readlines()  # Coloca cada linha do arquivo como um elemento em uma lista
                for linha in linhas:
                    linha = linha.strip()
                    if linha.startswith('>'):
                        cabecalho = linha[1:] # Tira o ">"
                    else:
                        sequencia += linha

        sequencias[cabecalho] = sequencia
    # Fim do processamento dos arquivos .fasta
    print("Processamento completo.\n\n")

    # Imprime o dicionário, apenas para visualização
    for i, j in sequencias.items():
        print(f"Cabeçalho = {i}\n", end="")
        print(f"Sequência = {j}\n\n")
    
    return sequencias