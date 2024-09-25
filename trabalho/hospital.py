class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

    def inserirSemPrioridade(self, novo_nodo):
        if not self.cabeca:
            self.cabeca = novo_nodo
        else:
            atual = self.cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_nodo

    def inserirComPrioridade(self, novo_nodo):
        if not self.cabeca:
            self.cabeca = novo_nodo
        else:
            atual = self.cabeca
            anterior = None
            while atual and atual.cor == 'A':
                anterior = atual
                atual = atual.proximo
            if not anterior:
                novo_nodo.proximo = self.cabeca
                self.cabeca = novo_nodo
            else:
                novo_nodo.proximo = atual
                anterior.proximo = novo_nodo

    def inserir(self):
        cor = input("Digite a cor do cartão (A/V): ").strip().upper()
        numero = int(input("Digite o número do cartão: ").strip())
        novo_nodo = Nodo(numero, cor)
        if not self.cabeca:
            self.cabeca = novo_nodo
        elif cor == 'V':
            self.inserirSemPrioridade(novo_nodo)
        elif cor == 'A':
            self.inserirComPrioridade(novo_nodo)

    def imprimirListaEspera(self):
        atual = self.cabeca
        while atual:
            print(f"Cartão {atual.numero} - Cor {atual.cor}")
            atual = atual.proximo

    def atenderPaciente(self):
        if self.cabeca:
            print(f"Chamando paciente com cartão {self.cabeca.numero}")
            self.cabeca = self.cabeca.proximo
        else:
            print("Não há pacientes na fila.")

def menu():
    lista = ListaEncadeada()
    while True:
        print("\nMenu:")
        print("1 - Adicionar paciente à fila")
        print("2 - Mostrar pacientes na fila")
        print("3 - Chamar paciente")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ").strip()
        if opcao == '1':
            lista.inserir()
        elif opcao == '2':
            lista.imprimirListaEspera()
        elif opcao == '3':
            lista.atenderPaciente()
        elif opcao == '4':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")
menu()