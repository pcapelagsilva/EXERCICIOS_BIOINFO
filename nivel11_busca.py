from Bio import SeqIO

caminho = "exercícios_bioinfo/meu_dna_nivel11.fasta"

for registro in SeqIO.parse(caminho, "fasta"):
    dna = str(registro.seq)
    print(f'A fita de DNA é composta por {dna}')
    iniciacao = dna.find("ATG")
    if iniciacao != -1:
        print(f"Códon de Start encontrado na posição: {iniciacao}")

        gene_ativo = dna[iniciacao:]

        proteina = registro.seq[iniciacao:].translate(to_stop=True)

        arquivo_saida = "exercícios_bioinfo/gene_ativo_resultado_nivel11.txt"
        with open (arquivo_saida, "w") as f_saida:
            f_saida.write(f"ID: {registro.id}\n")
            f_saida.write(f"Posição de início: {iniciacao}\n")
            f_saida.write(f"Sequencia ativa (DNA): {gene_ativo}\n")
            f_saida.write(f"Proteina traduzida: {proteina}\n")

        print(f"Resultado salvo com sucesso em: {arquivo_saida}")
    else:
        print(f"ALERTA: Nenhum códon de start (ATG) foi encontrado na sequencia.")

print("\n--- ESTUDO FINALIZADO ---")