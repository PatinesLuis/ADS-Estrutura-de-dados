class bst:
    def __init_(self, dado=None):
        self.dado = dado
        self.esquerda = None
        self.direita = None

    def inserir(self, dado):
        if (self.dado == None):
                self.dado = dado
        else:
            if (dado < self.dado):
                if(self.esquerda):
                    self.esquerda.inserir(dado)
                else:
                    self.esquerda = bst(dado)
            else:
                if(self.direita):
                    self.direita.inserir(dado)
                else:
                    self.direita = bst(dado)

Teste = bst()

Teste.inserir(7)
Teste.inserir(4)
Teste.inserir(9)
Teste.inserir(5)
Teste.inserir(12)