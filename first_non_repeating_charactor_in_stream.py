# I've used dictionary + doubly linked list to solve this problem. I've wrote 2 implementations. 
# method 1: store node reference and character frenquency both in dictionary. {char:[node,fre]}. 

class Node:
	def __init__(self, char):
		self.char = char
		self.fre = 1
		self.prev = None
		self.next = None


class FindFirstNonRepeating:
	def __init__(self):
		self.dic = {} #map char to (node, frequency)
		self.head = self.tail =Node(None)
		self.head.next = self.tail
		self.tail.prev = self.head


	def nextInStream(self, char):
		print("Reading", char, "from stream")
		# check the char in dic
		if char in self.dic:
			if self.dic[char].fre == 1:
				# pull it out
				node_to_remove = self.dic[char]
				self.removeNode(node_to_remove)
				self.dic[char].fre += 1
		else:
			# 1, add it to dic
			newNode = Node(char)
			self.dic[char] = newNode
			# 2.  add it to linkedlist
			self.addAtRight(newNode)
		if self.head.next == self.tail:
			res = -1
		else:
			res = self.head.next.char
		print("First non-repeating character so far is",res )

	def addAtRight(self, node):
		last_node = self.tail.prev
		node.next = self.tail
		node.prev = last_node
		last_node.next = node
		self.tail.prev = node

	def removeNode(self, node):
		node.prev.next = node.next
		node.next.prev = node.prev

# testing code
newObj = FindFirstNonRepeating()
newObj.nextInStream("a")
newObj.nextInStream("a")
newObj.nextInStream("b")
newObj.nextInStream("c")
newObj.nextInStream("b")
----------------------

# method 2: store frequency in Node. dictionaries value only store node reference. we can look up frequency by accessing the node. even after the node is deleted from DLL, 
# we still have reference to it, because we do not remove any key in our dictionary. 

class Node:
	def __init__(self, char):
		self.char = char
		self.fre = 1
		self.prev = None
		self.next = None


class FindFirstNonRepeating:
	def __init__(self):
		self.dic = {} #map char to (node, frequency)
		self.head = self.tail =Node(None)
		self.head.next = self.tail
		self.tail.prev = self.head


	def nextInStream(self, char):
		print("Reading", char, "from stream")
		# check the char in dic
		if char in self.dic:
			if self.dic[char].fre == 1:
				# pull it out
				node_to_remove = self.dic[char]
				self.removeNode(node_to_remove)
				self.dic[char].fre += 1
		else:
			# 1, add it to dic
			newNode = Node(char)
			self.dic[char] = newNode
			# 2.  add it to linkedlist
			self.addAtRight(newNode)
		if self.head.next == self.tail:
			res = -1
		else:
			res = self.head.next.char
		print("First non-repeating character so far is",res )

	def addAtRight(self, node):
		last_node = self.tail.prev
		node.next = self.tail
		node.prev = last_node
		last_node.next = node
		self.tail.prev = node

	def removeNode(self, node):
		node.prev.next = node.next
		node.next.prev = node.prev

# testing code
newObj = FindFirstNonRepeating()
newObj.nextInStream("a")
newObj.nextInStream("a")
newObj.nextInStream("b")
newObj.nextInStream("c")
newObj.nextInStream("b")

