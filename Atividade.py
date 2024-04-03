print("")
print("Lucas Dal Pra Brascher - 1C - Atividade 1: Calculadora no GitHub")
print("")

while True:
    
    print("1 - Soma ; 2 -  Subtração ; 3 - Multiplicação ; 4 - Divisão ; 5 - Sair")
    print("")

    oper = int(input("Seguindo o exemplo acima, qual operação voce deseja realizar? "))

    if oper == 1:
        num1 = int(input("Digite o primeiro numero: "))
        num2 = int(input("Digite o segundo numero: "))
        resultado = num1 + num2
        print("A operação foi soma: ", num1, "+", num2, "=", resultado)
        print("")

    elif oper == 2:
        num1 = int(input("Digite o primeiro numero: "))
        num2 = int(input("Digite o segundo numero: "))
        resultado = num1 - num2
        print("A operação foi subtração: ", num1, "-", num2, "=", resultado)
        print("")

    elif oper == 3:
        num1 = int(input("Digite o primeiro numero: "))
        num2 = int(input("Digite o segundo numero: "))
        resultado = num1 * num2
        print("A operação foi multiplicação: ", num1, "x", num2, "=", resultado)
        print("")

    elif oper == 4:
        num1 = int(input("Digite o primeiro numero: "))
        num2 = int(input("Digite o segundo numero: "))
        if num2 != 0:
            resultado = num1 / num2
            print("A operação foi divisão: ", num1, "/", num2, "=", resultado)
            print("")
        else:
            print("Erro: Divisão por zero!")
            print("")

    elif oper == 5:
        print("Encerrando o programa...")
        break

    elif oper < 0 or oper > 5:
        print("Opção invalida, tente novamente")
        print("")
        continue

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
