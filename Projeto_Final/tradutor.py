from typing import Dict

import freq_aminoacidos as fa
import os

# --- Tabela de Códons Padrão ---
# Esta é uma tabela de códons padrão para a tradução de RNA para aminoácidos.
# 'U' é usado para Uracil, como em RNA.
CODONS_TABLE: Dict[str, str] = {
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L'   , 'UUG': 'L'   ,
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S'   , 'UCG': 'S'   ,
    'UAU': 'Y', 'UAC': 'Y', 'UAA': 'STOP', 'UAG': 'STOP',
    'UGU': 'C', 'UGC': 'C', 'UGA': 'STOP', 'UGG': 'W'   ,
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L'   , 'CUG': 'L'   ,
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P'   , 'CCG': 'P'   ,
    'CAU': 'H', 'CAC': 'H', 'CAA': 'Q'   , 'CAG': 'Q'   ,
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R'   , 'CGG': 'R'   ,
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I'   , 'AUG': 'M'   , # AUG é Metionina e códon de início
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T'   , 'ACG': 'T'   ,
    'AAU': 'N', 'AAC': 'N', 'AAA': 'K'   , 'AAG': 'K'   ,
    'AGU': 'S', 'AGC': 'S', 'AGA': 'R'   , 'AGG': 'R'   ,
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V'   , 'GUG': 'V'   ,
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A'   , 'GCG': 'A'   ,
    'GAU': 'D', 'GAC': 'D', 'GAA': 'E'   , 'GAG': 'E'   ,
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G'   , 'GGG': 'G'
}


## G) Síntese Proteica (Tradução) e Frequência de Aminoácidos

### a. Implementar função de tradução

def transcrever_dna_para_rna(sequencia_dna: str) -> str:
    """
    Transcreve uma sequência de DNA para uma sequência de RNA.
    A -> U
    T -> A
    C -> G
    G -> C
    """
    # Certifique-se de que a sequência está em maiúsculas para o mapeamento
    sequencia_dna_upper = sequencia_dna.upper()

    # Mapeamento correto de DNA para RNA
    # Note que 'T' do DNA vira 'A' no RNA, 'A' do DNA vira 'U' no RNA.
    # Citosina e Guanina se pareiam entre si.
    mapeamento_transcricao = {
        'A': 'U',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }

    rna_bases = []
    for base in sequencia_dna_upper:
        # Se a base não estiver no mapeamento (ex: um caractere inválido),
        # você pode optar por manter, ignorar ou levantar um erro.
        # Aqui, vamos adicionar a base 'X' para indicar um caractere desconhecido.
        rna_bases.append(mapeamento_transcricao.get(base, 'X'))

    return "".join(rna_bases)

def traduzir_sequencia(sequencias: Dict[str, str]) -> None:
    """
    Realiza a tradução de uma sequência de nucleotídeos (DNA ou RNA)
    para uma sequência de aminoácidos.
    Para simplificar, a tradução ocorre a partir da primeira fase de leitura,
    parando no primeiro códon de parada ou no final da sequência.
    Códons não encontrados são identificados com 'X'.

    Args:
        sequencia (Dict[str, str]): Dicionário com todas as sequências de
                                    nucleotídeos (DNA ou RNA) a ser traduzidos.
    """

    # Diretório de armazenamento do .csv
    output_dir = "db/analysis"
    output_file = os.path.join(output_dir, "aa_translation.csv")

    # Escrita dos títulos do .csv
    with open(output_file, "w") as titles:
        titles.write("ID,Amino acid\n")

    # Algoritmo principal de tradução
    for key, sequencia_nucleotideos in sequencias.items():
        proteina = ""
        
        sequencia_rna = transcrever_dna_para_rna(sequencia_nucleotideos)

        i = 0
        while i + 2 < len(sequencia_rna):
            codon = sequencia_rna[i:i+3]
            aminoacido = CODONS_TABLE.get(codon, 'X') # Retorna 'X' se o códon não for encontrado
            if aminoacido == 'STOP':
                break # Para a tradução se um códon de parada for encontrado
            proteina += aminoacido
            i += 3

        # Calcula as frequências, insere no dicionário de frequências e plota as frequências relativas
        frequencias = fa.calcular_frequencia_aminoacidos(proteina)
        fa.plotar_frequencia_aminoacidos(frequencias, key)

        # Insere o aminoácido traduzido no .csv
        with open(output_file, "a") as aa:
            aa.write(f'"{key}",{proteina}\n')