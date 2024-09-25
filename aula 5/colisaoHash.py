#endereçamento aberto e tentativa linear

def hashFunc (k, n):
    return k % n

def hashFuncSigla (k, n):
    k = list(k)
    return (ord(k[0]) + ord(k[1])) % n

def tentativaLienar(k, n, pos, tabelaHash):
   tentativa = pos
   while (tabelaHash[tentativa] != None):
      tentativa +=1
      if tentativa == n:
         tentativa =0
      if tentativa == pos:
         tentativa = -1
         break
      return tentativa

#programa principal
#n é posições
#Programa principal
n = 10
tabelaHash = [None] * n

while True:
  print('1 - Inserir na tabela hash')
  print('2 - Remover na tabela hash')
  print('3 - Listar a tabela hash')
  print('4 - Sair')

  op = int(input("Escolha uma opção:"))
  if op == 1:
    chave = input('Digite a sigla de um estado: ')
    pos = hashFuncSigla(chave, n)
    if tabelaHash[pos] == None:
        tabelaHash[pos] = chave
    else: # colisao
        pos = tentativaLinear(chave, n, pos, tabelaHash)
        if pos != -1:
           tabelaHash[pos] = chave
        else:
           print('tabela cheia, impossivel inserir.')
  elif op == 2:
    chave = int(input('Digite o que deseja remover: '))
    pos = hashFuncSigla(chave, n)
    if tabelaHash[pos] == chave:
        tabelaHash[pos] = None
    else:
        print('Valor não localizado para a remoção!')
  elif op == 3:
      print(tabelaHash)
  elif op == 4:
    print('Encerrando...')
    break
  else:
    print("Selecione outra opção!\n")