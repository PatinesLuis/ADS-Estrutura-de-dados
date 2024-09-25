dados = [5,4,2,1,8]

def bubbleSort(dados):
    tam = len(dados)

    for v in range(0,tam,1):
        for i in range(0, tam-1,1):
            print("o " + str(dados[1]) + " é maior do que " + str(dados[i+1]))
            if dados[i] > dados[i+1]:
                aux = dados[i]
                dados[i] = dados[i+1]
                dados[i+1] = aux

bubbleSort(dados)
print("------")
print(dados)