import time
from typing import Tuple, List, Dict
from Bio import Entrez
from align import align

def processArchives() -> Tuple[Dict[str, str], List[str]]:
    """
    Baixa e processa os arquivos fasta, armazenando em um dicionário com cabeçalho do arquivo como chave e sequência como item.
    Retorna um dicionário segundo essa lógia e uma lista contendo os cabeçalhos (chaves) das sequências.
    """
    Entrez.email = "beatriz.ormond@unifesp.br"

    chaves = []
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
        chaves.append(cabecalho)
    # Fim do processamento dos arquivos .fasta
    print("Processamento completo.\n\n")

    # Imprime o dicionário, apenas para visualização
    for i, j in sequencias.items():
        print(f"Cabeçalho = {i}\n", end="")
        print(f"Sequência = {j}\n\n")
    
    return sequencias, chaves

def sizes(seq_dict: Dict[str, str]) -> Dict[str, int]:
    """ Recebe o dicionário das sequências e retorna o um dicionário contendo o tamanho de cada sequência """
    tamanho = {}
    for i,j in seq_dict.items():
        tamanho[i] = len(j)
        print(f"Sequência {i}: {tamanho[i]}")

    return tamanho

def main():
    seq_dict, chaves = processArchives()
    size_dict = sizes(seq_dict)

    align(seq_dict[chaves[0]][:300], seq_dict[chaves[1]][:300])

if __name__ == "__main__":
    main()