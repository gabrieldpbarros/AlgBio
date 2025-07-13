import numpy as np

""" Algoritmo de Needleman-Wunsch """
def nedWun(align_mt: np.ndarray, DNAseq1: str, DNAseq2: str, rows: int, cols: int) -> str:
    # Penalidades e score
    GAP = -2
    MISMATCH = -1
    MATCH = 1
    SCORE = 0

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
    SCORE = align_mt[rows - 1][cols - 1]

    print(SCORE)

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
def smiWat(align_mt: np.ndarray, DNAseq1: str, DNAseq2: str, rows: int, cols: int) -> str:
    # Penalidades
    GAP = -2
    MISMATCH = -1
    MATCH = 1

    """ PRIMEIRA ETAPA: Preenchimento da matriz de alinhamento """
    for i in range(rows - 1):
        for j in range(cols - 1):
            upper_value = align_mt[i, j + 1] + GAP
            if (upper_value < 0):
                upper_value = 0
            side_value = align_mt[i + 1, j] + GAP
            if (side_value < 0):
                side_value = 0
            # Verifica se há match de nucleotídeos
            if (DNAseq1[j] == DNAseq2[i]):
                diagonal_value = align_mt[i, j] + MATCH
            else:
                diagonal_value = align_mt[i, j] + MISMATCH
            if (diagonal_value < 0):
                diagonal_value = 0
            
            # Encontra o maior valor e insere na posição a ser preenchida
            higher = max(upper_value, side_value, diagonal_value)
            align_mt[i + 1, j + 1] = higher
    
    """ SEGUNGA ETAPA: Percorre a matriz pela extremidade oposta, retornando o alinhamento ótimo """
                         

def align(DNAseq1: str, DNAseq2: str):
    cols = len(DNAseq1) + 1
    rows = len(DNAseq2) + 1
    align_mt = np.zeros((rows, cols))
    DNAalign1, DNAalign2 = nedWun(align_mt, DNAseq1, DNAseq2, rows, cols)


    with open("sequence_alignment_TEMP.txt", "w") as al_file:
        al_file.write(f"{DNAalign1}\n{DNAalign2}")

    al_file.close()