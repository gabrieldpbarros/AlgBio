from typing import Dict

import matplotlib.pyplot as plt
import os
import pandas as pd

def plotar_frequencia_nucleotideos(archive: str) -> None:
    """ Plota um gráfico contendo as frequências de cada nucleotídeo para todas as sequências simultaneamente """
    df = pd.read_csv(archive)
    df['Abbreviated_ID'] = df['ID'].apply(lambda x: x.split()[0])

    # Associação com a intenção de salvar o gráfico em formato .png
    ax = df.set_index('Abbreviated_ID')[['A','C','G','T']].plot(figsize=(10,6), kind='bar')
    fig = ax.figure

    plt.ylabel('Frequência (%)')
    plt.title('Frequência relativa dos nucleotídeos de cada sequência')
    plt.legend(title='Nucleotídeo')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(rotation=45, ha='right', fontsize=8)
    plt.tight_layout()

    output_dir = "graficos"
    output_filename = os.path.join(output_dir, "Frequência relativa dos nucleotídeos de cada sequência.png")
    fig.savefig(output_filename)

def calculo(seq: str) -> Dict[str, float]:
    """ Calcua a frequencia de nucleotideos dos arquivos"""
    A = seq.count('A')
    C = seq.count('C')
    G = seq.count('G')
    T = seq.count('T')
    total = A + T + C + G
    return {    
        'A': A / total * 100 if total else 0,
        'C': C / total * 100 if total else 0,
        'G': G / total * 100 if total else 0,
        'T': T / total * 100 if total else 0,
    }

def salvar_frequencias_csv(header: str, seq: str, nome_saida: str) -> None:
    """ Salva as frequências de todas as sequências em um arquivo .csv """
    with open(nome_saida, 'a') as saida:
        freq = calculo(seq)
        saida.write(f'"{header}",{freq['A']:.2f},{freq['C']:.2f},{freq['G']:.2f},{freq['T']:.2f}\n')
                

def leitura(sequences_dict: Dict[str, int]) -> None:
    db_dir = "db/analysis"
    output_filename = os.path.join(db_dir, 'nuc_frequencies.csv')

    # Cria um arquivo .csv que vai conter todas as frequências
    with open(output_filename, 'w') as saida:
        saida.write('ID,A,C,G,T\n')
    # Importa as frequências para 'frequencies.csv'
    for key, sequence in sequences_dict.items(): 
        salvar_frequencias_csv(key, sequence, output_filename)

    # Plota o gráfico de frequências e salva na pasta 'graficos'
    plotar_frequencia_nucleotideos(output_filename)