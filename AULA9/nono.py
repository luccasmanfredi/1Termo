# Exercício 1 incorreto

# idade = input ("Digite sua idade: ")
# if idade >= "18":
#     print("Você é maior de idade.")
#------------------------------------------#
# Exercício correto

# idade = int(input ("Digite sua idade: "))
# if idade >= 18:
#     print("Você é maior de idade.")
#-------------------------------------------------------------------#
# Melhorado

# print ("Vamos verificar se você é maior ou menor de idade.")
# idade = int(input ("Digite sua idade: "))
# if idade >= 18:
#     print("Você é maior de idade.")
# else: 
#     print("Você é menor de idade.")

# No exemplo incorreto o código estava faltando a função int() para converter a entrada do usuário em um número inteiro, e também estava faltando a estrutura do else para tratar o caso em que a idade é menor que 18.
#---------------------------------------------------------------#
# Exercício 2 incorreto

# nome = "Mariana"
# print ("Seja bem-vinda, nome!")
#---------------------------------------------------------------#
# Exercício correto

# nome = "Mariana"
# print (f"Seja bem-vinda, {nome}!")
#------------------------------------------------------------------------#
# Melhorado

# nome = "Mariana"
# print (f"Seja bem-vinda, {nome}!")
# if nome == "Visitante": 
#     print("Olá, visitante!")

# No exemplo incorreto o código estava faltando a letra f antes da string para indicar que é uma f-string, e também estava faltando as chaves {} para incluir a variável nome dentro da string.
#---------------------------------------------------------------#
# Exercício 3 incorreto

# numero = 10
# if numero > 5:
# print("O número é maior que cinco.")
# else: 
# print("O número é menor ou igual a cinco.")
#---------------------------------------------------------------#
# Exercício correto 

# numero = int(input("Digite um número: "))
# if numero > 5:
#     print("O número é maior que cinco.")
# else: 
#     print("O número é menor ou igual a cinco.")
#---------------------------------------------------------------#
# Melhorado

# numero = int(input("Digite um número: "))
# if numero > 5:
#     print("O número é maior que cinco.")
# elif numero == 5:
#     print("O número é igual a cinco.")
# else: 
#     print("O número é menor que cinco.")

# No exemplo incorreto o código estava faltando a indentação das linhas do print dentro do if e do else, o que causaria um erro de sintaxe. A indentação é importante para indicar quais linhas pertencem a cada bloco de código.
#---------------------------------------------------------------#
# Exercício 4 incorreto

# usuario = "aluno123"
# if usuario == "aluno123"
# print ("Login realizado com sucesso.")
#---------------------------------------------------------------#
# Exercício correto

# usuario = input("Digite seu nome de usuário: ")
# if usuario == "aluno123":
#     print("Login realizado com sucesso.")

#---------------------------------------------------------------#
# Melhorado

# usuario = input("Digite seu nome de usuário: ")
# if usuario == "aluno123":
#     print("Login realizado com sucesso.")
# else: 
#     print("Usuário incorreto. Tente novamente.")

# No exemplo incorreto o código estava faltando os dois pontos (:) no final da linha do if, e também estava faltando a indentação da linha do print.
#---------------------------------------------------------------#
# Exercício 5 incorreto

# clima = "ensolarado"
# if clima = "chuvoso":
#     print("Leve um guarda-chuva.")
#---------------------------------------------------------------#
# Exercício correto

# clima = input("Como está o clima hoje? (ensolarado/chuvoso): ")
# if clima == "chuvoso":
#     print("Leve um guarda-chuva.")
# else: 
#     print("Aproveite o dia ensolarado!")
#---------------------------------------------------------------#
# Melhorado

# clima = input("Como está o clima hoje? (ensolarado/chuvoso/nublado): ")
# if clima == "chuvoso":
#     print("Leve um guarda-chuva.")
# elif clima == "nublado":
#     print("Pode ser que chova, leve um guarda-chuva por precaução.")
# else: 
#     print("Aproveite o dia ensolarado!")

# No exemplo incorreto o código estava usando o operador de atribuição (=) em vez do operador de comparação (==) no if, e também estava faltando a estrutura do else para tratar o caso em que o clima não é chuvoso.
#---------------------------------------------------------------#

# Exercício 6

# pontos = 50 
# print ("Parabéns! Você fez" + pontos + "pontos.")
#---------------------------------------------------------------#
# Exercício correto

# pontos = 50
# print (f"Parabéns! Você fez {pontos} pontos.")
#---------------------------------------------------------------#
# Melhorado

# print ("Vamos calcular seus pontos.")
# pontos = int(input("Digite a quantidade de pontos que você fez: "))
# print (f"Parabéns! Você fez {pontos} pontos.")

# No exemplo incorreto o código estava tentando concatenar uma string com um número inteiro, o que causaria um erro. A solução é usar uma f-string para incluir a variável pontos dentro da string de forma correta.
#---------------------------------------------------------------#
# Exercício 7 incorreto

# O sistema deve dar "Ecelente" para as notas 9 ou 10. 

# nota = 9.5 
# if nota >= 7:
#     print("Aprovado.")
# elif nota >= 9:
#         print("Excelente.")
#---------------------------------------------------------------#
# Exercício correto

# nota = float(input("Digite sua nota: "))
# if nota >= 9:
#     print("Excelente.")
# elif nota >= 7:
#     print("Aprovado.")
#---------------------------------------------------------------#
# Melhorado

# nota = float(input("Digite sua nota: "))
# if nota >= 9:
#     print("Excelente.")
# elif nota >= 7:
#     print("Aprovado.")
# else:
#     print("Reprovado.")

# No exemplo incorreto o código estava verificando primeiro se a nota era maior ou igual a 7, o que faria com que as notas 9 e 10 fossem classificadas como "Aprovado" em vez de "Excelente". A solução é verificar primeiro se a nota é maior ou igual a 9, e depois verificar se é maior ou igual a 7.
#---------------------------------------------------------------#
# Exercício 8 incorreto

# Objetivo: Mostrar na tela os números 1, 2, 3, 4 e 5 

# for i in range(5):
#     print(i)
#---------------------------------------------------------------#
# Exercício correto

# for i in range(1, 6):
#     print(i)
#---------------------------------------------------------------#
# Melhorado

# n = int(input("Digite um número: "))
# for i in range(1, n + 1):
#     print(i)

# No exemplo incorreto o código estava usando range(5), o que geraria os números de 0 a 4. Para gerar os números de 1 a 5, é necessário usar range(1, 6), onde o primeiro número é o início da sequência e o segundo número é o final da sequência (exclusivo).
#---------------------------------------------------------------#
# Exercício 9 incorreto

# tentativas = 1
# while tentativas <= 3: 
#     print("Tentando conectar...")
# O código deveria parar após 3 tentativas.
#---------------------------------------------------------------#
# Exercício correto

# tentativas = 1
# while tentativas <= 3: 
#     print("Tentando conectar...")
#     tentativas += 1
#---------------------------------------------------------------#
# Melhorado

# tentativas = 1
# while tentativas <= 3:
#     print("Tentando conectar...")
#     resposta = input("A conexão foi bem-sucedida? (s/n): ")
#     if resposta.lower() == 's':
#         print("Conexão estabelecida com sucesso!")
#         break
#     else:
#         print("Falha na conexão. Tentando novamente...")
#     tentativas += 1

# No exemplo incorreto o código estava faltando a linha tentativas += 1 dentro do loop while, o que faria com que a variável tentativas nunca aumentasse e o loop se tornasse infinito. A solução é adicionar essa linha para incrementar o número de tentativas a cada iteração do loop.
#---------------------------------------------------------------#
# Exercício 10 incorreto

# O programa deve pedir a senha até que o usuário digite "python123"


#---------------------------------------------------------------#
# Exercício correto

# senha = ""
# while senha != "python123":
#     senha = input("Digite a senha secreta: ")
# print("Acesso concedido.")
#---------------------------------------------------------------#
# Melhorado

# senha = ""
# while senha != "python123":
#     senha = input("Digite a senha secreta: ")
#     if senha != "python123":
#         print("Senha incorreta. Tente novamente.")
# print("Acesso concedido.")

# No exemplo incorreto o código estava faltando a estrutura do loop while para continuar pedindo a senha até que o usuário digitasse a senha correta. A solução é usar um loop while que verifica se a senha digitada é diferente de "python123", e dentro do loop pedir ao usuário para digitar a senha. Quando o usuário digitar a senha correta, o loop será encerrado e a mensagem "Acesso concedido." será exibida.