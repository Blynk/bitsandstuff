from collections import deque

class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class Tree:
	def __init__(self):
		self.root = None
		self.nodeCount = 0
		print "Created a new Binary Search Tree"

	def fromList(self, list):
		for num in list:
			self.insert(self.root, Node(num))

	def insert(self, currentNode, newNode):
		if self.root == None:
			self.root = newNode
			self.nodeCount += 1
		else:
			if newNode.value < currentNode.value:
				if currentNode.left is None:
					currentNode.left = newNode
					self.nodeCount += 1
				else:
					self.insert(currentNode.left, newNode)
			elif newNode.value > currentNode.value:
				if currentNode.right is None:
					currentNode.right = newNode
					self.nodeCount += 1
				else:
					self.insert(currentNode.right, newNode)
			else:
				print "Node with value already exists"

	def delete(self, currentNode, value):
		if self.nodeCount == 0:
			print "No nodes in tree"
			return false
		elif currentNode == None:
			print "Value not Found"
			return false
		else:
			# We need to serach for the node to delete
			if currentNode.value < value:
				self.delete(currentNode.right, value)
			elif currentNode.value > value:
				self.delete(currentNode.left, value)
			else:
				# we found the matching value --
				# Now there are three cases: 2, 1, or 0 children
				if currentNode.right and currentNode.left:
					parent = currentNode
					successor = currentNode.right
					while successor.left:
						parent = sucessor
						successor = successor.left
					currentNode.value = successor.value
					if parent.left == successor:
						# This means that the successor was the left child
						# of a node to the right
						# We need to shift up the subtree in case there were
						# any children on the right of the successor
						parent.left = successor.right
					else:
						# This means that the right child had no children
						# of its own on the left
						# So, we take the right subtree and shift up
						parent.right = successor.right
					del successor
				elif currentNode.right or currentNode.left:
					if currentNode.right == None:
						currentNode = currentNode.left
					else:
						currentNode = currentNode.right
				else:
					currentNode = None
				self.nodeCount -= 1
				return true

	def preorder(self, currentNode):
		if currentNode == None:
			return
		else:
			print str(currentNode.value) + " ",
			self.preorder(currentNode.left)
			self.preorder(currentNode.right)
	
	def inorder(self, currentNode):
		if currentNode == None:
			return
		else:
			self.inorder(currentNode.left)
			print str(currentNode.value) + " ", 
			self.inorder(currentNode.right)

	def postorder(self, currentNode):
		if currentNode == None:
			return
		else:
			self.postorder(currentNode.left)
			self.postorder(currentNode.right)
			print str(currentNode.value) + " ",

	def breadthfirst(self):
		q = deque()
		q.append(self.root)
		while len(q) != 0:
			currentNode = q.popleft()
			print str(currentNode.value) + " ",
			if currentNode.left != None:
				q.append(currentNode.left)
			if currentNode.right != None:
				q.append(currentNode.right)

	def getheight(self, currentNode):
		if currentNode == None:
			return 0
		else:
			left = self.getheight(currentNode.left) + 1
			right = self.getheight(currentNode.right) + 1
			return max(left, right)

t = Tree()
t.insert(t.root, Node(8))
t.insert(t.root, Node(3))
t.inorder(t.root)
print ""
t.insert(t.root, Node(10))
t.fromList([8, 3, 1, 6, 4, 7, 10, 14, 13])
t.inorder(t.root)
