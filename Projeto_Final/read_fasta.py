from alinhamento import align
#from Bio import Entrez
from freq_nucleotideos import leitura
from temp_melting import calcular_tm
from tradutor import traduzir_sequencia
from typing import Tuple, List, Dict

import freq_aminoacidos as fa
import os
import time

def processArchives() -> Tuple[Dict[str, str], List[str]]:
    """
    Baixa (se não encontrados no diretório) e processa os arquivos fasta, armazenando em um dicionário com cabeçalho do arquivo como chave e sequência como item.
    Retorna um dicionário segundo essa lógia e uma lista contendo os cabeçalhos (chaves) das sequências.
    """
    #Entrez.email = "beatriz.ormond@unifesp.br"
    dir = "db/fasta_archives"

    chaves = []
    sequencias = {}
    lista_ids = ['AY423387.1', 'AY423388.1', 'AB253429.1', 'AF004456', 'K03455.1']

    for id in lista_ids:
        try:
            # Caso o arquivo já exista no diretório
            cabecalho = ''
            sequencia = ''

            nome_arquivo = os.path.join(dir, id + ".fasta")
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
        except FileNotFoundError:
            # Caso seja necesário baixá-lo
            print(f"Baixando o arquivo relativo ao ID: {id}")
            with Entrez.efetch (db = 'nucleotide', id = id, rettype = 'fasta', retmode = 'text') as handle:
                seq = handle.read()
            time.sleep(1) # Espera 1 seg para outro download (evitar crash)

            nome_arquivo = os.path.join(dir, id + ".fasta")
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
    # for i, j in sequencias.items():
    #     print(f"Cabeçalho = {i}\n", end="")
    #     print(f"Sequência = {j}\n\n")
    
    return sequencias, chaves

def sizes(seq_dict: Dict[str, str]) -> None:
    """ Recebe o dicionário das sequências e cria um arquivo .csv contendo o tamanho de cada sequência """
    # Diretório final dos dados
    dir = "db/analysis"
    nome_arquivo = os.path.join(dir, "sequence_sizes.csv")

    # Títulos
    with open(nome_arquivo, "w") as titles:
        titles.write("ID,Size\n")

    with open(nome_arquivo, "a") as size:
        for header, seq in seq_dict.items():
            tamanho = len(seq)
            size.write(f'"{header}",{tamanho}\n')


def main():
    # Criação dos dicionários no formato Dict[cabeçalho da seq_nucleotideos, seq_nucleotideos]
    seq_dict, chaves = processArchives()
    # Informações que desejamos extrair das sequências
    sizes(seq_dict)
    leitura(seq_dict)
    calcular_tm(seq_dict)
    align(seq_dict, chaves)
    traduzir_sequencia(seq_dict)
    print("------INFORMAÇÕES EXTRAÍDAS------")

if __name__ == "__main__":
    main()