def exibir_menu():
    print("\n--- Lista de Compras ---")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Exibir lista")
    print("4. Sair")
    return input("Escolha uma opção: ")

def adicionar_item(lista):
    nome = input("Digite o nome do item: ")
    categoria = input("Digite a categoria do item: ")
    lista.append((nome, categoria))
    print(f"Item '{nome}' da categoria '{categoria}' adicionado com sucesso!")

def remover_item(lista):
    nome = input("Digite o nome do item a ser removido: ")
    for item in lista:
        if item[0] == nome:
            lista.remove(item)
            print(f"Item '{nome}' removido com sucesso!")
            return
    print(f"Item '{nome}' não encontrado na lista.")

def exibir_lista(lista):
    if not lista:
        print("A lista de compras está vazia.")
    else:
        print("\n--- Lista de Compras ---")
        for item in lista:
            print(f"Item: {item[0]}, Categoria: {item[1]}")
    
def main():
    lista_compras = []
    while True:
        opcao = exibir_menu()
        if opcao == '1':
            adicionar_item(lista_compras)
        elif opcao == '2':
            remover_item(lista_compras)
        elif opcao == '3':
            exibir_lista(lista_compras)
        elif opcao == '4':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Por favor, escolha novamente.")

if __name__ == "__main__":
    main()
