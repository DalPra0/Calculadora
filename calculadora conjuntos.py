def main():
    # Solicita ao usuário a quantidade de conjuntos
    num_sets = int(input("Quantidade de conjuntos: "))

    # Inicializa uma lista vazia para armazenar os conjuntos
    sets = []

    # Pede ao usuário para inserir os conjuntos
    for i in range(num_sets):
        elements = input(f"Inserir elementos para o conjunto {i + 1} separados por vírgulas: ").split(',')
        sets.append(set(map(int, elements)))

    while True:
        print("\nOperações disponíveis:")
        print("1. União")
        print("2. Interseção")
        print("3. Diferença")
        print("4. Pertinência")
        print("5. Sair")

        choice = int(input("Escolha uma operação (1/2/3/4/5): "))

        if choice == 1:
            union_sets = set.union(*sets)
            print("União dos conjuntos:", union_sets)
        elif choice == 2:
            intersection_sets = set.intersection(*sets)
            print("Interseção dos conjuntos:", intersection_sets)
        elif choice == 3:
            diff_sets = sets[0].difference(*sets[1:])
            print("Diferença dos conjuntos:", diff_sets)
        elif choice == 4:
            element = int(input("Digite o elemento a ser verificado: "))
            for i, s in enumerate(sets):
                if element in s:
                    print(f"O elemento {element} está presente no conjunto {i + 1}")
                    break
            else:
                print(f"O elemento {element} não está presente em nenhum dos conjuntos.")
        elif choice == 5:
            print("Saindo...")
            break
        else:
            print("Escolha inválida. Tente novamente.")


if __name__ == "__main__":
    main()
