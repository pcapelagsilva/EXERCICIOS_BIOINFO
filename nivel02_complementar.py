dna = "ATGC"
# Técnica de trocar por minúsculas para não confundir o Python
temp = dna.replace("A", "t").replace("T", "a").replace("C", "g").replace("G", "c")
complementar = temp.upper()
print(f"Original: {dna} -> Complementar: {complementar}")