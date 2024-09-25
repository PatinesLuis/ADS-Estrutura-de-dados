class Nodo:
    def __init__(self, sigla, nome_estado):
        self.sigla = sigla
        self.nome_estado = nome_estado
        self.proximo = None

class HashTable:
    def __init__(self):
        self.table = [None] * 10

    def hash_function(self, sigla):
        if (sigla == "DF"):
            return 7
        return (ord(sigla[0]) + ord(sigla[1])) % 10

    def inserir(self, sigla, nome_estado):
        indice = self.hash_function(sigla)
        novo_nodo = Nodo(sigla, nome_estado)
        if self.table[indice] is None:
            self.table[indice] = novo_nodo
        else:
            novo_nodo.proximo = self.table[indice]
            self.table[indice] = novo_nodo

    def imprimir_tabela(self):
        for i in range(10):
            print(f"Posição {i}: ", end="")
            nodo = self.table[i]
            if nodo is None:
                print("NONE")
            else:
                while nodo:
                    print(f"{nodo.sigla} ", end="")
                    nodo = nodo.proximo
                print()

tabela_hash = HashTable()

print("Tabela Hash antes de qualquer inserção:")
tabela_hash.imprimir_tabela()


estados = [
    ("AC", "Acre"), ("AL", "Alagoas"), ("AP", "Amapá"), ("AM", "Amazonas"),
    ("BA", "Bahia"), ("CE", "Ceará"), ("ES", "Espírito Santo"), ("GO", "Goiás"),
    ("MA", "Maranhão"), ("MT", "Mato Grosso"), ("MS", "Mato Grosso do Sul"),
    ("MG", "Minas Gerais"), ("PA", "Pará"), ("PB", "Paraíba"), ("PR", "Paraná"),
    ("PE", "Pernambuco"), ("PI", "Piauí"), ("RJ", "Rio de Janeiro"), ("RN", "Rio Grande do Norte"),
    ("RS", "Rio Grande do Sul"), ("RO", "Rondônia"), ("RR", "Roraima"), ("SC", "Santa Catarina"),
    ("SP", "São Paulo"), ("SE", "Sergipe"), ("TO", "Tocantins"), ("DF", "Distrito Federal")
]

for sigla, nome in estados:
    tabela_hash.inserir(sigla, nome)

print("\nTabela Hash após inserir os estados e DF:")
tabela_hash.imprimir_tabela()


nome_ficticio = "Luis Eduardo Patines"
sigla_ficticia = nome_ficticio[0] + nome_ficticio.split()[-1][0]
tabela_hash.inserir(sigla_ficticia, nome_ficticio)

print("\nTabela Hash após inserir os estados, DF e estado fictício:")
tabela_hash.imprimir_tabela()