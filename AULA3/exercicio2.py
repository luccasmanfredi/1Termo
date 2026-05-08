print ("Vamos calcular a gorjeta de um garçom")
valor_conta = float(input("Digite o valor da conta: R$ "))
porcentagem = int(input("Digite a porcentagem da gorjeta (5 ou 10): "))

if porcentagem == 5 or porcentagem == 10:
    gorjeta = valor_conta * (porcentagem / 100)
    total = valor_conta + gorjeta

    print(f"Gorjeta: R$ {gorjeta:.2f}")
    print(f"Total a pagar: R$ {total:.2f}")
else:
    print("Porcentagem inválida! Escolha 5 ou 10.")