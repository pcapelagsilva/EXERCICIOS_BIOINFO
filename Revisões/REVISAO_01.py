# =================================================================
# DESAFIOS DE PRÁTICA: PYTHON E BIOINFORMÁTICA
# Tente resolver cada exercício criando uma função com 'def'
# =================================================================

# EXERCÍCIO 1: O Localizador de Motivos (Baseado no Rosalind SUBS)
# Crie uma função que receba uma sequência de DNA e um 'motivo' (uma sequência curta).
# A função deve retornar uma lista com todas as POSIÇÕES onde o motivo começa.
# Lembre-se: Na Bioinformática, a contagem geralmente começa em 1, não em 0!

''' def encontrar_motivos(dna, motivo):
    posicoes = []
    tamanho_motivo = len(motivo)
    
    # DICA: Use um loop 'for i in range' para percorrer o DNA
    # Compare o pedaço dna[i : i+tamanho_motivo] com o motivo
    
    # --- Seu código aqui ---
    # PERCORRE O DNA LETRA POR LETRA
    for i in range(len(dna) - tamanho_motivo + 1):
        # VERIFICA SE O TRECHO ATUAL É IGUAL AO QUE BUSCAMOS
        if dna[i:i+tamanho_motivo] == motivo:
            # ADICIONA A POSIÇÃO (ajustada para começar no 1)
            posicoes.append(i+1)
    return posicoes

print(encontrar_motivos("GATATATGCATATACTT", "ATAT"))'''
#Teste: encontrar_motivos("GATATATGCATATACTT", "ATAT") 
# Resultado esperado: [2, 4, 10]

# -----------------------------------------------------------------

# EXERCÍCIO 2: O Tradutor Seletivo
# Crie uma função que traduza RNA em Proteína, mas com um detalhe:
# Ela deve começar a tradução APENAS quando encontrar o primeiro "AUG".
# Se não encontrar "AUG", deve retornar "Sequência Inválida".

# TABELA DE CÓDON E SEUS SIGNIFICADOS EM PROTEINAS
''' TABELA_SIMPLIFICADA = {"AUG": "M", "UUU": "F", "UCU": "S", "UAA": "Stop"} '''
# DEFINIÇÃO DE UMA FUNÇÃO
''' def traduzir_com_inicio(rna):
    # DICA: Use rna.find("AUG") para saber onde começar
    # Use o passo 3 no range para ler os códons corretamente '''
    
    # --- Seu código aqui ---
    # DEFINIMOS ONDE A TRADUÇÃO DEVE INICIAR
'''    inicio = rna.find("AUG")
    # CASO O INICIO NÃO ESTIVER NA SEQUÊNCIA DE RNA, MOSTRAR QUE A SEQUÊNCIA É INVÁLIDA
    if inicio == -1:
        return "Sequência inválida!!!"
    # CORTA O RNA PARA COMEÇAR DO AUG EM DIANTE
    rna_codificante = rna[inicio:]
    # DEFINE A O GRUPO PROTEINA COMO VAZIO
    proteina = ""
    # PERCORRE A SEQUENCIA DO RNA CODIFICANTE DE 3 EM 3 PARES
    for i in range(0, len(rna_codificante), 3):
        codon = rna_codificante[i:i+3]
        # SE O CÓDON TIVER MENOS DE 3 LETRAS (final da String) PARAR
        if len(codon) < 3:
            break
        # INDICA QUE O AMINOACIDO É IGUAL A UM DOS VALORES DA TABELA
        aminoacido = TABELA_SIMPLIFICADA.get(codon)
        # CASO O AMINOACIDO LIDO TENHA O VALOR IGUAL A "Stop" OU VAZIO PARAR
        if aminoacido == "Stop" or aminoacido is None:
            break
        # SE O AMINOACIDO POSSUIR UM VALOR VÁLIDO, ADICIONAR O GRUPO PROTEÍNA QUE HAVIAMOS DEFINIDO LÁ NO INÍCIO
        proteina += aminoacido
    return proteina

print(traduzir_com_inicio("CCCAAAGGG"))'''
#Teste: traduzir_com_inicio("CCCAUGUUUUCUUAA") 
# Resultado esperado: "MFS"


# -----------------------------------------------------------------

# EXERCÍCIO 3: Detector de Erros de Sintaxe (O Desafio da Tupla)
# Olhe para o código abaixo. Ele tem um erro que você já enfrentou!
# Corrija a variável para que o cálculo da média funcione sem dar erro de 'tuple'.

''' def calcular_media_gc(conteudo_gc):
    # O erro está na linha abaixo:
    # valor_gc = conteudo_gc,  # Por que isso gera um erro de tupla? O erro ocorre por conta da vírugla logo após o "conteudo_gc", pois, quando adicionamos uma vírgula após qualquer valor o Python o identifica como uma Tupla (lista imutável) e não como outro valor que desejamos
    valor_gc = conteudo_gc # Código arrumado
    # Imagine que queremos somar um bônus de 0.1
    resultado = valor_gc + 0.1
    return resultado '''
 
# Teste para correção: 
#media = media = calcular_media_gc(0.5)
#print(f"A média corrigida é: {media}")

# -----------------------------------------------------------------

# EXERCÍCIO 4: Limpeza de Arquivos (Baseado no Rosalind)
# Muitas vezes os arquivos do Rosalind vêm com espaços ou quebras de linha.
# Crie uma função que receba uma lista de sequências e remova 
# os espaços e caracteres '\n' de todas elas.

''' def limpar_sequencias(lista_suja):
    lista_limpa = []
    # DICA: Use o método .strip() dentro de um loop
    # --- Seu código aqui ---
    # Olha para cada sequência dentro da lista_suja
    for seq in lista_suja:
        # O método .strip() remove os espaços e \n das pontas da sequencia
        seq_limpa = seq.strip()
        # Adicionamos a sequência limpa na nova lista (lista_limpa)
        lista_limpa.append(seq_limpa)
    return lista_limpa

print(limpar_sequencias(["  ATGC\n", " GGG "])) '''
# Teste: limpar_sequencias(["  ATGC\n", " GGG "]) 
# Resultado esperado: ["ATGC", "GGG"]

# -----------------------------------------------------------------
# DESAFIO PRÁTICO: MINI-PIPELINE DE BIOINFORMÁTICA
# Resolva os passos abaixo para processar dados de laboratório.
# -----------------------------------------------------------------
# --- PASSO 1: PADRONIZAÇÃO ---
# O laboratório enviou esta sequência suja e em minúsculas.
# Objetivo: Limpe os espaços e transforme tudo em MAIÚSCULAS.
''' dna_bruto = "   atgcccgggaaattt\n"
dna_limpo = dna_bruto.upper().strip()

print(f"1. DNA Padronizado: {dna_limpo}") '''


# --- PASSO 2: TRANSCRIÇÃO ---
# Objetivo: Transforme o dna_limpo em RNA (troque 'T' por 'U').
''' dna_limpo = 'ATGCCCGGGAAATTT'
rna = dna_limpo.replace('T', 'U')

print(f"2. RNA Gerado: {rna}") '''


# --- PASSO 3: EXTRAÇÃO DE CÓDONS ---
# Objetivo: Use o fatiamento (slicing) para pegar o TERCEIRO códon do rna.
''' rna = 'AUGCCCGGGAAAUUU'
terceiro_codon = rna[6:9]

print(f"3. Terceiro Códon: {terceiro_codon}") '''


# --- PASSO 4: BANCO DE DADOS (DICIONÁRIOS) ---
# Objetivo: Tente buscar o peso do aminoácido 'M' (Metionina).
# Se não existir, o código deve retornar 0.0 em vez de dar erro.
''' pesos = {"A": 71.04, "C": 103.01, "G": 57.02}
peso_m = pesos.get('M', 0.0)

print(f"4. Peso da Metionina: {peso_m}") '''


# --- PASSO 5: PROCESSAMENTO DE LISTA ---
# Objetivo: Você recebeu uma lista de amostras. 
# Adicione "Amostra_04" ao final e depois coloque em ordem alfabética.
''' amostras = ["Amostra_03", "Amostra_01", "Amostra_02"]

amostras.append("Amostra_04")
amostras.sort()

print(f"5. Amostras Organizadas: {amostras}") '''


# --- PASSO 6: VALIDAÇÃO FINAL ---
# Objetivo: Calcule a porcentagem de 'G' neste fragmento: "GGAAAAAA"
# Use (quantidade / total) * 100 e converta para INTEIRO (int).
''' seq_teste = "GGAAAAAAAA"
quantidade_g = seq_teste.count('G')
total_bases  = len(seq_teste)
porcentagem_g = int((quantidade_g/total_bases)*100)

print(f"6. Porcentagem de G: {porcentagem_g}%") '''

# -----------------------------------------------------------------
# DESAFIOS INTERMEDIÁRIOS: LÓGICA E FILTRAGEM
# -----------------------------------------------------------------

# --- DESAFIO 1: O FILTRO DE QUALIDADE ---
# Em sequências de DNA, letras minúsculas às vezes indicam baixa qualidade.
# Objetivo: Conte quantas bases MAIÚSCULAS existem na sequência abaixo.
''' sequencia_mista = "ATgcTGGcaG"
bases_alta_qualidade = 0 

# Dica: Use um loop 'for' e o método .isupper()
for base in sequencia_mista:
    if base.isupper():
        bases_alta_qualidade += 1

print(f"1. Bases de alta qualidade: {bases_alta_qualidade}") '''


# --- DESAFIO 2: BUSCA DE MOTIVOS (PADRÕES) ---
# Objetivo: Verifique se o motivo "ATG" (códon de início) está presente.
# Se estiver, imprima a posição (índice) onde ele começa.
''' fita_dna = "CCGGTATGCCAA"
posicao_inicio = fita_dna.find('ATG')

print(f"2. O motivo começa no índice: {posicao_inicio}") '''


# --- DESAFIO 3: TRADUTOR DE EMERGÊNCIA ---
# Objetivo: Dado o dicionário abaixo, converta a lista de códons em proteína.
''' tabela = {"AUG": "Met", "CCG": "Pro", "UAA": "STOP"}
rna_lista = ["AUG", "CCG", "UAA"]
proteina = []

for codon in rna_lista:
    aminoacido = tabela.get(codon)
    proteina.append(aminoacido) '''
    
# Dica: Use um loop 'for' para percorrer rna_lista e .append() para a proteína.
''' print(f"3. Proteína gerada: {proteina}") '''


# --- DESAFIO 4: FILTRO DE TAMANHO (LIST COMPREHENSION) ---
# Objetivo: Dada uma lista de sequências, crie uma nova lista apenas 
# com as que possuem mais de 5 bases.
''' biblioteca = ["ATGC", "ATGCUUU", "AT", "GGGCCCTTT", "C", "ATCGU"]
sequencias_longas = []
sequencias_curtas = []
sequencias_com_5_aminoacidos = []
for base in biblioteca:
    if len(base) > 5:
        sequencias_longas.append(base)
    elif len(base) == 5:
        sequencias_com_5_aminoacidos.append(base)
    elif len(base) < 5:
        sequencias_curtas.append(base)
print(f"4. Sequências longas: {sequencias_longas}; Sequências curtas: {sequencias_curtas}; Sequência com 5 bases: {sequencias_com_5_aminoacidos} ") '''