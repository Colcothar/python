def min(a,b):
	if a>b:
		print("%d is lesser than %d"%(b,a))
	else:
		print("%d is lesser than %d"%(a,b))

		 
def outer(m):
	def inner():
		print("To find min of two numbers...")
		x=int(input("Enter a number:"))		
		y=int(input("Enter another number:"))		
		m(x,y)
		print("Function decorated successfully!!!")
	return inner
min=outer(min)
min()
		
