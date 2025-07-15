from typing import Dict, List

import collections
import matplotlib.pyplot as plt
import os


def calcular_frequencia_aminoacidos(sequencia_proteica: str) -> Dict[str, float]:
    """
    Calcula a frequência (em porcentagem) de cada aminoácido em uma
    sequência proteica.

    Args:
        sequencia_proteica (str): A sequência de aminoácidos.

    Returns:
        dict: Um dicionário onde as chaves são os aminoácidos e os valores
              são suas frequências em porcentagem.
    """
    if not sequencia_proteica:
        return {}

    contagem_aminoacidos: Dict[str,int]  = collections.Counter(sequencia_proteica)
    total_aminoacidos: int = len(sequencia_proteica)
    frequencias:Dict[str,float] = {aa: (count / total_aminoacidos) * 100 for aa, count in contagem_aminoacidos.items()}
    return frequencias

def plotar_frequencia_aminoacidos(frequencias:Dict[str, float], titulo:str="Frequência relativa dos aminoácidos de cada sequência") -> None:
    """
    Plota um gráfico de barras mostrando a frequência de aminoácidos.

    Args:
        frequencias (dict): Dicionário com aminoácidos e suas frequências.
        titulo (str): Título do gráfico.
    """
    if not frequencias:
        print(f"Não há dados para plotar para: {titulo}")
        return

    # Ordena os aminoácidos alfabeticamente para consistência no gráfico
    aminoacidos_ordenados: List[str] = sorted(frequencias.keys())
    valores_frequencia: List[float] = [frequencias[aa] for aa in aminoacidos_ordenados]

    fig = plt.figure(figsize=(12, 6))
    plt.bar(aminoacidos_ordenados, valores_frequencia, color='skyblue')
    plt.xlabel("Aminoácido")
    plt.ylabel("Frequência (%)")
    plt.title(titulo)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    output_dir:str = "graficos"
    output_filename: str = os.path.join(output_dir, f"{titulo}.png")
    fig.savefig(output_filename)
    plt.show()