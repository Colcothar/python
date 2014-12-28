class MyStack:
	def __init__(self):
		self.st=[]
	def push(self,ele):
		self.st.insert(0,ele)
	def pop(self):
		try:
			self.st.pop(0)
		except:
			print("Stack Empty")
	def display(self):
		print(self.st)

s=MyStack()
while True:
	ch=int(input("1:Push\n2:Pop\n3:Display\n4:Exit\n"))
	if(ch==1):
		n=int(input("Enter Data : "))
		s.push(n)
	elif(ch==2):
		s.pop()
	elif(ch==3):
		s.display()
	elif(ch==4):
		break
	else:
		print("Wrong Input")
		continue

