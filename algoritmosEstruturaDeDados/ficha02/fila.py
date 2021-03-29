class Fila:
    #2.1. Crie uma estrutura de dados tipo “fila”
    def __init__(self):
        self.fila = []
    #2.2. Crie uma função para ver se a “fila” está vazia
    def vazia(self):
        return self.tamanho() == 0
    def tamanho(self):
        return len(self.fila)
    #2.3. Crie uma função para adicionar um elemento na “fila”
    def inserir(self, n):
        self.fila.append(n)
        print("Inserindo o item",n)
    #2.4. Crie uma função para retirar o PRIMEIRO elemento na “fila”
    def excluir(self):
        if not self.vazia():
            return self.fila.pop(0)
    #2.5. Crie uma função para listar todos os elementos da “fila”
    def mostrar(self):
        return self.fila
    #2.6. Crie uma função para testar se um determinado valor, passado por 
    # parâmetro,está na “fila”
    def procurar(self, alvo):
        encontrado = False
        for items in self.fila:
            if items is alvo:           
                print("Item",alvo,"encontrado na fila")
                encontrado = True                                           
        if encontrado == False:     
            print("Item",alvo,"não encontrado na fila")
    #2.7. Crie uma função para ordenar uma fila por
    # ordem crescente ou decrescente(tipo de ordenação passado por parâmetro)
    def ordenar(self, ordenacao):
            if ordenacao == "crescente":
                print('Fila ordenada em ordem crescente:')
                return self.fila.sort()
            if ordenacao == "decrescente":
                print('Fila ordenada em ordem decrescente:')
                return self.fila.reverse()

fila = Fila()
fila.inserir(2)
fila.inserir(5)
fila.inserir(2)
fila.inserir(10)
fila.inserir(9)
fila.inserir(1)
fila.inserir(3)
print("Fila:",fila.mostrar())
fila.ordenar("crescente")
print("Fila:",fila.mostrar())
fila.ordenar("decrescente")
print("Fila:",fila.mostrar())
print("Excluindo o elemento",fila.excluir())
fila.procurar(10)
print("Fila:",fila.mostrar())
fila.procurar(1)
print("Excluindo o elemento",fila.excluir())
print("Excluindo o elemento",fila.excluir())
print("Verificando se a fila está vazia:",fila.vazia())
print("Fila:",fila.mostrar())