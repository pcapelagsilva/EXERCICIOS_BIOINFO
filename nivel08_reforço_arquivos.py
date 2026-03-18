# 1. AS FERRAMENTAS - Puxando o necessário para o estudo:
import os
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

# Isto mostra para onde o Python está "olhando":
print(f"Eu estou trabalhando na pasta: {os.getcwd()}.")

# 2. O CAMINHO - Onde o Python deve ir buscar o arquivo:
caminho = "exercícios_bioinfo/meu_dna.fasta"

# 3. O PROCESSO - Lendo o arquivo:
for registro in SeqIO.parse(caminho, 'fasta'):
    # A) ENCONTRAR E CORTAR - Separando o trecho escolhido da sequência:
    trecho = registro.seq[0:90]
    # B) TRABALHANDO - Calculando a porcentagem de Guaninas e Citosinas na sequência:
    gc = gc_fraction(trecho) * 100
    # C) TRABALHANDO - Calculando a proteína do trecho:
    proteina = trecho.translate()

    print(f'recorte = {trecho}; Calculo de GC = {gc:.2f}% e proteína = {proteina}')

# 4. ENVIAR - Criando o arquivo de saída:
# 'with open' cria o arquivo, 'w' de 'write' (escrever)
    with open("exercícios_bioinfo/relatorio_insulina.txt", "w") as f_saida:
        f_saida.write("--- REALTORIO BIOINFO ---\n")
        f_saida.write(f'ID do gene: {registro.id}\n')
        f_saida.write(f'Conteúdo GC: {gc:.2f}%\n')
        f_saida.write(f'Proteína: {proteina}\n')
        f_saida.write(f'-------------------------\n')
# 5. AVISO FINAL:
print("Processo concluído! Verifique o arquivo em 'relatorio_insulina.txt'.")