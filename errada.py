import math
import matplotlib.pyplot as plt
import numpy as np

def verificar_subconjunto_proprio(A, B):
    if A < B:
        print("A é subconjunto próprio de B")
    else:
        print("A não é subconjunto próprio de B")

def uniao_conjuntos(A, B):
    resultado = A | B
    print(f"União: {resultado}")

def intersecao_conjuntos(A, B):
    resultado = A & B
    print(f"Interseção: {resultado}")

def diferenca_conjuntos(A, B):
    resultado = A - B
    print(f"Diferença: {resultado}")

def menu_conjuntos():
    while True:
        print("\nMenu Conjuntos Numéricos")
        print("1. Verificar se A é subconjunto próprio de B")
        print("2. Realizar operação de União")
        print("3. Calcular interseção")
        print("4. Calcular diferença")
        print("5. Voltar")
        opcao = input("Escolha uma opção: ")
        if opcao == '5':
            break
        A = set(map(int, input("Informe os elementos do conjunto A separados por espaço: ").split()))
        B = set(map(int, input("Informe os elementos do conjunto B separados por espaço: ").split()))
        if opcao == '1':
            verificar_subconjunto_proprio(A, B)
        elif opcao == '2':
            uniao_conjuntos(A, B)
        elif opcao == '3':
            intersecao_conjuntos(A, B)
        elif opcao == '4':
            diferenca_conjuntos(A, B)
        else:
            print("Opção inválida. Tente novamente.")

def calcular_raizes(a, b, c):
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"Raízes reais: x1 = {x1}, x2 = {x2}")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Raiz única: x = {x}")
    else:
        real = -b / (2*a)
        imag = math.sqrt(-delta) / (2*a)
        print(f"Raízes complexas: x1 = {real} + {imag}i, x2 = {real} - {imag}i")

def calcular_valor_funcao_segundo_grau(a, b, c, x):
    valor = a*x**2 + b*x + c
    print(f"f({x}) = {valor}")

def calcular_vertice(a, b, c):
    xv = -b / (2*a)
    yv = a*xv**2 + b*xv + c
    tipo = "mínimo" if a > 0 else "máximo"
    print(f"Vértice: ({xv}, {yv}), Tipo: {tipo}")

def gerar_grafico_segundo_grau(a, b, c):
    x = np.linspace(-10, 10, 400)
    y = a*x**2 + b*x + c
    plt.plot(x, y)
    plt.title(f'Gráfico de f(x) = {a}x^2 + {b}x + {c}')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.show()

def menu_funcoes_segundo_grau():
    while True:
        print("\nMenu Funções do Segundo Grau")
        print("1. Calcular raízes")
        print("2. Calcular função em x pedido")
        print("3. Calcular Vértice")
        print("4. Gerar gráfico")
        print("5. Voltar")
        opcao = input("Escolha uma opção: ")
        if opcao == '5':
            break
        a = float(input("Informe o coeficiente a: "))
        b = float(input("Informe o coeficiente b: "))
        c = float(input("Informe o coeficiente c: "))
        if opcao == '1':
            calcular_raizes(a, b, c)
        elif opcao == '2':
            x = float(input("Informe o valor de x: "))
            calcular_valor_funcao_segundo_grau(a, b, c, x)
        elif opcao == '3':
            calcular_vertice(a, b, c)
        elif opcao == '4':
            gerar_grafico_segundo_grau(a, b, c)
        else:
            print("Opção inválida. Tente novamente.")

def verificar_crescimento(a, b):
    if b > 1:
        print("A função é crescente.")
    elif 0 < b < 1:
        print("A função é decrescente.")
    else:
        print("Valor de b inválido para uma função exponencial.")

def calcular_valor_funcao_exponencial(a, b, x):
    valor = a * (b ** x)
    print(f"f({x}) = {valor}")

def gerar_grafico_exponencial(a, b):
    x = np.linspace(-10, 10, 400)
    y = a * (b ** x)
    plt.plot(x, y)
    plt.title(f'Gráfico de f(x) = {a} * {b}^x')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.show()

def menu_funcoes_exponenciais():
    while True:
        print("\nMenu Funções Exponenciais")
        print("1. Verificar se é crescente ou decrescente")
        print("2. Calcular função em x pedido")
        print("3. Gerar gráfico")
        print("4. Voltar")
        opcao = input("Escolha uma opção: ")
        if opcao == '4':
            break
        a = float(input("Informe o coeficiente a: "))
        b = float(input("Informe o coeficiente b: "))
        if opcao == '1':
            verificar_crescimento(a, b)
        elif opcao == '2':
            x = float(input("Informe o valor de x: "))
            calcular_valor_funcao_exponencial(a, b, x)
        elif opcao == '3':
            gerar_grafico_exponencial(a, b)
        else:
            print("Opção inválida. Tente novamente.")

def imprimir_matriz(matriz):
    for linha in matriz:
        print('[', end=' ')
        for elem in linha:
            print(f'{elem}', end=' ')
        print(']')

def calcular_determinante_2x2(matriz):
    return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]

def calcular_determinante_3x3(matriz):
    return (matriz[0][0] * matriz[1][1] * matriz[2][2] +
            matriz[0][1] * matriz[1][2] * matriz[2][0] +
            matriz[0][2] * matriz[1][0] * matriz[2][1] -
            matriz[0][2] * matriz[1][1] * matriz[2][0] -
            matriz[0][0] * matriz[1][2] * matriz[2][1] -
            matriz[0][1] * matriz[1][0] * matriz[2][2])

def transpor_matriz(matriz):
    transposta = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]
    return transposta

def multiplicar_matrizes(A, B):
    if len(A[0]) != len(B):
        return None
    result = [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
    return result

def menu_matrizes():
    while True:
        print("\nMenu Matrizes")
        print("1. Imprimir matriz")
        print("2. Calcular determinante (2x2 ou 3x3)")
        print("3. Multiplicar matrizes")
        print("4. Matriz transposta")
        print("5. Voltar")
        opcao = input("Escolha uma opção: ")
        if opcao == '5':
            break
        linhas = int(input("Informe o número de linhas da matriz: "))
        colunas = int(input("Informe o número de colunas da matriz: "))
        matriz = []
        for i in range(linhas):
            linha = list(map(int, input(f"Informe os elementos da linha {i + 1} separados por espaço: ").split()))
            matriz.append(linha)
        if opcao == '1':
            imprimir_matriz(matriz)
        elif opcao == '2':
            if linhas == colunas:
                if linhas == 2:
                    det = calcular_determinante_2x2(matriz)
                    print(f"Determinante: {det}")
                elif linhas == 3:
                    det = calcular_determinante_3x3(matriz)
                    print(f"Determinante: {det}")
                else:
                    print("Somente determinantes de matrizes 2x2 ou 3x3 são suportados.")
            else:
                print("A matriz não é quadrada.")
        elif opcao == '3':
            linhas_b = int(input("Informe o número de linhas da segunda matriz: "))
            colunas_b = int(input("Informe o número de colunas da segunda matriz: "))
            matriz_b = []
            for i in range(linhas_b):
                linha = list(map(int, input(f"Informe os elementos da linha {i + 1} da segunda matriz separados por espaço: ").split()))
                matriz_b.append(linha)
            resultado = multiplicar_matrizes(matriz, matriz_b)
            if resultado:
                imprimir_matriz(matriz)
                print("X")
                imprimir_matriz(matriz_b)
                print("=")
                imprimir_matriz(resultado)
            else:
                print("Multiplicação não é possível.")
        elif opcao == '4':
            transposta = transpor_matriz(matriz)
            imprimir_matriz(transposta)
        else:
            print("Opção inválida. Tente novamente.")

def main():
    while True:
        print("\nMenu Principal")
        print("1. Conjuntos Numéricos")
        print("2. Funções do Segundo Grau")
        print("3. Funções Exponenciais")
        print("4. Matrizes")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '5':
            break
        elif opcao == '1':
            menu_conjuntos()
        elif opcao == '2':
            menu_funcoes_segundo_grau()
        elif opcao == '3':
            menu_funcoes_exponenciais()
        elif opcao == '4':
            menu_matrizes()
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
