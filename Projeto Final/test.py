# TESTE APENAS PARA VALIDACAO DO ALGORITMO AUTORAL
from Bio import Align

# 1. Defina suas sequências
# seq1 = "GAGCCTGGGAGCTCTCTGGCTAGCTGGGGAACCCACTGCTTAAGCCTCAATAAAGCTTGCCTTGAGTGCTTTAAGTAGTGTGTGCCCGTCTGTTATGTGACTCTGGTAACTAGAGATCCCTCAGACCCTTTTAGTCAGTGTGGAAAATCTCTAGCAGTGGCGCCCGAACAGGGACTTGAAGAAAGTAAAACCAGAGGAGATCTCTCGACGCAGGACTCGGCTTGCTGAAGAAGAAGCGCGCGCGGCAAGAGGCGAGGGGCGGCGACTGGTGAGTACGCCTAAAAATTTTGACTAGCGGA"
# seq2 = "CAATTTATGAAGGTTATGCTCTTCCCCATGCTATCATTCGTTTAGATTTAGCTGGACGAGATTTAACTGACTACTTAATGAAAATCCTAACTGAACGTGGTTATTCTTTCACCACTACAGCTGAGCGTGAAATTGTTAGAGATATAAAGGAGAAGCTTTGTTATGTAGCCTTAGACTTTGAACAGGAAATGACAACTGCAGCCTCAAGCTCCAGCCTTGAGAAATCTTATGAATTGCCTGATGGTCAAGTCATCACTATTGGTAATGAGCGTTTCCGATGCCCAGAAACACTCTTCCAG"

# # 2. Configure as pontuações (score parameters)
# # Needleman-Wunsch é um alinhador global
# # Match: +1
# # Mismatch: -1
# # Gap open: -2 (penalidade para abrir um gap)
# # Gap extend: -2 (penalidade para estender um gap - para N-W simples, é o mesmo que gap open)
# 
# # Crie um objeto Aligner
# aligner = Align.PairwiseAligner()
# 
# # Defina as pontuações
# aligner.match_score = 1
# aligner.mismatch_score = -1
# aligner.open_gap_score = -2
# aligner.extend_gap_score = -2 # Para N-W simples, open_gap_score e extend_gap_score são geralmente os mesmos
# 
# try:
#     best_bp_alignment = next(aligner.align(seq1, seq2))
# 
#     print("\n--- Melhor Alinhamento do Biopython ---")
#     # Para imprimir o alinhamento completo, ele pode ser bem longo.
#     # Você pode fatiá-lo para visualizar apenas uma parte:
#     print(best_bp_alignment)
#     print(f"Pontuação do Alinhamento: {best_bp_alignment.score}")
# 
#     # Se quiser, pode imprimir apenas as pontuações e uma representação fatiada
#     print(f"Seq1 Alinhada (início): {str(best_bp_alignment[0])[:50]}...")
#     print(f"Seq2 Alinhada (início): {str(best_bp_alignment[1])[:50]}...")
# 
# except StopIteration:
#     print("Nenhum alinhamento encontrado (isso não deve acontecer com Needleman-Wunsch).")
# except MemoryError:
#     print("Ainda enfrentando MemoryError, mesmo ao tentar pegar apenas um alinhamento. As sequências são realmente muito longas para esta máquina ou configuração de Biopython.")

# Sequências fornecidas
seq1 = "CTAGTGACCACCATGTGCCTGCTCGCCAATGTGACGTTCCCATGTGCCCAACCACCAATTTGCTACGACA"
seq2 = "GAGCCTGGGAGCTCTCTGGCTAGCTGGGGAACCCACTGCTTAAGCCTCAATAAAGCTTGCCTTGAGTGCT"

# Configuração do alinhador para Smith-Waterman (alinhamento local)
aligner = Align.PairwiseAligner()

# Definindo as pontuações
aligner.match_score = 2
aligner.mismatch_score = -1
aligner.open_gap_score = -1   # Penalidade para abrir um gap
aligner.extend_gap_score = -1 # Penalidade para estender um gap

# Definindo o modo de alinhamento como local (Smith-Waterman)
aligner.mode = 'local'

# Executa o alinhamento
# O .align() retorna um iterador de objetos Alignment
alignments = aligner.align(seq1, seq2)

# Pega o primeiro (e melhor) alinhamento encontrado
try:
    best_local_alignment = next(alignments)

    print("--- Melhor Alinhamento Local Encontrado ---")
    print(best_local_alignment)
    print(f"Pontuação do Alinhamento Local: {best_local_alignment.score}")

    print("\n--- Detalhes do Alinhamento ---")
    # --- CORREÇÃO AQUI: Acessando sequências alinhadas por índice ---
    print(f"Sub-sequência 1 alinhada (da SEQ1): {str(best_local_alignment[0])}")
    print(f"Sub-sequência 2 alinhada (da SEQ2): {str(best_local_alignment[1])}")

    # Os atributos de início/fim ('query_start', 'query_end', 'target_start', 'target_end')
    # são mais estáveis entre as versões, mas se der erro, você pode ter que parser
    # a representação em string do alinhamento para extraí-los.
    print(f"Início do alinhamento na SEQ1 (índice 0-based): {best_local_alignment.query_start}")
    print(f"Fim do alinhamento na SEQ1 (índice 0-based, exclusivo): {best_local_alignment.query_end}")
    print(f"Início do alinhamento na SEQ2 (índice 0-based): {best_local_alignment.target_start}")
    print(f"Fim do alinhamento na SEQ2 (índice 0-based, exclusivo): {best_local_alignment.target_end}")

except StopIteration:
    print("Nenhum alinhamento encontrado (isso não deve acontecer com o Smith-Waterman se houver alguma similaridade).")
except AttributeError as e:
    print(f"Erro de atributo: {e}. Sua versão do Biopython pode ser muito antiga para alguns atributos.")
    print("Por favor, considere atualizar o Biopython (`pip install --upgrade biopython`) ou adapte o código para sua versão.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")