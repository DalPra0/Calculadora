vetor = []
def criar_vetor():
    for i in range(0,5):
        vetor.append(0)
    return vetor
print(criar_vetor())


nome = input("nome")
def inverter():
##    reversed_string = ''.join(palavra[::-1] for palavra in nome.split())
    reversed_string = ''.join(reversed(nome))

    return reversed_string

print(inverter())