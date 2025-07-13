# TESTE APENAS PARA VALIDACAO DO ALGORITMO AUTORAL
from Bio import Align

# 1. Defina suas sequências
seq1 = "GAGCCTGGGAGCTCTCTGGCTAGCTGGGGAACCCACTGCTTAAGCCTCAATAAAGCTTGCCTTGAGTGCTTTAAGTAGTGTGTGCCCGTCTGTTATGTGACTCTGGTAACTAGAGATCCCTCAGACCCTTTTAGTCAGTGTGGAAAATCTCTAGCAGTGGCGCCCGAACAGGGACTTGAAGAAAGTAAAACCAGAGGAGATCTCTCGACGCAGGACTCGGCTTGCTGAAGAAGAAGCGCGCGCGGCAAGAGGCGAGGGGCGGCGACTGGTGAGTACGCCTAAAAATTTTGACTAGCGGA"
seq2 = "CAATTTATGAAGGTTATGCTCTTCCCCATGCTATCATTCGTTTAGATTTAGCTGGACGAGATTTAACTGACTACTTAATGAAAATCCTAACTGAACGTGGTTATTCTTTCACCACTACAGCTGAGCGTGAAATTGTTAGAGATATAAAGGAGAAGCTTTGTTATGTAGCCTTAGACTTTGAACAGGAAATGACAACTGCAGCCTCAAGCTCCAGCCTTGAGAAATCTTATGAATTGCCTGATGGTCAAGTCATCACTATTGGTAATGAGCGTTTCCGATGCCCAGAAACACTCTTCCAG"

# 2. Configure as pontuações (score parameters)
# Needleman-Wunsch é um alinhador global
# Match: +1
# Mismatch: -1
# Gap open: -2 (penalidade para abrir um gap)
# Gap extend: -2 (penalidade para estender um gap - para N-W simples, é o mesmo que gap open)

# Crie um objeto Aligner
aligner = Align.PairwiseAligner()

# Defina as pontuações
aligner.match_score = 1
aligner.mismatch_score = -1
aligner.open_gap_score = -2
aligner.extend_gap_score = -2 # Para N-W simples, open_gap_score e extend_gap_score são geralmente os mesmos

try:
    best_bp_alignment = next(aligner.align(seq1, seq2))

    print("\n--- Melhor Alinhamento do Biopython ---")
    # Para imprimir o alinhamento completo, ele pode ser bem longo.
    # Você pode fatiá-lo para visualizar apenas uma parte:
    print(best_bp_alignment)
    print(f"Pontuação do Alinhamento: {best_bp_alignment.score}")

    # Se quiser, pode imprimir apenas as pontuações e uma representação fatiada
    print(f"Seq1 Alinhada (início): {str(best_bp_alignment[0])[:50]}...")
    print(f"Seq2 Alinhada (início): {str(best_bp_alignment[1])[:50]}...")

except StopIteration:
    print("Nenhum alinhamento encontrado (isso não deve acontecer com Needleman-Wunsch).")
except MemoryError:
    print("Ainda enfrentando MemoryError, mesmo ao tentar pegar apenas um alinhamento. As sequências são realmente muito longas para esta máquina ou configuração de Biopython.")