print ("Vamos comprar um livro com desconto?")
valor_livro = float(input("Digite o valor do livro: R$ "))
desconto = valor_livro * 0.05
valor_final = valor_livro - desconto


print(f"Desconto (5%): R$ {desconto:.2f}")
print(f"Valor final com desconto: R$ {valor_final:.2f}")