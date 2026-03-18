# EXERCÍCIO ESTRUTURA DE REPETIÇÃO 'FOR' - 1º
''' frase = str(input("Escreva uma frase: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for p in range(len(junto) -1, -1, -1):
    inverso += junto [p]
if inverso == junto:
    print(f"A frase '{junto}' é um palindromo")
else:
    print(f" A frase '{junto}' não é um palindromo")
print("ANALISE FINALIZADA") '''

# EXERCÍCIO ESTRUTURA DE REPETIÇÃO 'FOR' - 2º
'''num = int(input("Digite um número: "))
for tabuada in range(1,11):
    valor = num * tabuada
    print(f"{valor}", end=" | ")
print("FIM")'''

# EXERCÍCIO ESTRUTURA DE REPETIÇÃO 'FOR' - 3º
'''par = impar = 0
soma = 0
for num in range(1, 501, 2):
    if num % 3 == 0: # todos os números impares divisíveis por 3
        soma += num
print(f'A soma de todos os números impares de 1 a 500 é igual a {soma}')'''

# EXERCÍCIO ESTRUTURA DE REPETIÇÃO 'FOR' - 4º
'''maior = 0
menor = 0

for p in range(1,6):
    peso = float(input(f"Peso da {p}ª pessoa (KG): "))

    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < maior:
            menor = peso
print(f"A pessoa mais pesada tem {maior}Kg")
print(f"A pessoa com o menor peso tem {menor}Kg")'''

# EXERCÍCIO ESTRUTURA DE REPETIÇÃO 'FOR' - 5º
''' num = int(input('Digite um número inteiro: '))
tot = 0

for p in range(1, num + 1 ):
    if num %  p == 0:
        tot += 1
    else:
        tot == 0
if tot == 2:
    print("O número é primo!!")
else:
    print("O número não é primo!!!") '''

# EXERCÍCIO ESTRUTURA DE REPETIÇÃO 'FOR' - 6º
''' from datetime import date
atual = date.today().year
tot_maior = 0
tot_menor = 0

for p in range(1,8):
    ano = int(input('Digite seu ano de nascença: '))
    idade = atual - ano

    if idade >= 21:
        tot_maior += 1
    else:
        tot_menor += 1

print(f'Ao todo {tot_maior} pessoas são maiores de idade')
print(f'Ao todo {tot_menor} pessoas são menores de idade')'''

# EXERCÍCIO ESTRUTURA DE REPETIÇÃO 'WHILE' - 1º
'''sexo = str(input('Digite seu sexo: ')).upper()

while sexo not in 'MF':
    sexo = str(input('Dados inválidos!!! digite seu sexo novamente: ')).upper()

print(f"Seu sexo foi registrado com sucesso!!")'''

# EXERCÍCIO ESTRUTURA DE REPETIÇÃO 'WHILE' - 2º
'''n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
opcao = 0

while opcao != 5:
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos números')
    print('[5] Sair do programa')
    opcao = int(input('Escolha uma das opções: '))

    if opcao == 1:
        print(f'A soma de {n1} e {n2} é igual a {n1 + n2}.')
    
    elif opcao == 2:
        print(f'A multiplicação do {n1} pelo {n2} é igual a {n1 * n2}.')
    
    elif opcao == 3:
        maior = n1 if n1 > n2 else n2
        print(f'Entre os números {n1} e {n2}, o maior é {maior}')
    
    elif opcao == 4:
        print("Informe novos números: ")
        n1 = float(input("Digite um número: "))
        n2 = float(input("Digite outro número: "))
    
    elif opcao == 5:
        print("FINALIZANDO O SISTEMA...")
    
    else:
        print("OPÇÃO INVÁLIDA, TENTE NOVAMENTE...")

print('PROGRAMA FINALIZADO COM SUCESSO')'''

# EXERCÍCIO ESTRUTURA DE REPETIÇÃO 'WHILE' - 3º
''' valor = int(input("Qual valor você deseja sacar?? R$"))
total = valor
cedula = 200
total_cedulas = 0

while True:
    if total >= cedula:
        total -= cedula
        total_cedulas += 1
    else:
        if total_cedulas > 0:
            print(f'Total de {total_cedulas} cédulas de R${cedula}')
        if cedula == 200:
            cedula = 50
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula ==10:
            cedula = 2
        elif cedula == 2:
            cedula =1
        total_cedulas = 0
        if total == 0:
            break
print(f"Saque de R${valor} finalizado...") '''

# EXERCÍCIO ESTRUTURA DE REPETIÇÃO 'WHILE' - 4º
''' from random import randint

computador = randint(1,11)
print('Estou pensando em um número de 1 a 10... será que você consegue acertar??')
acertou = False
palpite = 0

while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print(f'Você errou... vou dar uma dica, o número que eu pensei é maior do que você chutou')
        elif jogador > computador:
            print(f'Você errou... vou dar uma dica, o número que eu pensei é menor do que você chutou')
print(f'PARABÉNS!!! Você acertou com {palpite} tentativas...') '''

# EXERCÍCIO ESTRUTURA DE REPETIÇÃO 'WHILE' - 5º
''' total = totmil = menor = cont = 0
barato = ''

while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco

    if preco > 1000:
        totmil += 1
    
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja contiuar? [S/N]'))

    if resp == 'N':
        break
print(f'{" FIM DO PROGRAMA ":-^40}')
print(f'O total da compra foi R$ {total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}') '''

"""
ARQUIVO MESTRE DE REVISÃO - PYTHON
Este arquivo contém os exercícios resolvidos da semana e o desafio de estoque.
"""

# 1. STRINGS E ESCAPE (RESOLVIDO)
''' s1 = "Python é legal"
s2 = "ab\ncd"
s3 = "c:\\users\\user"

len(s1) -> 14
len(s2) -> 5
len(s3) -> 13 '''

# 2. MANIPULAÇÃO DE LISTAS (RESOLVIDO)
''' def filtrar_vencedores(corredores):
    vencedores = []
    for racer in corredores:
        if racer['finish'] == 1:
            if racer['name'] is not None:
                vencedores.append(racer['name'])
    return vencedores '''

# 3. BIBLIOTECAS - FATORIAL (RESOLVIDO)
''' import math as mt
def calcular_fatorial_de_cinco():
    return mt.factorial(5) '''

# 4. DESAFIO BLACKJACK (RESOLVIDO)
''' def calcular_pontos(mao):
    soma = 0
    for carta in mao:
        if carta in ['J', 'Q', 'K']:
            soma += 10
        elif carta == 'A':
            soma += 11
        else:
            soma += int(carta)
    
    if soma > 21:
        return 0
    return soma '''

# 5. DESAFIO FINAL: ANALISADOR DE ESTOQUE (PARA RESOLVER)
''' estoque = [
    {"nome": "Teclado", "preco": 150, "quantidade": 5},
    {"nome": "Mouse", "preco": 80, "quantidade": 0},
    {"nome": "Monitor", "preco": 900, "quantidade": 2},
    {"nome": "Fone", "preco": 200, "quantidade": 10},
]

def analisar_estoque(lista_produtos):
    """
    Objetivo: Retornar o valor total financeiro e lista de itens zerados.
    """
    relatorio = {
        "valor_total_estoque": 0,
        "itens_esgotados": []
    }
    for produtos in lista_produtos:
        valor_item = produtos['preco'] * produtos['quantidade']
        relatorio ['valor_total_estoque'] += valor_item
        if produtos['quantidade'] == 0:
            relatorio['itens_esgotados'].append(produtos['nome'])
    
    return relatorio '''

# =============================================================
# ÁREA DE EXECUÇÃO E TESTES
# =============================================================
if __name__ == "__main__":

# RESULTADO EXERCÍCIO 1
    ''' print("--- 1. Strings ---")
    print(f"Comprimentos: s1={len(s1)}, s2={len(s2)}, s3={len(s3)}") '''

# RESULTADO EXERCÍCIO 2
    ''' print("\n--- 2. Mario Kart ---")
    dados_exemplo = [{'name': 'Bowser', 'finish': 1}, {'name': None, 'finish': 1}, {'name': 'Toad', 'finish': 1}]
    print(f"Vencedores: {filtrar_vencedores(dados_exemplo)}") '''

# RESULTADO EXERCÍCIO 3
    ''' print("\n--- 3. Math ---")
    print(f"Fatorial de 5: {calcular_fatorial_de_cinco()}") '''

# RESULTADO EXERCÍCIO 4
    ''' print("\n--- 4. Blackjack ---")
    mao_teste = ['J', 'A', '2']
    print(f"Pontos da mão {mao_teste}: {calcular_pontos(mao_teste)}") '''

# RESULTADO EXERCÍCIO 5 - DESAFIO
    ''' print("\n--- 5. DESAFIO DE ESTOQUE ---")
    resultado = analisar_estoque(estoque)
    print(f"Valor Total: R$ {resultado['valor_total_estoque']}")
    print(f"Itens Esgotados: {resultado['itens_esgotados']}") '''

"""
LISTA DE ESTUDOS - VOLUME 2
Tópicos: Manipulação de Dados, Filtragem e Transformação.
"""

# DESAFIO 1: O FILTRO DE NOTAS
# Objetivo: Criar um dicionário com a média e a situação (Aprovado/Reprovado).
''' def avaliar_aluno(nome, notas):
    """
    Recebe um nome e uma lista de notas.
    Retorna um dicionário com: 'nome', 'media' e 'situacao'.
    Regra: media >= 7 -> "Aprovado", senão "Reprovado".
    """
    # Dica: media = sum(notas) / len(notas)
    media = sum(notas) / len(notas)

    if media >= 7:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
    
    resultado = {
        "Nome": nome,
        "Média": media,
        "Situação": situacao
        }
    return resultado '''

# DESAFIO 2: BUSCA DE USUÁRIO POR E-MAIL
# Objetivo: Encontrar um dicionário específico dentro de uma lista.
''' usuarios = [
    {"id": 1, "nome": "Alice", "email": "alice@gmail.com"},
    {"id": 2, "nome": "Pedro", "email": "pedro@uol.com.br"},
    {"id": 3, "nome": "Maria", "email": "maria@outlook.com"},
    {"id": 4, "nome": "Claudia", "email": "kaucapela@hotmail.com"}
]

def buscar_por_email(lista, email_procurado):
    """
    Deve retornar o NOME do usuário dono do e-mail.
    Se não encontrar, retorne "Usuário não encontrado".
    """
    for usuario in lista:
        if usuario['email'] == email_procurado:
            return usuario['nome']
    return "Usurário não encontrado" '''

# DESAFIO 3: CALCULADORA DE DESCONTO NO CARRINHO
# Objetivo: Aplicar lógica matemática em massa.
''' carrinho = [
    {"item": "Camiseta", "preco": 50},
    {"item": "Calça", "preco": 120},
    {"item": "Tênis", "preco": 300},
]

def aplicar_cupom(lista_itens, porcentagem_desconto):
    """
    Recebe a lista e um número (ex: 10 para 10%).
    Retorna o valor TOTAL do carrinho com o desconto aplicado.
    """
    # Dica: novo_preco = preco * (1 - desconto/100)
    total_desconto = 0
    multiplicador = 1 - (porcentagem_desconto / 100)
    for produto in lista_itens:
        preco_original = produto['preco']
        total_desconto += preco_original * multiplicador
    return total_desconto '''

# =============================================================
# ÁREA DE TESTES (Para você rodar no terminal)
# =============================================================
''' if __name__ == "__main__":
    #print("--- Teste 1: Notas ---")
    #print(avaliar_aluno("Pedro", [10, 6, 8])) 
    
    #print("\n--- Teste 2: Busca ---")
    #print(buscar_por_email(usuarios, "pedro@uol.com.br"))
    #print(buscar_por_email(usuarios, "fake@gmail.com"))
    #print(buscar_por_email(usuarios, "kaucapela@hotmail.com"))
    #print(buscar_por_email(usuarios, "0908@gmail.com"))

    #print("\n--- Teste 3: Carrinho ---")
    #print(f"Total com desconto: R$ {aplicar_cupom(carrinho, 10)}") '''

"""
LISTA DE EXERCÍCIOS - REVISÃO SEMANAL (Nível: Fácil ao Difícil)
Temas: Listas, Dicionários, Funções e Lógica de Negócio.
"""

# =============================================================
# EXERCÍCIO 1: O CONTADOR DE PALAVRAS (Fácil)
# Objetivo: Trabalhar com strings e listas simples.
# =============================================================
''' def contar_palavras(frase):
    """
    Recebe uma frase e retorna o número total de palavras.
    Dica: Use o método .split() que transforma uma string em lista.
    """
    palavras = frase.split()
    total = len(palavras)
    return total '''

# =============================================================
# EXERCÍCIO 2: O FORMATA-NOME (Médio)
# Objetivo: Manipular dicionários e strings.
# =============================================================

''' def formatar_usuario(id_usuario, nome_completo):
    """
    Recebe um ID e um Nome Completo.
    Deve retornar um dicionário com:
    - 'id': o ID recebido
    - 'primeiro_nome': apenas o primeiro nome
    - 'sobrenome': o restante do nome
    """
    nome = nome_completo.split()
    primeiro_nome = nome[0]
    sobrenome = " ".join(nome[1:])
    usuario = {
        "ID": id_usuario,
        "Nome": primeiro_nome,
        "Sobrenome": sobrenome
    }
    return usuario '''
    
# =============================================================
# EXERCÍCIO 3: FILTRO DE PREÇOS (Médio/Difícil)
# Objetivo: Filtrar itens de um dicionário com base em uma condição.
# =============================================================
''' produtos_loja = [
    {"nome": "MousePad", "preco": 35.50},
    {"nome": "Monitor 4K", "preco": 2500.00},
    {"nome": "Cabo HDMI", "preco": 45.00},
    {"nome": "Cadeira Gamer", "preco": 1200.00},
    {"nome": "Teclado Reizer", "preco": 353.04},
    {"nome": "WebCam", "preco": 98.90}
]

def filtrar_produtos_baratos(lista, preco_maximo):
    """
    Deve percorrer a lista e retornar uma NOVA lista apenas com 
    os NOMES dos produtos que custam menos ou igual ao preco_maximo.
    """
    selecionados = []
    for produto in lista:
        if produto['preco'] <= preco_maximo:
            selecionados.append(produto['nome'])
    return selecionados '''

# =============================================================
# EXERCÍCIO 4: O "SISTEMA DE BANCO" (Difícil - O Desafio)
# Objetivo: Integrar tudo o que vimos: Listas de Dicionários + Lógica.
# =============================================================
''' contas_bancarias = [
    {"titular": "Pedro", "saldo": 1500.00},
    {"titular": "Alice", "saldo": 350.00},
    {"titular": "Maria", "saldo": 5000.00},
]

def processar_saque(lista_contas, nome_titular, valor_saque):
    """
    Regras:
    1. Procure o titular na lista (como no exercício do e-mail).
    2. Se achar, verifique se o saldo é suficiente para o saque.
    3. Se tiver saldo: diminua o valor do saldo e retorne "Saque realizado".
    4. Se NÃO tiver saldo: retorne "Saldo insuficiente".
    5. Se não achar o titular: retorne "Conta não encontrada".
    """
    for conta in lista_contas:
        if conta['titular'] == nome_titular:
            if conta['saldo'] >= valor_saque:
                return f"O saque de R${valor_saque} foi realizado com sucesso"
            else:
                return f"Não é possível fazer o saque de R${valor_saque}"
    return "Conta não identificada" '''

# =============================================================
# ÁREA DE TESTES (Descomente para testar)
# =============================================================
''' if __name__ == "__main__":
    #print("--- Teste 1: Palavras ---")
    #print(contar_palavras("Python é a melhor linguagem")) # Esperado: 5
    
    #print("\n--- Teste 2: Formatar Nome ---")
    #print(formatar_usuario(10, "Pedro Capela Gonçalves Silva")) 
    
    #print("\n--- Teste 3: Filtro Baratos ---")
    #print(filtrar_produtos_baratos(produtos_loja, 100.00)) # Esperado: ['MousePad', 'Cabo HDMI']

    #print("\n--- Teste 4: Banco ---")
    #print(processar_saque(contas_bancarias, "Alice", 100)) # Esperado: Saque realizado
    #print(processar_saque(contas_bancarias, "Pedro", 2000)) # Esperado: Saldo insuficiente
    #print(processar_saque(contas_bancarias, 'Jorge', 50000)) # Esperado: Conta não identificada '''

"""
SIMULADO DE CONSOLIDAÇÃO - GEMINI 3 FLASH
Desafios para testar sua autonomia em lógica de programação.
"""

# =============================================================
# DESAFIO 1: O ANALISADOR DE TEMPERATURAS
# Objetivo: Filtrar valores numéricos em uma lista simples.
# =============================================================
''' temperaturas = [25, 32, 18, 40, 15, 28, 42]

def alertar_calor_extremo(lista_temps, limite):
    """
    Deve retornar uma lista apenas com as temperaturas que 
    forem MAIORES que o limite informado.
    """
    # Dica: Crie uma lista vazia e use .append()
    tep_maiores = []
    for temperatura in lista_temps:
        if temperatura > limite:
            tep_maiores.append(temperatura)
    return tep_maiores '''

# =============================================================
# DESAFIO 2: VERIFICADOR DE ACESSO (LOGIN)
# Objetivo: Percorrer dicionários e validar dois campos ao mesmo tempo.
# =============================================================
''' usuarios_db = [
    {"user": "pedro123", "senha": "999"},
    {"user": "alice_dev", "senha": "abc"},
    {"user": "admin", "senha": "123"},
]

def realizar_login(lista_usuarios, usuario_digitado, senha_digitada):
    """
    Deve percorrer a lista e verificar se o 'user' E a 'senha' batem.
    Retornos possíveis: "Acesso concedido" ou "Usuário ou senha incorretos".
    """
    # Dica: Use 'and' no seu 'if' para checar os dois campos
    for login  in lista_usuarios:
        if login['user'] == usuario_digitado and login['senha'] == senha_digitada:
        # Devemos usar as [] após o login para comparar texto com texto (o que está no banco e o que foi digitado), caso feito de outra forma, como o uso de == ele irá comparar se o dicionário é igual a e isso é como comparar uma "pasta de arquivos" com uma "frase solta" — eles nunca serão iguais.            return 'Acesso concedido'
        # O código 'and' exige que duas condições sejam verdadeiras ao mesmo tempo para entrar no código if    
            return 'Acesso concedido'
    return 'Usuário ou senha incorretos' '''

# =============================================================
# DESAFIO 3: CALCULADORA DE COMISSÃO
# Objetivo: Calcular um valor baseado em uma condição de meta.
# =============================================================
''' vendas_vendedores = [
    {"nome": "Carlos", "valor_vendas": 5000},
    {"nome": "Julia", "valor_vendas": 12000},
    {"nome": "Marcos", "valor_vendas": 8000},
]

resultado = []
def calcular_comissao(lista_vendas):
    """
    Regra: 
    - Se vendeu mais de 10.000, comissão é 10% do valor_vendas.
    - Se vendeu 10.000 ou menos, comissão é 5% do valor_vendas.
    
    A função deve retornar uma lista de dicionários contendo:
    [{'nome': '...', 'comissao': ...}, ...]
    """
    comissao = []
    for vendedor in lista_vendas:
        nome = vendedor['nome']
        valor = vendedor['valor_vendas']

        if valor > 10000:
            comissao = valor * 0.10
        else:
            comissao = valor * 0.05
        novo_dado = {
            "Nome": nome,
            "Comissão": comissao
        }
        resultado.append(novo_dado)
    return resultado '''


# =============================================================
# ÁREA DE TESTES (Tente fazer estes prints funcionarem!)
# =============================================================
if __name__ == "__main__":
    #print("--- Teste 1: Temperaturas ---")
    #print(alertar_calor_extremo(temperaturas, 35)) # Esperado: [40, 42]

    #print("\n--- Teste 2: Login ---")
    #print(realizar_login(usuarios_db, "alice_dev", "abc")) # Esperado: Acesso concedido
    #print(realizar_login(usuarios_db, "pedro123", "111")) # Esperado: Usuário ou senha incorretos

    #print("\n--- Teste 3: Comissão ---")
    #print(calcular_comissao(vendas_vendedores))

    