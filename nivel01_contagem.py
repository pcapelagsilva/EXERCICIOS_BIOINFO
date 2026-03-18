sequencia = "ACTGCTAGCTAGCGATCG"
tamanho = len(sequencia)
qtd_a = sequencia.count("A")
qtd_g = sequencia.count("G")
soma_purinas = qtd_a + qtd_g

print(f"Comprimento: {tamanho} | A: {qtd_a} | G: {qtd_g} | Soma A+G: {soma_purinas}")