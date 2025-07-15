import numpy as np

def save_alginment():
    """ Armazena o alinhamento em um arquivo .csv """

""" Algoritmo de Needleman-Wunsch """
def nedWun(align_mt: np.ndarray, DNAseq1: str, DNAseq2: str, rows: int, cols: int) -> None:
    # Penalidades
    GAP = -2
    MISMATCH = -1
    MATCH = 1

    # Insere os gaps iniciais
    align_mt[0, :] = np.arange(0, cols * GAP, GAP)
    align_mt[:, 0] = np.arange(0, rows * GAP, GAP)

    """ PRIMEIRA ETAPA: Preenchimento da matriz de alinhamento e score"""
    for i in range(rows - 1):
        for j in range(cols - 1):
            upper_value = align_mt[i, j + 1] + GAP
            side_value = align_mt[i + 1, j] + GAP
            # Verifica se há match de nucleotídeos
            if (DNAseq1[j] == DNAseq2[i]):
                diagonal_value = align_mt[i, j] + MATCH
            else:
                diagonal_value = align_mt[i, j] + MISMATCH
            
            # Encontra o maior valor e insere na posição a ser preenchida
            higher = max(upper_value, side_value, diagonal_value)
            align_mt[i + 1, j + 1] = higher

    score = align_mt[rows - 1][cols - 1]
    print(f"Score final para o alinhamento global: {score}")

    """ SEGUNGA ETAPA: Percorre a matriz pela extremidade oposta, retornando o alinhamento ótimo """
    DNAalign1 = ""
    DNAalign2 = ""
    i = rows - 1
    j = cols - 1
    while (i != 0 or j != 0):
        # Caso MATCH
        if (DNAseq1[j - 1] == DNAseq2[i - 1]):
            DNAalign1 = DNAseq1[j - 1] + DNAalign1
            DNAalign2 = DNAseq2[i - 1] + DNAalign2
            i -= 1
            j -= 1

        # Caso MISMATCH
        else:
            # Limite lateral
            if (j == 0):
                DNAalign1 = "-" + DNAalign1
                DNAalign2 = DNAseq2[i - 1] + DNAalign2
                i -= 1

            # Limite superior
            elif (i == 0):
                DNAalign1 = DNAseq1[j - 1] + DNAalign1
                DNAalign2 = "-" + DNAalign2
                j -= 1

            # Dentro dos limites da matriz de alinhamento
            else:
                # Desloca para a esquerda
                if (align_mt[i, j - 1] > align_mt[i - 1, j]):
                    DNAalign1 = DNAseq1[j - 1] + DNAalign1
                    DNAalign2 = "-" + DNAalign2
                    j -= 1

                # Desloca para cima
                elif (align_mt[i, j - 1] < align_mt[i - 1, j]):
                    DNAalign1 = "-" + DNAalign1
                    DNAalign2 = DNAseq2[i - 1] + DNAalign2
                    i -= 1

                # Caso de desempate, desloca na diagonal
                else:
                    DNAalign1 = DNAseq1[j - 1] + DNAalign1
                    DNAalign2 = DNAseq2[i - 1] + DNAalign2
                    i -= 1
                    j -= 1

    return DNAalign1, DNAalign2

""" Algoritmo de Smith-Waterman """
def smiWat(align_mt: np.ndarray, DNAseq1: str, DNAseq2: str, rows: int, cols: int) -> None:
    # Penalidades
    GAP = -2
    MISMATCH = -1
    MATCH = 1

    """ PRIMEIRA ETAPA: Preenchimento da matriz de alinhamento """
    for i in range(rows - 1):
        for j in range(cols - 1):
            upper_value = align_mt[i, j + 1] + GAP
            upper_value = max(0, upper_value)

            side_value = align_mt[i + 1, j] + GAP
            side_value = max(0, side_value)

            # Verifica se há match de nucleotídeos
            if (DNAseq1[j] == DNAseq2[i]):
                diagonal_value = align_mt[i, j] + MATCH
            else:
                diagonal_value = align_mt[i, j] + MISMATCH
            diagonal_value = max(0, diagonal_value)
            
            # Encontra o maior valor e insere na posição a ser preenchida
            higher = max(upper_value, side_value, diagonal_value)
            align_mt[i + 1, j + 1] = higher
    
    score = np.max(align_mt)
    print(f"Score final para o alinhamento local: {score}")
    
    """ SEGUNGA ETAPA: Percorre a matriz pela extremidade oposta, retornando o alinhamento ótimo """
    # Lista que vai conter todos os alinhamentos locais
    local_align = []

    # np.argwhere retorna uma lista de coordenadas (i, j)
    max_positions = np.argwhere(align_mt == score)

    for i, j in max_positions:
        DNAalign1 = ""
        DNAalign2 = ""
        current_i, current_j = i, j
        
        # Bactracking que para em 0
        while align_mt[current_i, current_j] != 0:
            current_score = align_mt[current_i, current_j]

            # Análise de qual direção o algoritmo vai seguir.
            # O uso de max(0, ...) é uma garantia de que temos apenas valores não negativos
            diagonal_prev = align_mt[current_i - 1, current_j - 1]
            if (DNAseq1[j - 1] == DNAseq2[i - 1]):
                diagonal_penal = MATCH
            else:
                diagonal_penal = MISMATCH
            diagonal_value = max(0, diagonal_prev + diagonal_penal)

            upper_prev = align_mt[current_i - 1, current_j]
            upper_value = max(0, upper_prev + GAP)

            side_prev = align_mt[current_i, current_j - 1]
            side_value = max(0, side_prev + GAP)

            # Decisão de caminho
            # MATCH ou MISMATCH
            if current_score == diagonal_value and current_score != 0 and align_mt[current_i - 1, current_j - 1] >= 0: # Para garantir que não veio de um 0 resetado
                DNAalign1 = DNAseq1[j - 1] + DNAalign1
                DNAalign2 = DNAseq2[i - 1] + DNAalign2
                current_i -= 1
                current_j -= 1
            # GAP
            elif current_score == upper_value and current_score != 0 and align_mt[current_i - 1, current_j] >= 0:
                DNAalign1 = "-" + DNAalign1
                DNAalign2 = DNAseq2[i - 1] + DNAalign2
                current_i -= 1
            elif current_score == side_value and current_score != 0 and align_mt[current_i, current_j - 1] >= 0:
                DNAalign1 = DNAseq1[j - 1] + DNAalign1
                DNAalign2 = "-" + DNAalign2
                current_j -= 1
            else:
                break

        local_align.insert(0, (DNAalign1, DNAalign2, score))

    print(local_align)

                
def align(DNAseq1: str, DNAseq2: str):
    cols = len(DNAseq1) + 1
    rows = len(DNAseq2) + 1
    align_mt = np.zeros((rows, cols))
    smiWat(align_mt, DNAseq1, DNAseq2, rows, cols)
    #DNAalign1, DNAalign2 = nedWun(align_mt, DNAseq1, DNAseq2, rows, cols)

    #with open("global_sequence_alignment.txt", "w") as al_file:
    #    al_file.write(f"{DNAalign1}\n{DNAalign2}")

    #DNAalign1, DNAalign2 = smiWat(align_mt, DNAseq1, DNAseq2, rows, cols)
    #with open("local_sequence_alignment.txt", "w") as al_file:
    #    al_file.write(f"{DNAalign1}\n{DNAalign2}")

align("ATT", "GTT")