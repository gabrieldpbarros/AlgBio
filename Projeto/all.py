import numpy as np

""" Algoritmo de Needleman-Wunsch """
def nedWun(align_mt, DNAseq1, DNAseq2, rows, cols):
    # Penalidades
    GAP = -2
    MISMATCH = -1
    MATCH = 1

    # Insere os gaps iniciais
    last_digit_row = -1 * ((cols - 1) * 2 + 1)
    align_mt[0, 0:] = np.arange(0, last_digit_row, GAP)
    last_digit_col = -1 * ((rows - 1) * 2 + 1)
    align_mt[0:, 0] = np.arange(0, last_digit_col, GAP)

    """ PRIMEIRA ETAPA: Preenchimento da matriz de alinhamento """
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

    """ SEGUNGA ETAPA: Percorre a matriz pela extremidade oposta, retornando o alinhamento ótimo """
    for i in range(rows - 1, 0, -1):
        for j in range(cols - 1, 0, -1):
            a = 0

    print(align_mt) # verificacao

def main():
    DNAseq1 = "ATGCT"
    DNAseq2 = "AGCT"
    cols = len(DNAseq1) + 1
    rows = len(DNAseq2) + 1
    align_mt = np.zeros((rows, cols))
    nedWun(align_mt, DNAseq1, DNAseq2, rows, cols)

if __name__ == "__main__":
    main()