from Bio import SeqIO

caminho = "exercícios_bioinfo/meu_dna_nivel09.fasta"

for registro in SeqIO.parse(caminho, "fasta"):
    trecho = registro.seq[5:-5]
    print(f'O trecho pedido é {trecho}')
    with open ("exercícios_bioinfo/dna_limpo_nivel09.txt", "w") as f_saida:
        f_saida.write("--- DNA RECORTADO ---\n")
        f_saida.write(f"ID do gene: {registro.id}\n")
        f_saida.write(f"DNA original: {registro.seq}\n")
        f_saida.write(f"Trecho do DNA requisitado: {trecho}\n")

    print('PROCESSO CONCLUÍDO... CONFIRA NO ARQUIVO: dna_limpo_nivel09.txt')