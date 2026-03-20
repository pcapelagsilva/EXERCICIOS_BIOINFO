#================================================================
          # EXERCÍCIOS DE PYTHON PARA BIOTECNOLOGIA #
#================================================================

# EXERCÍCIO 1: CÁLCULO DE CONTEÚDO GC E MELTING TEMPERATURE (Tm)
# Em biotecnologia, o conteúdo GC e a Tm são cruciais para o design de primers.
# TAREFA:
# 1. Crie uma variável chamada 'sequencia_dna' com uma sequência de sua escolha.
# 2. Calcule a porcentagem de Guaninas (G) e Citosinas (C) na sequência.
# 3. Calcule a Tm usando a fórmula simplificada: Tm = 2*(A+T) + 4*(G+C).
# 4. Imprima o resultado formatado.

# ------------------------ RESOLUÇÃO ----------------------------

'''seq_dna = "ATCG"
g = seq_dna.count('G')
c = seq_dna.count("C")

porcentagem_gc = ((g + c) / len(seq_dna)) * 100

print(f"A porcentagem de 'G' e 'C' na sequencia é de {porcentagem_gc}%")

def calculo_tm(seq_dna):
    a = seq_dna.count("A")
    t = seq_dna.count("T")
    g = seq_dna.count('G')
    c = seq_dna.count("C")
    tm = 2 * (a+t) + 4 * (g+c)
    return tm

print(f"A 'Tm' da sequencia é igual a {calculo_tm(seq_dna)}")'''

# ===============================================================

# EXERCÍCIO 2: TRADUÇÃO DE SEQUÊNCIA (DO DNA À PROTEÍNA)
# Simule o dogma central da biologia molecular.
# TAREFA:
# 1. Use a biblioteca Bio.Seq (BioPython).
# 2. Converta uma sequência de DNA em RNA (Transcrição).
# 3. Converta esse RNA em uma sequência de Aminoácidos (Tradução).
# 4. O programa deve parar a tradução no primeiro 'STOP codon' que encontrar.

# ------------------------ RESOLUÇÃO ----------------------------

'''from Bio.Seq import Seq

seq_dna = input("Digite sua sequência de DNA: ").strip().upper().replace(" ", "")#"ATGGTGCACCTGACTCCT"

dna = Seq(seq_dna)
rna = dna.transcribe()

print(f"Nosso RNA é igual a {rna}")

proteina = rna.translate(to_stop=True)

print(f"Nosso RNA traduzido (até o Stop) é igual a {proteina}")'''

# ===============================================================

# EXERCÍCIO 3: FILTRO DE QUALIDADE DE SEQUENCIAMENTO
# Frequentemente recebemos arquivos com sequências que contêm "N" (bases desconhecidas).
# TAREFA:
# 1. Crie uma lista chamada 'pool_sequencias' contendo pelo menos 5 sequências.
# 2. Algumas devem ter apenas A, T, C, G e outras devem conter a letra "N".
# 3. Use um loop (for) para percorrer a lista.
# 4. O programa deve imprimir apenas as sequências que são 100% confiáveis (sem nenhum "N").

# ===============================================================

# ------------------------ RESOLUÇÃO ----------------------------

'''pool_seq = ["ATCG", "AATT", "CCGG", "CCNC", "ATGCGTACG", "ATGCNGTAC", "GGGTACCCG", "NNNATGCCC", "TTTGGGAAA"]
seq_n = 0
seq_c = 0
print("--- INICIANDO O FILTRO DE QUALIDADE: ---")
numero_seq = len(pool_seq)
for seq in pool_seq:
    if "N" in seq:
        seq_n += 1
        #print(f"Sequência NÃO CONFIÁVEL: {seq}")
    elif "N" not in seq:
        seq_c += 1
        print(f"Sequência CONFIÁVEL: {seq}")

print(40*"-")
print(f"O número total de sequências filtradas foi: {numero_seq}")
print(f"O total de sequências não confiáveis é: {seq_n}")
print(f"O total de sequências confiáveis é: {seq_c} ")
print("--- FILTRO FINALIZADO ---")'''

# ===============================================================

# EXERCÍCIO 4 (DESAFIO TCC): BUSCA DE MUTAÇÃO PONTUAL
# Útil para estudos como os de Anemia Falciforme.
# TAREFA:
# 1. Defina duas sequências: uma 'normal' e uma 'mutada' (com uma letra diferente).
# 2. Crie uma lógica que compare as duas posição por posição.
# 3. O programa deve dizer em qual posição a mutação ocorreu e quais eram as bases.

# ------------------------ RESOLUÇÃO ----------------------------

'''seq_n = "ATGC"
seq_m = "TTGG"

for i, (base_n, base_m) in enumerate(zip(seq_n, seq_m)):
    if base_n != base_m:
        print("----- MUTAÇÃO ENCONTRADA -----")
        print(f"A posição da mutação é: {i+1}")
        print(f"Base Normal: {base_n}")
        print(f"Base Mutada: {base_m}")
        print(f"Tipo: Substituição")
        print(30*"-")
        if base_n == "A" and base_m == "T":
            print("🛑 ALERTA!! 🛑 Esta troca (A por T) indica Anemia Falciforma (HbS)")
        else:
            print("Tipo: Outra variante genética detectada")
            print(30*"-")'''

# ===============================================================

# EXERCÍCIO 5: CONTADOR DE MUTAÇÕES TOTAIS (SNP)
# Na Anemia Falciforme, focamos em uma troca, mas genomas reais têm várias.
# TAREFA:
# 1. Crie uma função 'contar_variantes(seq1, seq2)' que compare duas sequências.
# 2. A função deve retornar o NÚMERO TOTAL de bases diferentes entre elas.
# 3. Teste com: seq_a = "ATGCCG", seq_b = "ATGCCT" (Deve retornar 1).

# ------------------------ RESOLUÇÃO ----------------------------

'''seq_a = input("Digite sua 1ª sequência: ").strip().upper().replace(" ", "")
seq_b = input("Digite sua 2ª sequência: ").strip().upper().replace(" ", "")

def contar_variantes(seq_1, seq_2):
    total_diferentes = 0
    for i, (base_1, base_2) in enumerate(zip(seq_1, seq_2)):
        if base_1 != base_2:
            total_diferentes += 1
        else:
            total_diferentes == total_diferentes
    return total_diferentes

print(40*"-=")
print(f"O número total de mutações encontradas foi de: {contar_variantes(seq_a, seq_b)}")
print(40*"-=")'''

# ===============================================================

# EXERCÍCIO 6: IDENTIFICADOR DE CÓDON DE INÍCIO (START CODON)
# Toda tradução biológica real começa no códon ATG (Metionina).
# TAREFA:
# 1. Dada uma sequência longa, use o método '.find("ATG")' para encontrar a 
#    posição onde o gene realmente começa.
# 2. Imprima a sequência a partir dessa posição até o final.
# DICA: dna_teste = "CCGATGCCTAG" -> Resultado esperado: "ATGCCTAG"

# ------------------------ RESOLUÇÃO ----------------------------

'''seq_dna = input("Digite sua sequência de DNA: ").strip().upper().replace(" ", "")

inicio = seq_dna.find("ATG")

print(40*"-")
print(f"A sequência limpa é: {seq_dna[inicio:]}")
print(40*"-")'''

# ===============================================================

# EXERCÍCIO 7: SIMULADOR DE MUTAÇÃO (SABOTAGEM GENÉTICA)
# Às vezes queremos testar o que acontece se "trocarmos" uma base no código.
# TAREFA:
# 1. Peça ao usuário uma sequência de DNA.
# 2. Peça uma posição (ex: 5) e uma nova base (ex: "T").
# 3. Use fatiamento (slicing) para criar uma nova string com a base trocada.
# DICA: nova_seq = seq[:posicao] + nova_base + seq[posicao+1:]

# ------------------------ RESOLUÇÃO ----------------------------

'''seq_dna = input("Digite sua sequência de DNA: ").strip().upper().replace(" ", "")
posiçao = int(input("Digite a posição desejada: "))
nova_base = input("Digite a nova base desejada: ").strip().upper()

seq_nova = seq_dna[:posiçao] + nova_base + seq_dna[posiçao+1:]

print(40*"-")
print(f"A nova sequência é: {seq_nova}")
print(40*"-")'''

# ===============================================================

# EXERCÍCIO 8: CÁLCULO DE PESO MOLECULAR (BIOPYTHON)
# O BioPython possui ferramentas para calcular propriedades físicas das proteínas.
# TAREFA:
# 1. Importe: from Bio.SeqUtils.ProtParam import ProteinAnalysis
# 2. Crie uma sequência de proteína (ex: "MVHLTPVEK").
# 3. Use 'analise = ProteinAnalysis(minha_proteina)' e imprima 'analise.molecular_weight()'.

# ------------------------ RESOLUÇÃO ----------------------------

'''from Bio.SeqUtils.ProtParam import ProteinAnalysis
from Bio.Seq import Seq

seq_dna = input("Digite sua sequência de DNA suja: ").strip().upper().replace(" ", "")
inicio_dna = seq_dna.find("ATG")
seq_dna_limpa = seq_dna[inicio_dna:]
dna = Seq(seq_dna_limpa)
rna = dna.transcribe()
proteina = rna.translate()
analise = ProteinAnalysis(proteina)

print(40*"-=")
print(f"Sua sequência DNA limpa é: {dna}")
print(f"Transcrita para RNA fica: {rna}")
print(f"Traduzia como proteína: {proteina}")
print(f"E o seu peso molecular é: {analise.molecular_weight()}")
print(40*"-=")'''

# =================================================================

# EXERCÍCIO 9: VISUALIZAÇÃO DE DADOS BIOLÓGICOS (GRÁFICOS)
# ENUNCIADO: 
# Criar um gráfico de barras que mostre a frequência de cada base nitrogenada.
# Isso ajuda a visualizar o perfil genético de uma sequência rapidamente.
# DICA: Se o VS Code der erro de 'ModuleNotFoundError', 
# rode no terminal: pip install matplotlib
# =================================================================

import matplotlib.pyplot as plt

def gerar_grafico_bases(seq): # Conta as bases A, T, C, G e gera um gráfico de barras colorido.
    bases = ["Adeninda (A)", "Timina (T)", "Citosina (C)", "Guanina (G)"]

    contagem = [
        seq.count('A'),
        seq.count('T'),
        seq.count('C'),
        seq.count('G')
    ]

    # Configurando a aparência do gráfico
    plt.figure(figsize=(10,6))

    cores = ['royalblue', 'firebrick', 'forestgreen', 'darkorange']

    plt.bar(bases, contagem, color=cores, edgecolor='black')

    # Adicionando informações textuais
    plt.title('DISTRIBUIÇÃO DE BASES NA SEQUÊNCIA', fontsize=20)
    plt.xlabel('Bases Nitrogenadas', fontsize=15)
    plt.ylabel('Frequência (Quantidade)', fontsize=15)

    # Adiciona o valor exato em cima de cada barra
    for i, valor in enumerate(contagem):
        plt.text(i, valor + 0.1, str(valor), ha='center', fontweight='bold')

    print("\n[INFO] Gráfico gerado com sucesso! Feche a janela para continuar...")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# --- ÁREA DE TESTE ---
# Vamos usar o fragmento da Hemoglobina que você está estudando
seq_dna = input("Digite sua sequência de DNA: ").strip().upper().replace(" ", "")

print(f"Analisando a sequência {seq_dna}...")
gerar_grafico_bases(seq_dna)