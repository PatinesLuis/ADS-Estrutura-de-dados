def queue(pilha, fim, tam, dado):
    if len(fila) == tam:
        print("fila cheia! impossivel inserir. ")
    else:
        if fim < tam:
            fila.insert(fim, dado)
            fim += 1
        else:
            fim = 0
            fila.insert(fim, dado)
        return fila, fim

def dequeue (fila, inicio):
    if len(fila) == 0:
        print('fila vazia! impossivel remover.')
    else:
        fila[inicio] = None
        inicio +=1
        return fila, inicio

inicio = 0 
fim = 0
fila = []
tam = 5

while True:
    print("1 - Inserir na fila")
    print("2 - remover na fila")
    print("3 - listar na fila")
    print("4 - Sair")

    op = int(input("escolha uma opção:"))
    if op ==1:
        dado = int (input('Qual numero deseja inserir?'))
        fila, fim = queue(fila, inicio, tam, dado)
    elif op ==2:
        fila, inicio = dequeue(fila, inicio)
    elif op ==3:
        for item in fila:
            print(item, end = " ")
        print()
    elif op ==4:
        print("encerrando")
        break
    else:
        print("Selecione outra opção")