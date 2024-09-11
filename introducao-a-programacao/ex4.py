quantidade_reais = int(input("Digite a quantidade de moedas de 1 real: "))
quantidade_cinquenta_centavos = int(input("Digite a quantidade de moedas de 50 centavos: "))
quantidade_vinte_e_cinco_centavos = int(input("Digite a quantidade de moedas de 25 centavos: "))

valor_reais = quantidade_reais * 1.00
valor_cinquenta_centavos = quantidade_cinquenta_centavos * 0.50
valor_vinte_e_cinco_centavos = quantidade_vinte_e_cinco_centavos * 0.25

valor_total = valor_reais + valor_cinquenta_centavos + valor_vinte_e_cinco_centavos

print(f"O valor total das moedas é: R$ {valor_total:.2f}")
