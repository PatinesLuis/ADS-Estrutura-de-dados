dados = [50,22,3,5,66,22,15,95,13,12,87]

def quickSort(dados, inicio,fim):
    if(inicio < fim):
        posicao_do_pivo = particion(dados,inicio,fim)
        quickSort(dados, inicio, posicao_do_pivo -1)
        quickSort(dados, posicao_do_pivo +1, fim)

def particion(dados,inicio,fim):
    pivo = dados[inicio]
    esqu = inicio +1
    dire = fim
    flag = False
    while not flag:
        while esqu <= dire and dados[esqu] <= pivo:
            esqu = esqu +1
        while dados[dire] >= pivo and dire >= esqu:
            dire = dire -1
            if dire < esqu:
                flag = True
            else:
                temp = dados[esqu]
                dados[esqu] = dados [dire]
                dados [dire] = temp
            temp = dados[inicio]
            dados[inicio] = dados[dire]
            dados[dire] = temp
            return dire

quickSort(dados, 0, len(dados)-1)
print(dados)
