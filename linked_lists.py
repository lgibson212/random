class Node:
	def __init__(self, data, pointer):
		self.data = data
		self.next = pointer

class LinkedList:
	def __init__(self, node):
		self.head = node
		current1 = self.head

	def insert(self, node):
		current = self.head
		if current == None:
			self.head = node
		while current:
		#while used instead of for loop since there is an undefined number of nodes (we don't know how many)
			if current.next == None:
				current.next = node
				break
			current = current.next

	def delete(self, data):
		current = self.head
		previous = None
		while current:
			if current.data == data and current.next != None:
			#if not last node in list
				current.data = current.next.data
				current.next = current.next.next
				#move pointer to Next Node
			elif current.data == data and current.next == None:
			#if is last node in list
				if current == self.head:
					self.head = None
					break
				else:
					previous.next = previous.next.next
			previous = current
			current = current.next
			#sets previous node to be next node, skipping over current


	def search(self, data):
		current = self.head 
		data_exists = False
		while current:
			if current.data == data:
				data_exists = True
				return current
			current = current.next
		if data_exists == False:
			return None


	def print_forward(self):
		current = self.head
		while current:
			print("|{}| -> ".format(current.data), end="")
			#end prints it out on the same line
			current = current.next 
		print("None")

	def print_backward(self):
		print("None", end='')
		self.pb()

	def pb(self):
		out = ""
		current = self.head
		while current:
			out = "|{}| <- ".format(str(current.data)) + out
			current = current.next
		print(out)
	
