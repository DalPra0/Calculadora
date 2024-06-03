def menu_principal():
    while True:
        print("\nCalculadora RMC - Menu Principal")
        print("1. Conjuntos Numéricos")
        print("2. Funções do Segundo Grau")
        print("3. Funções Exponenciais")
        print("4. Matrizes")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            menu_conjuntos()
        elif escolha == '2':
            menu_funcoes_segundo_grau()
        elif escolha == '3':
            menu_funcoes_exponenciais()
        elif escolha == '4':
            menu_matrizes()
        elif escolha == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_conjuntos():
    while True:
        print("\nConjuntos Numéricos")
        print("1. Verificar subconjunto próprio")
        print("2. Realizar união")
        print("3. Calcular intersecção")
        print("4. Calcular diferença")
        print("5. Voltar")
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            verificar_subconjunto()
        elif escolha == '2':
            realizar_uniao()
        elif escolha == '3':
            calcular_interseccao()
        elif escolha == '4':
            calcular_diferenca()
        elif escolha == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_funcoes_segundo_grau():
    while True:
        print("\nFunções do Segundo Grau")
        print("1. Calcular raízes")
        print("2. Calcular função em x pedido")
        print("3. Calcular vértice")
        print("4. Gerar gráfico")
        print("5. Voltar")
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            calcular_raizes()
        elif escolha == '2':
            calcular_funcao_em_x()
        elif escolha == '3':
            calcular_vertice()
        elif escolha == '4':
            gerar_grafico_segundo_grau()
        elif escolha == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_funcoes_exponenciais():
    while True:
        print("\nFunções Exponenciais")
        print("1. Verificar se é crescente ou decrescente")
        print("2. Calcular função em x pedido")
        print("3. Gerar gráfico")
        print("4. Voltar")
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            verificar_crescente_decrescente()
        elif escolha == '2':
            calcular_funcao_exponencial_em_x()
        elif escolha == '3':
            gerar_grafico_exponencial()
        elif escolha == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_matrizes():
    while True:
        print("\nMatrizes")
        print("1. Determinante")
        print("2. Multiplicação")
        print("3. Matriz transposta")
        print("4. Voltar")
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            calcular_determinante()
        elif escolha == '2':
            multiplicar_matrizes()
        elif escolha == '3':
            calcular_transposta()
        elif escolha == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")

def verificar_subconjunto():
    A = set(input("Digite os elementos do conjunto A separados por espaço: ").split())
    B = set(input("Digite os elementos do conjunto B separados por espaço: ").split())
    if A < B:
        print("A é subconjunto próprio de B")
    else:
        print("A não é subconjunto próprio de B")

def realizar_uniao():
    A = set(input("Digite os elementos do conjunto A separados por espaço: ").split())
    B = set(input("Digite os elementos do conjunto B separados por espaço: ").split())
    print("A união de A e B é:", A | B)

def calcular_interseccao():
    A = set(input("Digite os elementos do conjunto A separados por espaço: ").split())
    B = set(input("Digite os elementos do conjunto B separados por espaço: ").split())
    print("A interseção de A e B é:", A & B)

def calcular_diferenca():
    A = set(input("Digite os elementos do conjunto A separados por espaço: ").split())
    B = set(input("Digite os elementos do conjunto B separados por espaço: ").split())
    print("A diferença de A e B é:", A - B)

def calcular_raizes():
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    delta = b**2 - 4*a*c
    if delta > 0:
        raiz1 = (-b + delta**0.5) / (2*a)
        raiz2 = (-b - delta**0.5) / (2*a)
        print(f"As raízes são {raiz1} e {raiz2}")
    elif delta == 0:
        raiz = -b / (2*a)
        print(f"A raiz é {raiz}")
    else:
        raiz_real = -b / (2*a)
        raiz_imaginaria = (-delta)**0.5 / (2*a)
        print(f"As raízes são {raiz_real} + {raiz_imaginaria}i e {raiz_real} - {raiz_imaginaria}i")

def calcular_funcao_em_x():
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    x = float(input("Digite o valor de x: "))
    resultado = a*x**2 + b*x + c
    print(f"f({x}) = {resultado}")

def calcular_vertice():
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    xv = -b / (2*a)
    yv = a*xv**2 + b*xv + c
    if a > 0:
        tipo = "mínimo"
    else:
        tipo = "máximo"
    print(f"O vértice da parábola é ({xv}, {yv}) e é um ponto de {tipo}")

def gerar_grafico_segundo_grau():
    import matplotlib.pyplot as plt
    import numpy as np
    
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    
    x = np.linspace(-10, 10, 400)
    y = a*x**2 + b*x + c
    
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(f'Gráfico de f(x) = {a}x^2 + {b}x + {c}')
    plt.grid(True)
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.show()

def verificar_crescente_decrescente():
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    if b > 1:
        print("A função é crescente")
    elif 0 < b < 1:
        print("A função é decrescente")
    else:
        print("Valor de b inválido para uma função exponencial")

def calcular_funcao_exponencial_em_x():
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    x = float(input("Digite o valor de x: "))
    resultado = a * (b ** x)
    print(f"f({x}) = {resultado}")

def gerar_grafico_exponencial():
    import matplotlib.pyplot as plt
    import numpy as np
    
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    
    x = np.linspace(-10, 10, 400)
    y = a * (b ** x)
    
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(f'Gráfico de f(x) = {a} * {b}^x')
    plt.grid(True)
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.show()

def calcular_determinante():
    tamanho = int(input("Digite o tamanho da matriz (2 ou 3): "))
    if tamanho == 2:
        matriz = [[float(input(f"Digite o elemento [{i+1},{j+1}]: ")) for j in range(2)] for i in range(2)]
        determinante = matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
        print(f"O determinante é {determinante}")
    elif tamanho == 3:
        matriz = [[float(input(f"Digite o elemento [{i+1},{j+1}]: ")) for j in range(3)] for i in range(3)]
        determinante = (matriz[0][0] * matriz[1][1] * matriz[2][2] + 
                        matriz[0][1] * matriz[1][2] * matriz[2][0] + 
                        matriz[0][2] * matriz[1][0] * matriz[2][1] - 
                        matriz[0][2] * matriz[1][1] * matriz[2][0] - 
                        matriz[0][1] * matriz[1][0] * matriz[2][2] - 
                        matriz[0][0] * matriz[1][2] * matriz[2][1])
        print(f"O determinante é {determinante}")
    else:
        print("Tamanho inválido")

def multiplicar_matrizes():
    linhas_A = int(input("Digite o número de linhas da matriz A: "))
    colunas_A = int(input("Digite o número de colunas da matriz A: "))
    matriz_A = [[float(input(f"Digite o elemento A[{i+1},{j+1}]: ")) for j in range(colunas_A)] for i in range(linhas_A)]
    
    linhas_B = int(input("Digite o número de linhas da matriz B: "))
    colunas_B = int(input("Digite o número de colunas da matriz B: "))
    
    if colunas_A != linhas_B:
        print("A multiplicação não é possível. O número de colunas da matriz A deve ser igual ao número de linhas da matriz B.")
        return
    
    matriz_B = [[float(input(f"Digite o elemento B[{i+1},{j+1}]: ")) for j in range(colunas_B)] for i in range(linhas_B)]
    
    matriz_resultado = [[sum(matriz_A[i][k] * matriz_B[k][j] for k in range(colunas_A)) for j in range(colunas_B)] for i in range(linhas_A)]
    
    print("A matriz resultado da multiplicação AxB é:")
    for linha in matriz_resultado:
        print(linha)

def calcular_transposta():
    linhas = int(input("Digite o número de linhas da matriz: "))
    colunas = int(input("Digite o número de colunas da matriz: "))
    matriz = [[float(input(f"Digite o elemento [{i+1},{j+1}]: ")) for j in range(colunas)] for i in range(linhas)]
    
    matriz_transposta = [[matriz[j][i] for j in range(linhas)] for i in range(colunas)]
    
    print("A matriz transposta é:")
    for linha in matriz_transposta:
        print(linha)

if __name__ == "__main__":
    menu_principal()
    