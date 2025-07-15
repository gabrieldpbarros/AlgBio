from typing import Dict

# --- Tabela de Códons Padrão ---
# Esta é uma tabela de códons padrão para a tradução de RNA para aminoácidos.
# 'U' é usado para Uracil, como em RNA.
CODONS_TABLE: Dict[str:str] = {
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

def traduzir_sequencia(sequencia_nucleotideos: str) -> str:
    """
    Realiza a tradução de uma sequência de nucleotídeos (DNA ou RNA)
    para uma sequência de aminoácidos.
    Para simplificar, a tradução ocorre a partir da primeira fase de leitura,
    parando no primeiro códon de parada ou no final da sequência.
    Códons não encontrados são identificados com 'X'.

    Args:
        sequencia_nucleotideos (str): A sequência de nucleotídeos (DNA ou RNA)
                                      a ser traduzida.

    Returns:
        str: A sequência de aminoácidos resultante da tradução.
    """
    proteina = ""
    # Converte T (Timina, DNA) para U (Uracila, RNA) para a tradução
    # já que a tabela de códons é baseada em RNA.
    sequencia_rna = sequencia_nucleotideos.upper().replace('T', 'U')

    i = 0
    while i + 2 < len(sequencia_rna):
        codon = sequencia_rna[i:i+3]
        aminoacido = CODONS_TABLE.get(codon, 'X') # Retorna 'X' se o códon não for encontrado
        if aminoacido == 'STOP':
            break # Para a tradução se um códon de parada for encontrado
        proteina += aminoacido
        i += 3
    return proteina