# manipulacao_arquivos = ("Manipulação de arquivos e texto com python")

# print (manipulacao_arquivos.upper()) # Maiúsculas
# print(manipulacao_arquivos.lower()) # Minúsculas
# print(manipulacao_arquivos.strip()) # Remove espaços em branco
# print(manipulacao_arquivos.split()) # Divide a string em uma lista de palavras
# print(manipulacao_arquivos.replace("Python", "Java")) # Substitui "Python" por "Java"
# print(manipulacao_arquivos.replace(" ", "_")) # Substitui "Espaço" por "_"
# print(manipulacao_arquivos.count("a")) # Conta quantas vezes a letra "a" aparece na string
# print(manipulacao_arquivos.count("Python")) # Conta quantas vezes a palavra "Python" aparece na string
# print(manipulacao_arquivos.upper().count("PYTHON")) # Conta quantas vezes a letra "PYTHON" aparece na string e converte para maiúsculas
# print(manipulacao_arquivos.strip().count("python")) # Conta quantas vezes a letra "python" aparece na string, removendo os espaços em branco
# print(manipulacao_arquivos.find("Python")) # Retorna a posição da primeira ocorrência da palavra "Python" na string

# print(manipulacao_arquivos.title()) # Converte a primeira letra de cada palavra para maiúscula
# print(manipulacao_arquivos.capitalize()) # Converte a primeira letra da string para maiúscula e o restante para minúscula
# print(manipulacao_arquivos.swapcase()) # Converte as letras maiúsculas para minúsculas e vice-versa
# print(manipulacao_arquivos.center(50, "*")) # Centraliza a string e preenche com "*" até atingir 50 caracteres
#--------------------------------------------------------------------------------------------------------------------------------------------------#
# Exercicio 1:
# Crie um algoritmo onde peça para inserir uma frase e deixa-a formatada com maiuscula e acrescente uma contagem de cada frase.

# frase = input("Digite uma frase: ")
# print(frase.upper())
# print(f"Quantidade de caracteres: {len(frase)}") 

# frase_usuario = input("Inserir frase :) ")
# print(frase_usuario.upper())
# print(frase_usuario.count(frase_usuario))
# print(frase_usuario.count(""))
#--------------------------------------------------------------------------------------------------------------------------------------------------#

# with open ("arquivo.txt", "w") as exemplo:
#     exemplo.write("Exemplo de Clean Code - Aula 8\n")
# # w = write - Escreve no arquivo, se o arquivo já existir, ele irá sobrescrever o conteúdo.
# with open ("arquivo.py", "w") as python:
#     python.write('print("Exemplo de arquivo Python")')

# with open ("arquivo.txt", "r") as exemplo:
#     conteudo = exemplo.read()
#     print(conteudo)
# # r = read - Lê o conteúdo do arquivo, se o arquivo não existir, ele irá gerar um erro.

# with open ("arquivo.py","a") as python:
#     python.write('\nprint("Continuando a escrever no arquivo Python")')
#     python.write('\nprint("Mais uma linha no arquivo Python")')
# a = append - Adiciona conteúdo ao final do arquivo, se o arquivo não existir, ele irá criar um novo arquivo.

# Manipulação de Sistema Operacional
import os #Biblioteca para manipulação de arquivos e diretórios

# Criando um diretório
# os.mkdir("Teste")

# Renomear pastas
# os.rename("Teste","Aulas")

# Excluir pastas
# os.rmdir("Aulas")

# Criar arquivos
# os.mknod("teste.txt")
# os.touch("aula.txt")

# Listagem de Diretorios
# print(os.listdir()) # Lista os arquivos e pastas do diretório atual

# print(os.listdir("..")) # Lista os arquivos e pastas do diretório pai
# print(os.listdir("C:\\")) # Lista os arquivos e pastas do diretório raiz do C
#------------------------------------------------------------------------------------------------------------------------------#

# Exercício 2 
# Crie um algoritimo para a criação de um arquivo que irá desligar o computador. 

with open ("desligar.bat" , "w") as desligar:
    desligar.write('shutdown /s /t 10 /c "Sextou! Pode descansar"')
