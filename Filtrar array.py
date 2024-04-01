# crie um ALGORITIMO QUE FILTRE UM ARRAY E TIRE DELE OS ELEMENTOS QUE APARECEM UMA QUANTIDADE PAR DE VEZES E RETORNE UM NOVO ARRAY
# EXEMPLO: [1,2,1,3,3] -> [1,1] 

from collections import Counter

def filtra_elementos_pares(array):
    freq_counter = Counter(array)

    array_filtrado = [elemento for elemento in array if freq_counter[elemento] % 2 != 0]

    return array_filtrado

entrada = input("Digite os elementos do array separados por espaços: ")
meu_array = list(map(int, entrada.split()))

# Chama a função para filtrar o array
novo_array = filtra_elementos_pares(meu_array)
print("Array filtrado:", novo_array)
