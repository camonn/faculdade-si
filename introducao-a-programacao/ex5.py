agua_disponivel = float(input("Digite a quantidade de água disponível em litros: "))
distancia = float(input("Digite a distância até o oásis em quilômetros: "))

agua_necessaria = distancia * 2

if agua_disponivel >= agua_necessaria:
    print("A quantidade de água é suficiente para chegar ao oásis.")
else:
    print("A quantidade de água não é suficiente. Você precisa de mais água.")
