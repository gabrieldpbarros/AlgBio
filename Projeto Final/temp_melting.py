from typing import Dict

import os

def salvar_tm_csv(header: str, tm: float, archive: str) -> None:
    """ Armazena cada temperatura de melting em um arquivo .csv """
    with open(archive, "a") as row:
        row.write(f'"{header}",{tm}\n')

def calcular_tm(sequencias: Dict[str, str]) -> float:
    """ Calcula a temperatura de melting com base na sequência fornecida """
    # Diretório final dos dados
    dir = "db/analysis"
    output_file = os.path.join(dir, "temp_melting.csv")
    
    with open(output_file, "w") as tm_table:
        # Titulos
        tm_table.write("ID,Tm (Degree Celsius)\n")

    for key, seq in sequencias.items():
        # Essencial para calcular o conteúdo GC
        num_g = seq.count('G')
        num_c = seq.count('C')

        comprimento_sequencia = len(seq)

        # Caso de tamanho nulo
        if comprimento_sequencia == 0:
            salvar_tm_csv(key, 0.0, output_file)
            continue

        # Cálculo normal da temperatura de melting (Tm)
        Tm = 64.9 + 41 * ((num_g + num_c - 16.4) / comprimento_sequencia)
        salvar_tm_csv(key, Tm, output_file)