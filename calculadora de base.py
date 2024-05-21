## Codigo calculadora de binario

print("1 - Operações de bases iguais, 2 - Transposição de base")

opt = int(input("Baseado na tabela acima, qual operação deseja fazer?"))

if opt == 1:
    print("2 - Binario, 8 - Octal, 10 - Decimal, 16 - Hexadecimal")
    opeBase = int(input("Deseja fazer uma operação com qual base?"))
    if opeBase == 2:
        print("Binario")

    elif opeBase == 8:
        print("Octal")

    elif opeBase == 10:
        print("Decimal")

    elif opeBase == 16:
        print("Hexadecimal")

    else:
        print("Nao temos essa opcao")
        