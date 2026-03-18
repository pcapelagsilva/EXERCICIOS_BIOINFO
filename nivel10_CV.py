from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

caminho_1 = "exercícios_bioinfo/paciente_A_nivel10.fasta"
caminho_2 = "exercícios_bioinfo/paciente_B_nivel10.fasta"

for registro_1 in SeqIO.parse(caminho_1, "fasta"):
    dna_1 = registro_1.seq
    gc_1 = gc_fraction(dna_1)*100

for registro_2 in SeqIO.parse(caminho_2, "fasta"):
    dna_2 = registro_2.seq
    gc_2 = gc_fraction(dna_2)*100

if dna_1 == dna_2:
    print("As sequencias são completamente iguais!!")
else:
    print("As sequencias são DIFERENTES!!!")

    print(f"O conteúdo GC do paciente A é igual a {gc_1:.2f}%")
    print(f"O conteúdo GC do paciente B é igual a {gc_2:.2f}%")

# EXTRA!!! POSIÇÃO ONDE OS AMINOÁCIDOS SÃO DISTINTOS:
mutacoes = [] #Criamos uma lista para guardar onde estão as diferenças


for i, (base_a, base_b) in enumerate(zip(dna_1, dna_2)): #'zip()' junta as duas sequências para compará-las
    if base_a != base_b:
        mutacoes.append(f"Posição {i+1}: Paciente A tinha '{base_a}' e Paciente B tinha '{base_b}'.") #Guardamos a posição (i+1 para humanos entenderem, começando do 1) e as bases que mudaram

if len(mutacoes) > 0: #Exibindo os resultados
    print(f"\n Foram encontradas {len(mutacoes)} mutações:")
    for m in mutacoes:
        print(m)
else:
    print("\n Nenhuma mutação foi encontrada.")