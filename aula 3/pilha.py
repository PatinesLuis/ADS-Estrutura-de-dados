top = 0
pilha = []
tam = 5

def push(pilha, top, tam, dado):
    if len(pilha) == tam:
        print('pilha cheia! remova algum item para inserir outro')
    else:
        pilha.insert(top,dado)
        top +=1
        return pilha, top 
    
def pop(pilha, top):
    if len(pilha) == 0:
        print("pilha vazia! insira algum dado")
    else:
        del pilha[top]
        top -= 1
        return pilha, top

while True:
    print ("1 - insira na pilha")
    print ("2 - remova na pilha")
    print ("3 - lista a pilha")
    print ("4 - Sair")

    op = int(input("Escolha uma opção:"))
    if op ==1:
        dado = int(input("Qual numero deseja inserir"))
        push(pilha, top, tam, dado)
    elif op == 2:
        pop(pilha, top,)
    elif op ==3:
        for item in pilha:
            print(item)
    elif op ==4:
        print("encerrando")
        break
    else:
        print("selecione outra opção!")
        print(" ")