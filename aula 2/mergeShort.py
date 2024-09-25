dados = [54, 26, 93, 17, 77, 31, 44, 55]

def mergeSort(dados):
    # Condição que indica se os dados ainda precisam ser divididos
    if len(dados) > 1:
        # Divide recursivamente
        meio = len(dados) // 2
        esquerda = dados[:meio]
        direita = dados[meio:]

        mergeSort(esquerda)
        mergeSort(direita)

        # Intercala/mescla os dados
        i = j = k = 0

        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                dados[k] = esquerda[i]
                i += 1  # Corrigido: i = i + 1
            else:
                dados[k] = direita[j]
                j += 1  # Corrigido: j = j + 1
            k += 1  # Corrigido: k = k + 1

        while i < len(esquerda):
            dados[k] = esquerda[i]
            i += 1  # Corrigido: i = i + 1
            k += 1  # Corrigido: k = k + 1

        while j < len(direita):  # Corrigido: 'J' para 'j'
            dados[k] = direita[j]
            j += 1  # Corrigido: j = j + 1
            k += 1  # Corrigido: k = k + 1

# Exemplo de uso
mergeSort(dados)
print(dados)