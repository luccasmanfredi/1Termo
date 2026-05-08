# Lista de temperaturas lidas pelo sensor por minuto 
# leituras = [70, 75, 82, 98, 110, 85, 80]

# for temp in leituras:
#    if temp > 100:
#     print(f"CRÍTICO: {temp}°C detectado! Acionando parada de emergência.")
#     break # O loop para aqui NÃo lê os próximos valores (85 e 80)
#    print (f"Temperatura está em {temp}°C. Operação normal.")

# print ("Sistema desligado. Aguarde manutenção.")
#---------------------------------------------------------------------------------------------------------#

# Cenário 2 
# Adicionar uma outra condição para a temperatura abaixo de 50 e quando chegar até 10 parar

# leituras = [70, 75, 82, 98, 110, 85, 80]
# baixos = [50, 55, 52, 30, 20, 15, 10]

# todas_leituras = leituras + baixos

# for temp in todas_leituras:
# 	if temp > 100:
# 		print(f"CRÍTICO: {temp}°C detectado! Acionando parada de emergência.")
		
# 	elif temp <= 10:
# 		print(f"BAIXA EXTREMA: {temp}°C detectado! Parando o sistema por segurança.")
		
# 	elif temp < 50:
# 		print(f"ALERTA: temperatura baixa ({temp}°C). Verificar aquecimento.")
# 	else:
# 		print(f"Temperatura está em ({temp}°C). Operação normal.")

# print("Sistema desligado. Aguarde manutenção.")
#---------------------------------------------------------------------------------------------------------#

# materiais = ["metal", "metal", "plastico", "metal", "vidro", "metal"]
# for peca in materiais:
#     if peca != "metal":
#         print(f"Aviso: Peça de {peca} detectada. Desviando para descarte...")
#         continue # Pula o restante do código abaixo e vai para a próxima peça
    
#     # Este código só roda se a peça for metal 
#     print (f"Processando peça de {peca}. Furando e polindo...") 
    
#     print ("Fim do lote de produção.")
#---------------------------------------------------------------------------------------------------------#

# Exercício 1 
# Tente criar um código que conte de 1 a 10, mas use o continue para não imprimir o número 5 (simulando uma falha de sensor específica no item 5)

# from time import sleep
# for num in range(1,11):
#     if num == 5:
#         print(f"Falha ao imprimir o nº {num}")
#         sleep(1.8)
#         continue
#     print(f"Listando números {num}")
#     sleep(2)
# print("Fim!")
#---------------------------------------------------------------------------------------------------------#

# Exercício 2 
# Simule um semáforo com parada para cada cor. Determine um tempo que deseja para quando mudar para tal cor ele represente uma pausa. 

# from time import sleep

# while True:
#     print(" VERDE - Siga")
#     sleep(5)

#     print(" AMARELO - Atenção")
#     sleep(2)

#     print(" VERMELHO - Pare")
#     sleep(4)
#---------------------------------------------------------------------------------------------------------#

# Exercício 3 
#Uma fábrica tem 5 máquinas. Peça ao usuário (via input dentro do loop) o consumo em kWh de cada uma das 5 máquinas. Ao final do loop, o programa deve exibir o consumo total da fábrica.

# total = 0.0

# for i in range(1, 6):
#     consumo = float(input(f"Digite o consumo da máquina {i} (em kWh): "))
#     total += consumo

# print(f"Consumo total da fábrica: {total:.2f} kWh")
#---------------------------------------------------------------------------------------------------------#
# Exercício 4 - Identificador de Peças Defeituosas (for + if)
# Percorra uma lista de medidas de peças: 
# medidas = [50.1, 49.8, 52.0, 50.0, 48.5].
# O padrão de qualidade aceita apenas peças com exatamente 50.0 ou mais.
# Use um for para ler a lista e, para cada peça, diga se ela está "Aprovada" ou "Rejeitada".
 
# medidas = [50.1, 49.8, 52.0, 50.0, 48.5]
# for pecas in medidas:
#     if pecas > 50:
#         print(f"Peça {pecas} Aprovada.. :)")
#     else: 
#         print (f"Peça {pecas} Rejeitada")
#---------------------------------------------------------------------------------------------------------#

# Exercício 5 - Uma balança industrial está pesando um lote de 6 sacos de insumos. O peso ideal de cada saco é 50kg, mas o sistema aceita variações.

# sacos = [49.5, 50.0, 51.2, 48.9, 50.5, 47.8]

# min_aceito = 49.0
# max_aceito = 51.0

# for peso in sacos:
#     if min_aceito <= peso <= max_aceito:
#         print(f"Saco com peso {peso} kg: Aceitável")
#     else:
#         print(f"Saco com peso {peso} kg: Rejeitado - Fora do limite aceitável")
#---------------------------------------------------------------------------------------------------------#

# O Desafio: Gestão de Ciclo Térmico
# Você deve criar um programa que monitore a temperatura de uma estufa que processa um lote de 5 peças.
# Regras do Sistema:
# O programa deve rodar em um loop até que 5 peças válidas sejam processadas.
# Para cada peça, peça ao usuário a temperatura atual (input).
# Filtro de Erro (continue): Se o usuário digitar uma temperatura negativa, exiba "Erro de leitura no sensor" e use o continue para pedir a temperatura novamente (essa leitura não conta como peça processada).
# Parada de Emergência (break): Se a temperatura for maior que 150°C, o sistema deve exibir "ALERTA CRÍTICO: Risco de Explosão!", interromper o loop imediatamente e encerrar o programa.

# O Desafio: Gestão de Ciclo Térmico (estufa)
# Objetivo: processar 5 peças válidas, mas parar se a temperatura passar de 150°C

pecas_validas = 0

while pecas_validas < 5:
    temp = float(input(f"Digite a temperatura da peça {pecas_validas + 1} (°C): "))

    
    if temp < 0:
        print("Erro de leitura no sensor")
        continue  
    
    if temp > 150:
        print("ALERTA CRÍTICO: Risco de Explosão!")
        break 

    print("Peça processada com sucesso!")
    pecas_validas += 1

print("Programa encerrado.")
#---------------------------------------------------------------------------------------------------------#

# Exercício 7: Sistema Inteligente de Manutenção
# Crie um programa que receba dois dados: a pressão atual (float) e as horas de uso acumuladas (int) de uma turbina.
# O programa deve classificar o estado da máquina seguindo esta hierarquia:
# Crítico (Prioridade 1): Se a pressão for maior que 100 OU as horas de uso forem maiores que 10.000.
# Mensagem: "PARADA IMEDIATA: Risco de falha catastrófica."
# Alerta (Prioridade 2): Se a pressão estiver entre 80 e 100 (inclusive).
# Mensagem: "MANUTENÇÃO AGENDADA: Pressão acima do ideal."
# Monitoramento (Prioridade 3): Se as horas de uso forem entre 8.000 e 10.000.
# Mensagem: "AVISO: Máquina aproximando-se da revisão de 10k horas."
# Normal: Para qualquer outro caso que não se encaixe nos acima.
# Mensagem: "SISTEMA OPERAL: Todos os parâmetros dentro da normalidade."

 


pressao = float(input("Pressão atual: "))
horas = int(input("Horas de uso: "))


if pressao > 100 or horas > 10000:
    print("PARADA IMEDIATA: Risco de falha catastrófica.")


elif pressao >= 80 and pressao <= 100:
    print("MANUTENÇÃO AGENDADA: Pressão acima do ideal.")


elif horas >= 8000 and horas <= 10000:
    print("AVISO: Máquina aproximando-se da revisão de 10k horas.")

else:
    print("SISTEMA OPERACIONAL: Todos os parâmetros dentro da normalidade.")