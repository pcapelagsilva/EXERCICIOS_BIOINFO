# =================================================================
# REVISÃO: FUNÇÕES (DEF) E MANIPULAÇÃO DE ARQUIVOS FASTA
# =================================================================

# EXERCÍCIO 1: A FUNÇÃO "BOM DIA"
# TAREFA: Crie uma função chamada 'saudacao' que recebe o nome de um paciente e RETORNA a frase: "Olá, [nome]!"
# ---------------------------------------------------------
'''def saudaçao(nome):
    return f"Olá {nome}!!Peor"

nome = input("Digite seu nome: ")
print(saudaçao(nome))'''


# ---------------------------------------------------------
# EXERCÍCIO 2: CALCULADORA DE BASES
# TAREFA: Crie uma função chamada 'somar_bases' que recebe dois números (ex: quantidade de A e de T) e retorna a soma.
# ---------------------------------------------------------

'''def somar_bases(quant_a, quant_t):
    soma = quant_a + quant_t
    return soma

a = int(input("Digite a quantidade de 'A' da sua sequência: "))
t = int(input("Digite a quantidade de 'T' da sua sequência: "))

print(somar_bases(a, t))'''

# ---------------------------------------------------------
# EXERCÍCIO 3: DETECTOR DE INÍCIO (START CODON)
# TAREFA: Crie uma função chamada 'tem_inicio' que recebe uma sequência e retorna True se ela começar com "ATG".
# ---------------------------------------------------------

'''def tem_inicio(dna):
    if dna.startswith("ATG"):
        return True
    else:
        return False

seq = str(input("Digite sua sequência: ")).strip().upper().replace(" ", "")
print(tem_inicio(seq))'''

# ---------------------------------------------------------
# EXERCÍCIO 4: CONTADOR DE LINHAS
# TAREFA: Abra o arquivo 'sequencias.fasta', percorra-o 
# com um 'for' e conte quantas linhas ele tem no total.
# ---------------------------------------------------------

'''contador = 0
with open ("sequencias_rev.fasta", "r") as arquivo:
    for linha in arquivo:
        contador += 1

print(f"O arquivo tem o total de {contador} linhas")'''

# ---------------------------------------------------------
# EXERCÍCIO 5: FILTRO DE CABEÇALHO
# TAREFA: Abra o arquivo 'sequencias.fasta' e imprima APENAS as linhas que começam com ">".
# ---------------------------------------------------------

'''with open("sequencias_rev.fasta", "r") as arquivo:
    for linha in arquivo:
        if linha.startswith(">"):
            print(f"Cabeçalho encontrado: {linha.strip()}")'''

# ---------------------------------------------------------

# Antes de começar: Crie um arquivo chamado 'sequencias.fasta' na mesma 
# pasta do seu código e cole o conteúdo abaixo nele:
# >seq1
# ATGCGTACGT
# >seq2
# ATGGTGCACCTGACTCCTGAGGAG
# >seq3
# ATGC123N

# -----------------------------------------------------------------
# EXERCÍCIO R1: A ESTRUTURA BÁSICA DO DEF
# -----------------------------------------------------------------
# TAREFA: Crie uma função chamada 'exibir_estatistica' que receba uma sequência e apenas imprima o tamanho dela (len).
# Teste a função chamando: exibir_estatistica("ATGGT")

# def exibir_estatistica --> Mostra como a função irá ser chamada depois;
# (seq) --> O que você precisa colocar dentro dela para funcionar (no nosso caso a sequencia de dna);
# tamanho = len(seq) --> O que a "máquina" faz com os ingredientes;
# return --> O resultado que sai da máquina.
'''def exibir_estatistica(seq):
    tamanho = len(seq)
    return tamanho

print(exibir_estatistica("ATGGT"))'''

# -----------------------------------------------------------------
# EXERCÍCIO R2: LENDO O ARQUIVO LINHA POR LINHA
# -----------------------------------------------------------------
# TAREFA: Use o comando 'with open("sequencias.fasta", "r") as arquivo:'
# Faça um loop 'for linha in arquivo' e imprima apenas as linhas que NÃO começam com ">" (ou seja, apenas as sequências).
# DICA: Use 'if not linha.startswith(">"):'

'''with open('sequencias_rev.fasta', 'r') as arquivo:
    for linha in arquivo:
        linha_limpa = linha.strip()
        if not linha.startswith(">"):
            print(f"DNA encontrado: {linha_limpa}")'''


# -----------------------------------------------------------------
# EXERCÍCIO R3: UNINDO DEF + ARQUIVO (O QUE CAI NO TCC)
# -----------------------------------------------------------------
# TAREFA: 
# 1. Crie uma função 'processar_bio' que recebe uma sequência, calcula o conteúdo GC e retorna esse valor.
# 2. Abra o arquivo FASTA.
# 3. Para cada linha de sequência, chame a função e mostre o resultado.

# Define o nome da ferramenta e o que é preciso pro dentro dela para funcionar
'''def processar_bio(seq):
    g = seq.count("G")
    c = seq.count("C")
    # Calcula a porcentagem de GC
    total = len(seq)
    if total > 0:
        porcentagem_gc = ((g + c)/total)*100
        return porcentagem_gc # <-- Entrega o valor para fora
    else:
        return 0

# Abre o arquivo que desejamos e apelidamos ele de 'arquivo'
with open("sequencias_rev.fasta", "r") as arquivo:
    for linha in arquivo:
        linha_limpa = linha.strip()
        # Se o cabeçalho for '>', imprimimos apenas o nome da sequência
        if linha_limpa.startswith(">"):
            print(f"\nAnalisando: {linha_limpa}")
        # Se o cabeçalho NÃO for '>', é DNA! mandamos para função
        else:
            # Chamamos a função: Passamos a linha e guardamos o retorno em 'resultado'
            resultado = processar_bio(linha_limpa)
            print(f"Conteúdo GC: {resultado:.2f}%")'''

# -----------------------------------------------------------------
# EXERCÍCIO R4: LIMPEZA DE DADOS (STRIP)
# -----------------------------------------------------------------
# TAREFA: Arquivos texto vêm com um "\n" (quebra de linha) invisível.
# Modifique o exercício anterior usando o método '.strip()' para limpar a sequência antes de mandar para a função.

'''def processar_bio(seq):
    g = seq.count("G")
    c = seq.count("C")
    total = len(seq)

    if total > 0:
        porcentagem_gc = ((g+c)/total)*100
        return porcentagem_gc
    else:
        return 0

with open("sequencias_rev.fasta", "r") as entrada, open("relatorio_final_rev04.txt", "w") as saida:

    saida.write("=== RELATÓRIO DE ANÁLISE GENÉTICA ===\n\n")

    for linha in entrada:
        linha_limpa = linha.strip()

        if linha_limpa.startswith(">"):
            nome = linha_limpa
            saida.write(f"Amostra: {nome}\n")

        else:
            res = processar_bio(linha_limpa)
            saida.write(f"Resultado GC: {res:.2f}%\n")
            saida.write("-"*30 + "\n")

print("Arquivo 'relatorio_final_rev04.txt' gerado com sucesso")'''

# ---------------------------------------------------------
# EXERCÍCIO 6: O LIMPADOR DE DNA (REPLACE)
# TAREFA: Crie uma função chamada 'limpar_dna' que recebe 
# uma sequência cheia de traços (ex: "A-T-G-C") e retorna 
# apenas as letras, sem os traços.
# DICA: Use o comando .replace("-", "")
# ---------------------------------------------------------

'''def limpar_dna(seq):
    seq_limpa = seq.strip().upper().replace("-", "").replace(" ", "")
    return seq_limpa

dna = input("Digite sua sequência suja: ").strip().upper().replace("-", "").replace(" ", "")
print(limpar_dna(dna))'''

# ---------------------------------------------------------
# EXERCÍCIO 7: COMPARADOR DE TAMANHO
# TAREFA: Crie uma função chamada 'comparar_amostras' que 
# recebe DUAS sequências. Se a primeira for maior que a 
# segunda, retorne "Amostra 1 é maior". Caso contrário, 
# retorne "Amostra 2 é maior ou igual".
# ---------------------------------------------------------

'''def comparar_tamamho(seq1, seq2):
    if len(seq1) > len(seq2):
        return "A primeira amostra é maior que a segunda"
    else:
        return "A segunda amostra é maior que a primeira"

seq_a = input("Digite sua primeira sequência: ").strip().upper().replace(" ", "")
seq_b = input("Digite sua segunda sequência: ").strip().upper().replace(" ", "")

print(comparar_tamamho(seq_a, seq_b))'''

# ---------------------------------------------------------
# EXERCÍCIO 8: CONTADOR DE MUTAÇÕES (PONTO ÚNICO)
# TAREFA: Crie uma função chamada 'contar_g' que recebe 
# uma sequência. Ela deve contar quantas vezes a base 'G' aparece e retornar esse número multiplicado por 10 
# (simulando um cálculo de score de qualidade).
# ---------------------------------------------------------

'''def contar_g(sequencia):
    g = sequencia.count("G")
    total = g * 10
    return total

dna = input("Digite sua sequência: ").strip().upper().replace(" ", "")
print(f"A sequência possui no total {dna.count("G")} G, e esse número vezes 10 fica igual a {contar_g(dna)}")'''


# ---------------------------------------------------------
# EXERCÍCIO 9: O FILTRO DO ARQUIVO (DESAFIO FINAL)
# TAREFA: Abra o arquivo 'sequencias.fasta'. Para cada linha que for DNA (que não começa com ">"), use a sua função 
# do EXERCÍCIO 6 para limpar a sequência e imprima o resultado.
# ---------------------------------------------------------

'''def limpar_dna(seq):
    seq_limpa = seq.strip().upper().replace("-", "").replace(" ", "")
    return seq_limpa

with open("sequencias_rev.fasta", "r") as arquivo:
    for linha in arquivo:
        if linha.startswith(">"):
            continue
        else:
            print(limpar_dna(linha))'''

# =================================================================
# REVISÃO AVANÇADA: PROCESSAMENTO DE GENOMAS E ARQUIVOS
# =================================================================

# ---------------------------------------------------------
# EXERCÍCIO 10: TRADUTOR DE FITAS (COMPLEMENTAR)
# TAREFA: Crie uma função chamada 'gerar_complementar' que 
# recebe uma sequência e substitui: A por T, T por A, 
# C por G e G por C. 
# DICA: Use .replace() ou um dicionário. Retorne a fita nova.
# ---------------------------------------------------------

'''def gerar_complementar(dna):
    seq_pronta = ""
    for base in dna:
        if base == "A":
            seq_pronta += "T"
        elif base == "T":
            seq_pronta += "A"
        elif base == "C":
            seq_pronta += "G"
        elif base == "G":
            seq_pronta += "C"
        else:
            seq_pronta == base

    return seq_pronta

seq = input("Digite sua sequência: ").strip().upper().replace(" ", "")

print(gerar_complementar(seq))'''

# ---------------------------------------------------------
# EXERCÍCIO 11: LOCALIZADOR DE MUTAÇÃO (SNP)
# TAREFA: Crie uma função chamada 'buscar_mutacao' que recebe uma sequência. Se ela encontrar o padrão "GTG" 
# (mutação da anemia falciforme), retorne: "⚠️ Mutação Detectada".
# Caso contrário, retorne: "✅ Sequência Normal".
# ---------------------------------------------------------

'''def buscar_mutacao(seq):
    posicao = seq.find("GTG")
    
    if posicao != -1:
        return f"⚠️ Mutação Detectada na posição: {posicao + 1}"
    else:
        return "✅ Sequência Normal"

# Teste
dna = input("Digite a sequência: ").strip().upper()
print(buscar_mutacao(dna))'''

# ---------------------------------------------------------
# EXERCÍCIO 12: CONTADOR DE QUALIDADE (BASES N)
# TAREFA: Em sequenciamentos ruins, aparecem muitos "N". 
# Crie uma função 'checar_qualidade' que retorna a 
# PORCENTAGEM de letras "N" em uma sequência.
# ---------------------------------------------------------

'''def checar_qualidade(sequencia):
    n = sequencia.count("N")
    tamanho = len(sequencia)

    if tamanho > 0:
        porcentagem_n = (n/tamanho)*100
        return porcentagem_n
    else:
        return 0
    
dna = input("Digite sua sequência: ").strip().upper().replace(" ", "")
print(f"Qualidade: {checar_qualidade(dna)}% de N")'''

# ---------------------------------------------------------
# EXERCÍCIO 13: O DESAFIO DO ARQUIVO REAL (INTEGRAÇÃO)
# TAREFA: 
# 1. Abra o arquivo 'sequencias.fasta'.
# 2. Para cada sequência (pule os cabeçalhos >):
#    - Use a função do EX 11 para ver se tem mutação.
#    - Use a função do EX 12 para ver se a qualidade é boa.
#    - Imprima um laudo para cada uma.
# ---------------------------------------------------------

'''def buscar_mutacao(seq):
                posicao = seq.find("GTG")
    
                if posicao != -1:
                    return f"⚠️ Mutação Detectada na posição: {posicao + 1}"
                else:
                    return "✅ Sequência Normal"
                
def checar_qualidade(sequencia):
                n = sequencia.count("N")
                tamanho = len(sequencia)

                if tamanho > 0:
                    porcentagem_n = (n/tamanho)*100
                    return porcentagem_n
                else:
                    return 0

with open("sequencias_rev.fasta", "r") as arquivo:
    for linha in arquivo:
        linha_limpa = linha.strip().upper()

        if linha_limpa.startswith(">"):
               print(f"\nAnalisando: {linha_limpa}")
        else:
            resultado_mutacao = buscar_mutacao(linha_limpa)
            resultado_qualidade = checar_qualidade(linha_limpa)

            print(resultado_mutacao)
            print(f"Ruído (N): {resultado_qualidade:.2f}%")'''

# =================================================================
# REVISÃO: LÓGICA DE PROGRAMAÇÃO PARA BIOINFORMÁTICA
# =================================================================

# ---------------------------------------------------------
# EXERCÍCIO 14: FILTRO DE COMPRIMENTO (DNA DE INTERESSE)
# TAREFA: Às vezes, o sequenciador gera fragmentos muito curtos 
# que não servem. Crie uma função 'e_longo_o_suficiente' que 
# recebe uma sequência e um tamanho mínimo (ex: 10). 
# Se a sequência for maior ou igual ao mínimo, retorne True.
# ---------------------------------------------------------

'''def e_longo_o_suficiente(sequencia):
    minimo = 10
    if len(sequencia) >= minimo:
        return True
    elif len(sequencia) < minimo:
        return "Sequência inválida"
    else:
        return False

seq = input("Digite uma sequência de no mínimo 10 bases: ").strip().upper().replace(" ", "")
print(e_longo_o_suficiente(seq))'''

# ---------------------------------------------------------
# EXERCÍCIO 15: TRADUTOR DE PROTEÍNA (CÓDON DE PARADA)
# TAREFA: Crie uma função 'tem_parada' que verifica se a 
# sequência de DNA contém algum dos "Stop Codons": 
# TAA, TAG ou TGA. 
# Se encontrar qualquer um, retorne "⚠️ Proteína Incompleta".
# ---------------------------------------------------------
# Tabela de Códons (Dicionário de Tradução)
'''tabela_codons = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'stop', 'TAG':'stop', 'TGC':'C', 'TGT':'C', 'TGA':'stop', 'TGG':'W',
}

def tem_parada(dna):
    if "TAA" in dna or "TAG" in dna or "TGA" in dna:
        return "⚠️ Proteína Incompleta"
    else:
        return "✅ Sequência Completa (Sem Stop Codons)"

print(tem_parada("ATGATAAGCT"))'''

# ---------------------------------------------------------
# EXERCÍCIO 16: CONTADOR DE ADENINAS (RIQUEZA DE A)
# TAREFA: Crie uma função 'contar_a' que retorna apenas a 
# quantidade absoluta de letras "A" em uma sequência.
# ---------------------------------------------------------

'''def contar_a(dna):
    return dna.upper().count("A")

seq = input("Digite uma sequência: ").strip().upper().replace(" ", "")
print(contar_a(seq))'''

# ---------------------------------------------------------
# EXERCÍCIO 17: O SUPER PIPELINE (DESAFIO)
# TAREFA: 
# 1. Abra o seu arquivo 'sequencias.fasta'.
# 2. Para cada sequência (pule cabeçalhos):
#    - Se 'e_longo_o_suficiente' for True:
#        - Conte as Adeninas (Ex 16).
#        - Verifique se tem Stop Codon (Ex 15).
#        - Imprima: "Sequência válida encontrada!" e os dados.
#    - Caso contrário:
#        - Imprima: "❌ Sequência muito curta para análise."
# ---------------------------------------------------------
'''def contar_a(dna):
    return dna.upper().count("A")

def tem_parada(dna):
    if "TAA" in dna or "TAG" in dna or "TGA" in dna:
        return "⚠️ Proteína Incompleta"
    else:
        return "✅ Sequência Completa (Sem Stop Codons)"
    
def e_longo_o_suficiente(sequencia):
    minimo = 10
    if len(sequencia) >= minimo:
        return True
    elif len(sequencia) < minimo:
        return "Sequência inválida"
    else:
        return False
    
with open("sequencias_rev.fasta", "r") as arquivo:
    for linha in arquivo:
        if linha.startswith(">"):
            continue
        else:
            if e_longo_o_suficiente(linha):
                qtd_a = contar_a(linha)
                aviso_stop = tem_parada(linha)
                print(f"✅ Sequência válida encontrada!")
                print(f"   - Adeninas: {qtd_a}")
                print(f"   - Status: {aviso_stop}")
            else:
                print("❌ Sequência muito curta para análise.")'''