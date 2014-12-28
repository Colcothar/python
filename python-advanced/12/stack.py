class Stack:
	'''Stack class'''

	def __init__(self,size):
		self.stack=[]
		self.size=size
	
	def push(self,elem):
		try:
			if len(self.stack)==self.size:
				raise Exception
		except Exception as e:
				print("Stack full\n")
		else:
			self.stack.append(elem)

	def pop(self):
		try:
			x=self.stack.pop()
		except:
			print("Empty stack\n")
		else:
			return x

	def display(self):
		print("\nThe stack contents are:")
		for i in self.stack:
			print(i,end=' ')
		print("\n")
n=int(input("Enter the size of the stack"))
obj=Stack(n)
while True:
	ch=int(input("1-Push\n2-Pop\n3-Display\n4-Exit\t"))
	if ch==1:
		e=int(input("\nEnter the element\t"))
		obj.push(e)
	elif ch==2:
		e=obj.pop()
		if e!=None:
			print("The returned object is:{}\n".format(e))
	elif ch==3:
		obj.display()
	else:
		break
