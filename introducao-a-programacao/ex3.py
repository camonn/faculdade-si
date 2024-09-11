tipo_animal = input("Seu animal favorito é mamífero ou réptil? ").strip().lower()

if tipo_animal == "mamífero":
    print("Seu animal favorito é um cachorro!")
elif tipo_animal == "réptil":
    print("Seu animal favorito é uma tartaruga!")
else:
    print("Resposta não reconhecida. Por favor, responda com 'mamífero' ou 'réptil'.")
