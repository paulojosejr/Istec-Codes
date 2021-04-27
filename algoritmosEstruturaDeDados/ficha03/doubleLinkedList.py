class Node:
     
    # Construtor para criar um novo nó
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
 
# Classe para criar uma lista duplamente ligada
class DoublyLinkedList:
    # Construtor para lista duplamente ligada vazia
    def __init__(self):
        self.head = None
    
    # Dada a referencia a cabeça da lista e um inteiro,
    #insere um novo nó no começo da lista
    def push(self, new_data):
 
        # 1. Aloca nó
        # 2. Coloca o dado no nó
        new_node = Node(new_data)

        # 3. Faz o próximo do novo nó como cabeça
        # e o anterior como None
        new_node.next = self.head
 
        # 4. muda prev da cabeça do nó para new_node
        if self.head is not None:
            self.head.prev = new_node
 
        # 5. move a cabeça para apontar para o novo nó
        self.head = new_node
 
    # Dado o nó como prev_node, insere um novo nó depois desse nó
    def insertAfter(self, prev_node, new_data):
 
        # 1. Checa se o prev_node dado é None
        if prev_node is None:
            print("the given previous node cannot be NULL")
            return
 
        # 2. aloca novo nó
        # 3. coloca os dados
        new_node = Node(new_data)
 
        # 4.  Faz a ligação do novo nó como next do prev node
        new_node.next = prev_node.next
 
        # 5. Faz prev_node como anterior do new_node
        prev_node.next = new_node
 
        # 6. Faz prev_node como anterior do new_node
        new_node.prev = prev_node
 
        # 7. Muda o anterior de new_node do próximo nó
        if new_node.next:
            new_node.next.prev = new_node
 
    # Dada a referencia para a cabeça e um inteiro,
    #  insere um novo nó no fim
    def append(self, new_data):
 
        # 1. Aloca o nó
        # 2. insere os dados
        new_node = Node(new_data)

        # 3. Esse novo nó vai ser o último nó,
        # então faz seu próximo ser None
        # (Já foi inicializado como None)
 
        # 4. Se a lista ligada estiver vazia,
        # faz o novo nó como cabeça
        if self.head is None:
            self.head = new_node
            return
 
        # 5.  Caso contrário atravessá até o último nó
        last = self.head
        while last.next:
            last = last.next
 
        # 6. Muda o next do último nó
        last.next = new_node
 
        # 7. Faz o último nó como anterior do novo nó
        new_node.prev = last
 
        return
 
    # Essa função escreve o conteúdo da lista
    # Começando por um dado nó
    def printList(self, node):
 
        print("\nTraversal in forward direction")
        while node:
            print(" % d" % (node.data))
            last = node
            node = node.next
 
        print("\nTraversal in reverse direction")
        while last:
            print (" % d" % (last.data))
            last = last.prev
 
# Testes
 
 
# Começa com lista vazia
llist = DoublyLinkedList()
 
# Insere 6. A lista passa a 6-> None
llist.append(6)
 
# Insere 7 no começo.
# A lista passa a 7->6->None
llist.push(7)
 
# Insere 1 no começo
# A lista passa a 1->7->6->None
llist.push(1)
 
# Insere 4 no final.
# A lista passa a 1->7->6->4->None
llist.append(4)
 
# Insere 8, Depois do 7.
# So linked list becomes 1->7->8->6->4->None
llist.insertAfter(llist.head.next, 8 )
 
print("Created Double Linked List is: ")
llist.printList(llist.head)