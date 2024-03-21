def criar_matriz(rows, cols):
    matriz = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            elemento = int(input(f"Digite o elemento para [{len(matriz) + 1}][{len(row) + 1}]: "))
            row.append(elemento)
        matriz.append(row)
    return matriz

def imprimir_matriz(matriz):
    for linha in matriz:
        print(" ".join(map(str, linha)))

def somar_matrizes(matriz1, matriz2):
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        print("As matrizes devem ter o mesmo tamanho para realizar a operação de soma.")
        return None
    resultado = []
    for i in range(len(matriz1)):
        linha = []
        for j in range(len(matriz1[0])):
            linha.append(matriz1[i][j] + matriz2[i][j])
        resultado.append(linha)
    return resultado

def subtrair_matrizes(matriz1, matriz2):
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        print("As matrizes devem ter o mesmo tamanho para realizar a operação de subtração.")
        return None
    resultado = []
    for i in range(len(matriz1)):
        linha = []
        for j in range(len(matriz1[0])):
            linha.append(matriz1[i][j] - matriz2[i][j])
        resultado.append(linha)
    return resultado

def multiplicar_matrizes(matriz1, matriz2):
    if len(matriz1[0]) != len(matriz2):
        print("O número de colunas da primeira matriz deve ser igual ao número de linhas da segunda matriz para realizar a operação de multiplicação.")
        return None
    resultado = []
    for i in range(len(matriz1)):
        linha = []
        for j in range(len(matriz2[0])):
            soma = 0
            for k in range(len(matriz2)):
                soma += matriz1[i][k] * matriz2[k][j]
            linha.append(soma)
        resultado.append(linha)
    return resultado

def transpor_matriz(matriz):
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

def main():
    while True:
        print("\n1. Somar Matrizes")
        print("2. Subtrair Matrizes")
        print("3. Multiplicar Matrizes")
        print("4. Transpor Matriz")
        print("5. Parar")

        escolha = int(input("Escolha uma operação: "))

        if escolha in [1, 2, 3]:
            rows = int(input("Digite o número de linhas das matrizes: "))
            cols = int(input("Digite o número de colunas das matrizes: "))
            matriz1 = criar_matriz(rows, cols)
            matriz2 = criar_matriz(rows, cols) if escolha != 4 else None
            
            print("Matriz 1:")
            imprimir_matriz(matriz1)
            if matriz2:
                print("Matriz 2:")
                imprimir_matriz(matriz2)
            if escolha == 1:
                resultado = somar_matrizes(matriz1, matriz2)
                if resultado:
                    print("Resultado da soma:")
                    imprimir_matriz(resultado)
            elif escolha == 2:
                resultado = subtrair_matrizes(matriz1, matriz2)
                if resultado:
                    print("Resultado da subtração:")
                    imprimir_matriz(resultado)
            elif escolha == 3:
                resultado = multiplicar_matrizes(matriz1, matriz2)
                if resultado:
                    print("Resultado da multiplicação:")
                    imprimir_matriz(resultado)
        elif escolha == 4:
            rows = int(input("Digite o número de linhas da matriz: "))
            cols = int(input("Digite o número de colunas da matriz: "))
            matriz = criar_matriz(rows, cols)
            print("Matriz original:")
            imprimir_matriz(matriz)
            matriz_transposta = transpor_matriz(matriz)
            print("Matriz transposta:")
            imprimir_matriz(matriz_transposta)
        elif escolha == 5:
            break
        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()
