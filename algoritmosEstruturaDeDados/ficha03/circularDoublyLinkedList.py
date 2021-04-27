start = None

# Estrutura do node
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

# Função para inserir no fim
def insertEnd(value) :
	global start
	
	# Se a lista estiver vazia, crie um
	# circular de node unico e uma lista
	if (start == None) :

		new_node = Node(0)
		new_node.data = value
		new_node.next = new_node.prev = new_node
		start = new_node
		return

	# se a lista não estiver vazia

	# encontre o ultimo node
	last = (start).prev

	# Cria um Node dinamicamente
	new_node = Node(0)
	new_node.data = value

	# O início será o próximo do new_node
	new_node.next = start

	# faz o new_node antes do começo
	(start).prev = new_node

	# Faz a última previa do new_node
	new_node.prev = last

	# Faz o new_node próximo do último
	last.next = new_node

# Função para inserir o Node no inicio
# da lista
def insertBegin( value) :
	global start
	
	# O ponteiro aponta para o ultimo node
	last = (start).prev

	new_node = Node(0)
	new_node.data = value # Inserindo os dados

	# Configurar o anterior e o
	# próximo do new_node
	new_node.next = start
	new_node.prev = last

	# Atualiza os ponteiros seguintes e anteriores
	# de início e último.
	last.next = (start).prev = new_node

	# Atualiza o ponteiro do inicio
	start = new_node

# Função para inserir nó com valor como value1.
# O novo node é inserido após o nó com value2
def insertAfter(value1, value2) :
	global start
	new_node = Node(0)
	new_node.data = value1 # Inserindo os dados

	# Encontra o node com o value2 e o próximo node
	temp = start
	while (temp.data != value2) :
		temp = temp.next
	next = temp.next

	# insere new_node entre temp e next.
	temp.next = new_node
	new_node.prev = temp
	new_node.next = next
	next.prev = new_node

def display() :
	global start
	temp = start

	print ("Traversal in forward direction:")
	while (temp.next != start) :

		print (temp.data, end = " ")
		temp = temp.next
	
	print (temp.data)
	
	print ("Traversal in reverse direction:")
	last = start.prev
	temp = last
	while (temp.prev != last) :

		print (temp.data, end = " ")
		temp = temp.prev
	
	print (temp.data)

if __name__ == '__main__':
	global start
	
	# Começa com uma lista vazia
	start = None
	
	# Insere 5. então a lista ligada se torna 5.None
	insertEnd(5)

	# Insere 4 no inicio. já faz ligação
	# e a lista se torna 4.5
	insertBegin(4)

	# Insere 7 no fim. então a lista se torna 4.5.7
	insertEnd(7)

	# Insere 8 no fim. então a lista se torna 4.5.7.8
	insertEnd(8)

	# Insere 6, depois do 5. então a lista se torna 
    # 4.5.6.7.8
	insertAfter(6, 5)

	print ("Created circular doubly linked list is: ")
	display()