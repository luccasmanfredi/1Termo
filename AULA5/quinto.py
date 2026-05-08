# O laço 'for' (Repetições Determinadas)
# Use o 'for' quando você sabe exatamente quantas vezes algo deve acontecer (Como ler 10 sensores ou processar uma lista de peças)
# Exemplo: Relatório de Produção Diária 
# Imagine que você tem uma meta de produzir 5 lotes e quer numerar cada um: 
 
 # Exemplo 1 
 
# for lote in range (1, 6):
#     print (f"Processando lote número {lote},..")
#     print ("Qualidade verificada. [OK]")
#     print ("Produção do dia finalizada!")
#--------------------------------------------------------------------------------------------------------------------------------#
    
    # Imagine que você queira atingir uma meta de produção de 5 carros e numera-los
    
# for carros in range (1,6):
#         print (f"Produção de carros de luxo diária {carros}...")
#----------------------------------------------------------------------------------------------------------------------------------#

## Exemplo 2
# Contar até 4
# for i in range (5):
#     print (i)
#------------------------------------------------------------------------------------------------------------------------------------#

## Exemplo 3

# pecas = ["Engrenagem", "Eixo", "Rolamento", "Parafuso", "Martelo"]
# tipos_pecas = ["Barra Dentada", "Porca do Eixo", "Anel Externo", "Parafuso Phillips", "Martelo Cabeça Chata"]

# for item in pecas:
#     print (f"Item em estoque: {item}")
# for tipos in tipos_pecas:
#     print (f"Minha lista de tipos de peças {tipos_pecas}")
#---------------------------------------------------------------------------------------------------------------------------------------#

# Exemplo 4 
# Imagine a seguinte situação, gostaria de ter um menu onde pudesse perguntar qual opção você deseja e a partir da seleção ele listar os produtos 

# print ("Loja de peças Manfredi")
# print ("Bem-Vindo ao nosso sistema")
# print ("Escolha uma das opções")
# print ("1 - Peças")
# print ("2 - Tipos de Peças ")

# tipos_pecas = ["Barra Dentada", "Porca do Eixo", "Anel Externo", "Parafuso Phillips", "Martelo Cabeça Chata"]
# pecas = ["Engrenagem", "Eixo", "Rolamento", "Parafuso", "Martelo"]
# opcao = int(input("Digite sua opção de pesquisa: "))

# if opcao == 1:
#     for item in pecas: 
#         print (f"Item em estoque: {item}")
#         print ("Fim da lista")
    
# elif opcao == 2:
#     for item2 in pecas: 
#         print (f"Item em estoque: {item2}")
#         print ("Encerrando a lista")
        
# else: 
#     print ("Encerrando sistema")
    
#------------------------------------------------------------------------------------------------------------------------------------------#

# Exercício 1
## 1. Contador de Produção (for)
## uma esteira processa 10 peças por ciclo. Crie um programa que use um for para contar de 1 a 10 e, para cada número, imprima: "Peça n° X processada com sucesso". No final, exiba "Ciclo de produção concluído"

# for ciclo in range (1, 11):
#     print (f"Peça N°", [ciclo], "Processada com sucesso...")
# print ("Ciclo de produção concluído")
#-----------------------------------------------------------------------------------------------------------------------------------------------------#

# Exercício 2 
# Imagine a produção de frutas em uma feira. Desejo apresentar frutas banana, manga, melancia, abacaxi. Com uma quantidade de 10 bananas, 5 mangas, 10 melancias e 13 abacaxi.

# frutas = ["banana", "manga", "melancia", "abacaxi"]
# quantidades = [10, 5, 10, 13]

# for lote in range(1, 6):
#     print(f"Processando lote número {lote}...")

#     for i in range(len(frutas)):
#         fruta = frutas[i]
#         quantidade = quantidades[i]

#         print(f"Possuímos {fruta} até {quantidade} unidades:")
#         for n in range(1, quantidade + 1):
#             print(f"{fruta} {n}")

# print("Quantidade verificada. [OK]")
# print("Produção do dia finalizada!")
#----------------------------------------------------------------------------------------------------------------------------------------#

# Exercício 3 
# Montar uma tabuada inicialmente pode ser com um valor fixo 

# SIMPLES 
# numero = 7

# for i in range(1, 11):
# 	print(f"{numero} x {i} = {numero * i}")
 
# COMPLEXA 

# numero = int(input("Digite um número para ver a tabuada: "))

# for i in range(1, 11):
# 	print(f"{numero} x {i} = {numero * i}")

#----------------------------------------------------------------------------------------------------------------------------------------#

# O laço while (Repetições Indeterminadas)
# Use o while quando você não sabe quando vai parar. Ele depende de uma condição (como um sensor de segurança ou um borão de emergência)
# Exemplo: Monitor de Temperatura (Loop infinito controlado)

# Repete enquanto a temperatura está segura
# Início 

# import time 
# temperatura = 25 
# while temperatura < 40:
#     print (f"Temperatura atual: {temperatura} °C. Sistema operando...")
#     time.sleep(2)
#     temperatura += 3 # Simulando o aquecimento da máquina 
# print ("ALERTA! Temperatura atingiu o limite. Desligar o motor...")
#----------------------------------------------------------------------------------------------------------------------------------------#

# Exemplo 2: Menu de Interação 
# (!= diferente ) 
# (lower é minusculo) 
# (upper é maiusculo )
# opcao = ""

# while opcao != "sair" and "SAIR":
#     opcao = input  ("Digite a leitura do sensor ou 'sair' para fechar: ").lower() 
#     if opcao != "sair" and "SAIR":
#         print (f"Dado '{opcao}' registrado no banco de dados.")
# print ("Sistema encerrado")

# and e or
# and comparações verdadeiras e iguais 
# or comparações verdadeiras e não iguais
#----------------------------------------------------------------------------------------------------------------------------------------#

# Exercício 4 
# Monitor de pressão crítica (while)
# Crie um simulador onde o usuário deve digitar a pressão atual de um compressor.
# Enquanto a pressão for menor que 100 PSI, o programa continua pedindo a nova leitura 
# Assim que o usuário digitar um valor maior ou igual a 100, o loop para e exibe a mensagem: "ALERTA: Pressão crítica atingida! Desligando sistema." 

# import time 
# temperatura = float(input("Digite a temperatura inicial (°C): "))
# limite = 80.0
# aumento = 2.5  

# while temperatura < limite:
#     print(f"Temperatura atual: {temperatura:.1f} °C")
#     time.sleep(1)
#     temperatura += aumento

# print(f"Temperatura atual: {temperatura:.1f} °C")
# print("ALERTA: Temperatura crítica atingida! Desligando sistema.")
#----------------------------------------------------------------------------------------------------------------------------------------#

# Exercício 5
# Criar um menu de opções com 4 itens ex: Escolher series apresente sua escolha de series das outras três.
# Qualquer opcao diferente sair do menu.

continuar = True
while continuar: 
    print("\n=== MENU DE SÉRIES ===")
print("[1] Stranger Things")
print("[2] The Last of Us")
print("[3] Senhor dos Anéis")
print("[4] Round 6")

opcao = input("Escolha uma opção (1-4): ")

if opcao == "1":
    print("Você escolheu: Stranger Things")
    print("Aproveite!")

elif opcao == "2":
    print("Você escolheu: The Last of Us")
    print("Aproveite!")

elif opcao == "3":
    print("Você escolheu: Senhor dos Anéis")
    print("Aproveite!")

elif opcao == "4":
    print("Você escolheu: Round 6")
    print("Aproveite!")

else:
    print("Opção inválida!")