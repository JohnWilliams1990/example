#!PYTHONPATH




class Stack():
	def __init__(self):
		self.stack = []
	def push(self,item):
		self.stack.append(item)
	def pop(self):
		x = self.stack[len(self.stack)-1]
		self.stack.pop()
		return x
	def peek(self):
		return self.stack[len(self.stack)-1]

	def isEmpty(self):
		return (len(self.stack) == 0)


#x = Stack()
	
#for i in range(100):
#	x.push(i)

#for i in range(100):
#	if not x.empty():
#		print(x.peek())
#		x.pop()

#if x.isEmpty():
#	print("stack is empty", end = " your face!")
 
	

	
