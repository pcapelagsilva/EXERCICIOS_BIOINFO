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