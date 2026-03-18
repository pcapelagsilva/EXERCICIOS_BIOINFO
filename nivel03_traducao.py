from Bio.Seq import Seq
meu_dna = Seq("ATGCGCTAGCTC")
proteina = meu_dna.translate()
print(f"DNA: {meu_dna} -> Proteína: {proteina}")
# Lembre-se: o '*' é o Stop Códon!