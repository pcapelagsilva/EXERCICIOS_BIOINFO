from Bio import SeqIO

for registro in SeqIO.parse("exercícios_bioinfo/meu_dna.fasta", "fasta"):
    print(f"ID do gene: {registro.id}")
    print(f"Sequência lida: {registro.seq}")
    print(f"Tamanho: {len(registro.seq)}")

from Bio import SeqIO

caminho = "exercícios_bioinfo/meu_dna.fasta"

for registro in SeqIO.parse(caminho, "fasta"):
    proteina = registro.seq.translate()

    with open ("exercícios_bioinfo/resultado_final.txt", "w") as f:
        f.write(f"ID DO GENE = {registro.id}\n")
        f.write(f"PROTEINA TRADUZIDA: {proteina}")

print("Módulo concluído! o arquivo: resultado_final.txt foi gerado")