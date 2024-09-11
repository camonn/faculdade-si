ferro = float(input("Digite a quantidade de ferro em kg: "))
ouro = float(input("Digite a quantidade de ouro em kg: "))

quantidade_total = ferro + ouro

percentual_ferro = (ferro / quantidade_total) * 100

if percentual_ferro >= 70:
    print("A liga é adequada para a armadura.")
else:
    print("A liga não é adequada. A porcentagem de ferro deve ser de pelo menos 70%.")
