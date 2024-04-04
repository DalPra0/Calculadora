print("")
print("Lucas Dal Pra Brascher, Guilherme Kai - 1C - Conjuntos complexos")
print("")

num_sets = int(input("Quantidade de conjuntos: "))

sets = []

for i in range(num_sets):
    elements = input(f"Inserir elementos para o conjunto {i + 1} separados por vírgulas: ").split(',')
    sets.append(set(map(int, elements)))



while True:

    print("1 - Operação com os conjuntos, 2 - Verificar alguma coisa dos conjuntos, 3 - sair")
    esc = int(input("Baseado no exemplo acima, digite o que quer fazer: ")) 

    if esc == 1:
        print("\nOperações disponíveis:")
        print("1. União")
        print("2. Interseção")
        print("3. Diferença")
        print("4. Pertinência")

        choice = int(input("Escolha uma operação (1/2/3/4): "))

        if choice == 1:
            quant_conj = int(input("Quantos conjuntos voce quer usar? "))
            for i in quant_conj:
                conj{i} = int(input(""))
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