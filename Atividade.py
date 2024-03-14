print("")
print("Lucas Dal Pra Brascher - 1C - Atividade 1: Calculadora no GitHub")
print("")

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

print("1 - Soma ; 2 -  Subtração ; 3 - Multiplicação ; 4 - Divisão ; 5 - Sair")

oper = int(input("Seguindo o exemplo acima, qual operação voce deseja realizar? "))

if oper == 1:

    resultado = num1+num2
    print("A operação foi soma: ", num1,"+", num2, "=", resultado)

elif oper == 2:

    resultado = num1-num2
    print("A operação foi subtração: ", num1, "-", num2, "=", resultado)

elif oper == 3:

    resultado = num1*num2
    print("A operação foi multiplicação: ", num1, "x", num2, "=", resultado)

elif oper == 4:

    resultado = num1/num2
    print("A operação foi divisão: ", num1, "%", num2, "=", resultado)

elif oper == 5:
    
    exit