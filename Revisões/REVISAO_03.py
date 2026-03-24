# =================================================================
# LISTA DE EXERCÍCIOS: DO BÁSICO AO AVANÇADO (BIOINFORMÁTICA)
# =================================================================

# -----------------------------------------------------------------
# NÍVEL 1: AQUECIMENTO (LÓGICA E STRINGS)
# -----------------------------------------------------------------

# EXERCÍCIO 1: CALCULADORA DE COMPRIMENTO DE ÉXONS
# TAREFA: Peça ao usuário duas sequências (Exon 1 e Exon 2).
# Calcule o comprimento total do gene formado pela junção deles e 
# exiba qual dos dois éxons é o maior.

'''exon_1 = input("Digite o seu primeiro Exon: ").strip().upper().replace(" ", "")
exon_2 = input("Digite o seu segundo Exon: ").strip().upper().replace(" ", "")

seq = exon_1+exon_2
comprimento = len(seq)

maior = ""
if len(exon_1) > len(exon_2):
    maior = exon_1
elif len(exon_2) > len(exon_1):
    maior = exon_2
elif len(exon_1) == len(exon_2):
    maior = "Ambos os exons possuem o mesmo tamanho"

print(f"O comprimento total da sequência é de {comprimento}db, sendo o maior entre eles o exon: {maior}")'''

# -----------------------------------------------------------------

# EXERCÍCIO 2: BUSCA DE MOTIVOS (PADRÕES)
# TAREFA: Crie um programa que verifique se a sequência "TATA" (TATA Box) está presente em uma sequência de DNA fornecida. 
# Se estiver, diga em qual posição ela começa (use o método .find()).

'''seq = input("Digite a sequência: ").strip().upper().replace(" ", "")

verif_seq = seq.find("TATA")
if verif_seq != -1:
    print(f"A sequência possui uma box TATA, e ela se inicia na posição {verif_seq}")
else:
    print("A sequência não possui uma box TATA")'''

# -----------------------------------------------------------------
# NÍVEL 2: INTERMEDIÁRIO (LISTAS E DICIONÁRIOS)
# -----------------------------------------------------------------

# EXERCÍCIO 3: TRADUTOR MANUAL COM DICIONÁRIO
# TAREFA: Crie um dicionário chamado 'tabela_genetica' onde as chaves são 3 códons (ex: "ATG", "GAA", "TGT") e os valores são seus 
# aminoácidos. Peça um códon ao usuário e retorne o aminoácido.

'''tabela_genetica = {
    # T
    'TTT': 'Fenilalanina', 'TTC': 'Fenilalanina', 'TTA': 'Leucina', 'TTG': 'Leucina',
    'TCT': 'Serina', 'TCC': 'Serina', 'TCA': 'Serina', 'TCG': 'Serina',
    'TAT': 'Tirosina', 'TAC': 'Tirosina', 'TAA': 'STOP', 'TAG': 'STOP',
    'TGT': 'Cisteína', 'TGC': 'Cisteína', 'TGA': 'STOP', 'TGG': 'Triptofano',
    
    # C
    'CTT': 'Leucina', 'CTC': 'Leucina', 'CTA': 'Leucina', 'CTG': 'Leucina',
    'CCT': 'Prolina', 'CCC': 'Prolina', 'CCA': 'Prolina', 'CCG': 'Prolina',
    'CAT': 'Histidina', 'CAC': 'Histidina', 'CAA': 'Glutamina', 'CAG': 'Glutamina',
    'CGT': 'Arginina', 'CGC': 'Arginina', 'CGA': 'Arginina', 'CGG': 'Arginina',
    
    # A
    'ATT': 'Isoleucina', 'ATC': 'Isoleucina', 'ATA': 'Isoleucina', 'ATG': 'Metionina (START)',
    'ACT': 'Treonina', 'ACC': 'Treonina', 'ACA': 'Treonina', 'ACG': 'Treonina',
    'AAT': 'Asparagina', 'AAC': 'Asparagina', 'AAA': 'Lisina', 'AAG': 'Lisina',
    'AGT': 'Serina', 'AGC': 'Serina', 'AGA': 'Arginina', 'AGG': 'Arginina',
    
    # G
    'GTT': 'Valina', 'GTC': 'Valina', 'GTA': 'Valina', 'GTG': 'Valina',
    'GCT': 'Alanina', 'GCC': 'Alanina', 'GCA': 'Alanina', 'GCG': 'Alanina',
    'GAT': 'Ácido Aspártico', 'GAC': 'Ácido Aspártico', 'GAA': 'Ácido Glutâmico', 'GAG': 'Ácido Glutâmico',
    'GGT': 'Glicina', 'GGC': 'Glicina', 'GGA': 'Glicina', 'GGG': 'Glicina'
}

codon = input("Digite um Códon (ex: ATG): ").strip().upper().replace(" ", "")

resultado = tabela_genetica.get(codon, "Códon não encontrado na tabela")

print(f"O aminoácido correspondente ao códon {codon} é: {resultado}")

# EXERCÍCIO 4: FILTRO DE SEQUÊNCIAS POR TAMANHO
# TAREFA: Dada uma lista de sequências: ["ATG", "ATGCGT", "AT", "GGCAT"]
# Use um loop 'for' para criar uma nova lista contendo apenas as 
# sequências que tenham MAIS de 3 caracteres.'''

# -----------------------------------------------------------------
# NÍVEL 3: AVANÇADO (ESTATÍSTICA E ARQUIVOS)
# -----------------------------------------------------------------

# EXERCÍCIO 5: FREQUÊNCIA RELATIVA DE BASES
# TAREFA: Peça uma sequência. Calcule a porcentagem de cada base (A, T, C, G)
# em relação ao total. 
# Ex: "A" aparece 2 vezes em 10 bases = 20%. 
# Exiba os resultados formatados com duas casas decimais.
'''def cal_porcentagem(seq, base):
    contagem = seq.count(base)
    total_bases = len(seq)

    if total_bases == 0:
        return 0
    
    resultado = (contagem/total_bases)*100
    return resultado

seq = input("Digite uma sequência: ").strip().upper().replace(" ", "")
lista_bases = ['A', 'T', 'C', 'G']
print(f"Sequência analisada: {seq}\n")

for b in lista_bases:
    porcentagem = cal_porcentagem(seq, b)
    print(f"Base = {b} --> Porcentagem = {porcentagem:.2f}%")'''

# EXERCÍCIO 6: SIMULADOR DE BANCO DE DADOS (DICIONÁRIO DE LISTAS)
# TAREFA: Crie um dicionário onde a CHAVE é o nome do paciente e o VALOR é a sequência de DNA dele. 
# 1. Adicione 3 pacientes.
# 2. Peça ao usuário o nome de um paciente.
# 3. Se o nome existir, mostre a sequência e o Conteúdo GC dele.

'''def calcular_porcentagem(seq, base):
    if len(seq) == 0:
        return 0
    return (seq.count(base)/len(seq))*100

pacientes = {'Gabriel':'ATGTG', 'Lúcio':'GTCGGATCG', 'Rafinha':'AGGCTAGAGC', 'Virginia':'GGCTAGCTA', 'Pablo':'AGCTGGCTAGAC', 'Cazé':'GGCTAGCAAGCT'}

print("--- SISTEMA DE BUSCA DE PACIENTES ---")
nome = input("Digite o nome do paciente que você deseja conferir os resultados: ").strip().capitalize()
print("-------------------------------------")

if nome in pacientes:
    dna_encontrado = pacientes[nome]
    print(f"\nPaciente {nome} encontrado!!")
    print(f"Sequência igual a: {dna_encontrado}")

    g = calcular_porcentagem(dna_encontrado, "G")
    c = calcular_porcentagem(dna_encontrado, "C")
    gc_total = g + c

    print(f"Conteúdo GC Total: {gc_total:.2f}%")
else:
    print(f"⚠️ERRO⚠️\n O paciente {nome} não consta no sistema")'''

# -----------------------------------------------------------------
# NÍVEL MASTER: DESAFIO FINAL (AUTOMAÇÃO)
# -----------------------------------------------------------------

# EXERCÍCIO 7: LOG DE ERROS AUTOMATIZADO
# TAREFA: Crie um programa que percorra uma lista de sequências. 
# Se a sequência tiver algum caractere que NÃO seja A, T, C ou G, salve essa sequência em uma lista chamada 'erros'. 
# No final, imprima: "Processamento concluído. X sequências com erro detectadas."

'''def validar_sequencia(dna):
    bases_validas = "ATCG"
    for letra in dna:
        if letra not in bases_validas:
            return False
    return True

amostras = []
print("--- CADASTRO DE AMOSTRAS ---")
print("(Digite 'fim' para encerrar o cadastro)")

while True:
    seq = input("Digite a sequência da amostra: ").strip().upper().replace(" ", "")

    if seq == 'FIM':
        break
    amostras.append(seq)

amostras_validas = []
amostras_invalidas = []

for dna in amostras:
    if validar_sequencia(dna):
        amostras_validas.append(dna)
    else:
        amostras_invalidas.append(dna)

print("-=" * 40)
print("📊 RELATÓRIO DE CONTROLE DE QUALIDADE")
print("-=" * 40)
print(f"Foram cadastradas o total de {len(amostras)} amostras")
print(f"Delas {len(amostras_validas)} são válidas✅ e {len(amostras_invalidas)} inválidas ❌...")

if amostras_invalidas:
    print("\n⚠️ Verifique as amostras corrompidas:")
    for erro in amostras_invalidas:
        print(f"- {erro}")

print("\nProcessamento concluído.")'''