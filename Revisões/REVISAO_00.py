# =================================================================
# EXERCÍCIOS DE REFORÇO: FUNDAMENTOS PARA BIOINFORMÁTICA
# Foca na sintaxe e na lógica simples antes de usar funções 'def'.
# =================================================================

# EXERCÍCIO 1: O Contador de Citocinas (Loops)
# Objetivo: Contar quantas letras 'C' existem na string.
# Regra: Não podes usar .count(), tens de usar um loop 'for'.

''' dna = "ATGCGCCGCT"
contador_c = 0

# Escreve o teu código aqui (Dica: for base in dna:)
for base in dna:
    contador_c = dna.count('C')

print(f"1. Total de Citocinas: {contador_c}") # Resultado esperado: 5 '''


# -----------------------------------------------------------------

# EXERCÍCIO 2: Pesos Moleculares (Dicionários)
# Objetivo: Aceder a valores num dicionário sem deixar o código crashar.

''' pesos = {"A": 71.04, "C": 103.01, "G": 57.02}

# Tenta obter o peso da Alanina ('A') e da Timina ('T')
# Dica: Usa o método .get() para a Timina não dar erro.

peso_a = pesos.get('A')
peso_t = pesos.get('T')

print(f"2. Peso da Alanina: {peso_a}") # Resultado esperado: 71.04
print(f"2. Peso da Timina: {peso_t}")   # Resultado esperado: None ou um aviso
'''

# -----------------------------------------------------------------

# EXERCÍCIO 3: Fatiamento de RNA (Slicing)
# Objetivo: Extrair pedaços específicos de uma sequência.

''' rna_longo = "AUGCCCGGGAAAUUU"

# Extrai o segundo códon (posições de 3 a 6) 
# e o terceiro códon (posições de 6 a 9).

codon_2 = rna_longo[3:6]
codon_3 = rna_longo[6:9]

print(f"3. Segundo códon: {codon_2}") # Resultado esperado: CCC
print(f"3. Terceiro códon: {codon_3}") # Resultado esperado: GGG
'''

# -----------------------------------------------------------------

# EXERCÍCIO 4: Limpeza de Lista (Método .strip)
# Objetivo: Limpar espaços de vários nomes ao mesmo tempo.

''' pacientes = [" Pedro ", "Maria\n", "  João"]
pacientes_limpos = []

# Usa um loop 'for p in pacientes:' e o método .strip()
# para preencher a lista 'pacientes_limpos'.
for p in pacientes:
    pacientes_limpos.append(p.strip())
print(f"4. Lista limpa: {pacientes_limpos}") 
# Resultado esperado: ["Pedro", "Maria", "João"]'''

# ------------------------------------------------------------------

# EXERCÍCIO 5: Comparação de Nucleotídeos (Case Sensitivity)
# Objetivo: Entender que 'A' é diferente de 'a' no Python.
# Regra: Use um 'if' para verificar se as duas bases são IGUAIS.

''' base_lida = "a"
base_referencia = "A"
resultado_comparacao = False'''

# Escreva o seu código aqui. 
# Como você faria para o Python ignorar se é maiúscula ou minúscula?
# Dica: use o método .upper() na base_lida
'''resultado_comparacao = (base_lida.upper() == base_referencia.upper())

print(f"5. As bases são iguais? {resultado_comparacao}") '''


# -----------------------------------------------------------------

# EXERCÍCIO 6: Montando um DNA (Concatenação)
# Objetivo: Criar uma sequência nova a partir de partes soltas.

''' parte1 = "ATG"
parte2 = "CCG"
parte3 = "TAA" '''

# Una as três partes em uma única variável chamada 'dna_completo'
''' dna_completo = parte1 + parte2 + parte3

print(f"6. Sequência completa: {dna_completo}") # Esperado: ATGCCGTAA '''


# -----------------------------------------------------------------

# EXERCÍCIO 7: Verificador de Tamanho (len)
# Objetivo: Validar se uma sequência tem o tamanho mínimo para um códon.

'''sequencia = "ATG" '''

# Verifique se o tamanho (len) da sequencia é igual a 3.
# Se for 3, e_codon deve ser True. Se não, deve ser False.
'''e_codon = (len(sequencia) == 3)'''
'''codon = ''
for codon in sequencia:
    if codon == 3:
        e_codon = True
    elif codon != 3:
        e_codon = False
print(f"7. É um códon completo? {e_codon}") # Esperado: False'''


# -----------------------------------------------------------------

# EXERCÍCIO 8: Substituição Simples (replace)
# Objetivo: Transformar DNA em RNA de forma rápida.

'''dna_original = "ATGC" '''

# Use o método .replace() para trocar todos os 'T' por 'U'
'''rna_gerado = dna_original.replace('T', 'U')

print(f"8. RNA gerado: {rna_gerado}") # Esperado: AUGC'''

# -----------------------------------------------------------------

# EXERCÍCIO 9: Organizando Pacientes (Sort)
# Objetivo: Colocar uma lista de nomes em ordem alfabética.

'''lista_pacientes = ["Zeca", "Ana", "Beto"]'''

# Use o método .sort() para organizar a lista acima.
# Dica: lista_pacientes.sort() não precisa de uma nova variável.

'''lista_pacientes.sort()
print(f"9. Lista em ordem alfabética: {lista_pacientes}")'''
# Esperado: ["Ana", "Beto", "Zeca"]


# -----------------------------------------------------------------

# EXERCÍCIO 10: Cálculo de Porcentagem GC (Matemática)
# Objetivo: Calcular a proporção de bases GC em um fragmento pequeno.

''' total_bases = 10
quantidade_gc = 4'''

# Calcule a porcentagem: (quantidade_gc dividido por total_bases) vezes 100
'''porcentagem_gc = ((quantidade_gc / total_bases)*100)

print(f"10. Conteúdo GC: {porcentagem_gc:.0f}%") # Esperado: 40%'''

# -----------------------------------------------------------------
