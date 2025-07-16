from typing import Dict, List

import csv
import numpy as np
import os

def save_alginment_score(path_name: str, score_map: np.ndarray, headers: List[str]) -> None:
    """ Armazena o score do alinhamento no um arquivo .csv """
    # Cria os títulos para o .csv que contém os scores dos alinhamentos globais e insere os valores após
    with open(path_name, "w", newline='') as align_file:
        writer = csv.writer(align_file)

        # Escreve a linha de títulos (nomes das colunas).
        # A formatação de headers impede que as vírgulas nos cabeçalhos sejam inclusas como vírgulas do .csv
        writer.writerow(['ID'] + headers)

        # Escreve as linhas de dados
        for i in range(5):
            # Cada linha começa com o nome da sequência correspondente
            row_to_write = [headers[i]] + score_map[i, :].tolist()
            writer.writerow(row_to_write)

""" Algoritmo de Needleman-Wunsch """
def nedWun(align_mt: np.ndarray, DNAseq1: str, DNAseq2: str, rows: int, cols: int) -> np.number:
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

    return score

""" Algoritmo de Smith-Waterman """
def smiWat(align_mt: np.ndarray, DNAseq1: str, DNAseq2: str, rows: int, cols: int) -> np.number:
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

    return score

                
def align(seq_dict: Dict[str, str], headers: List[str]) -> None:
    # Caminho para o diretório final
    dir_name = "db/analysis"
    output_global_file = os.path.join(dir_name, "global_alignment.csv")
    output_local_file = os.path.join(dir_name, "local_alignment.csv")

    # Matrizes de score
    global_scores = np.zeros((5,5))
    local_scores = np.zeros((5,5))

    for i in range(5):
        for j in range(5):
            if (i == j):
                global_scores[i, j] = 0
                local_scores[i, j] = 0
            else:
                # Seleciona apenas os 300 primeiros nucleotídeos
                DNAseq1 = seq_dict[headers[i]][:300]
                DNAseq2 = seq_dict[headers[j]][:300]
                cols = len(DNAseq1) + 1
                rows = len(DNAseq2) + 1
                # Matrizes de alinhamento
                global_align_mt = np.zeros((rows, cols))
                local_align_mt = np.zeros((rows, cols))
                # Calcula os alinhamentos e scores
                global_scores[i, j] = nedWun(global_align_mt, DNAseq1, DNAseq2, rows, cols)
                local_scores[i, j] = smiWat(local_align_mt, DNAseq1, DNAseq2, rows, cols)

    # Insere os valores nos respectivos .csv
    save_alginment_score(output_global_file, global_scores, headers)
    save_alginment_score(output_local_file, local_scores, headers)