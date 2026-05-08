print ("Bem-Vindo a minha calculadora")
print ("Escolha uma das operações")
print (" 1 - Adição")
print (" 2 - Subtração")
print (" 3 - Multiplicação")
print (" 4 - Divisão")

escolha = int(input ("Digite sua escolha pelo número da opção \n"))

if escolha == 1: 
    print ("Você deseja realizar uma adição, OK \n")
    n1 = float(input("Digite o primeiro valor: \n"))
    n2 = int (input("Digite o segundo valor: \n "))
    total = n1 + n2
    print ("O resultado da sua operação foi:", (total))
    print ( "Obrigado por ultilizar o Sistema Manfredi \n" + "Volte sempre!")

elif escolha == 2:
    print ("Você deseja realizar uma subtração, OK \n")
    n1 = float(input("Digite o primeiro valor: \n"))
    n2 = int (input("Digite o segundo valor: \n "))
    total = n1 - n2
    print ("O resultado da sua operação foi:", (total))
    print ( "Obrigado por ultilizar o Sistema Manfredi \n" + "Volte sempre!")

elif escolha == 3:
    print ("Você deseja realizar uma multiplicação, OK \n")
    n1 = float(input("Digite o primeiro valor: \n"))
    n2 = int (input("Digite o segundo valor: \n "))
    total = n1 * n2
    print ("O resultado da sua operação foi:", (total))
    print ( "Obrigado por ultilizar o Sistema Manfredi \n" + "Volte sempre!")

elif escolha == 4:
    print ("Você deseja realizar uma divisão, OK \n")
    n1 = float(input("Digite o primeiro valor: \n"))
    n2 = int (input("Digite o segundo valor: \n "))
    total = n1 / n2
    print ("O resultado da sua operação foi:", (total))
    print ( "Obrigado por ultilizar o Sistema Manfredi \n" + "Volte sempre!")

else:
    print("Desculpe mas você não escolheu nenhuma das opções acima \n")
    print ("Estamos encerrando o sistema")
    print ("Obrigado")


