def dec(func):
	def f(*args):		
		print(".....................")
		func(*args)
		print(".....................")
	return f
@dec
def compare(a,b):
	if a<b:
		print(a,"is less than",b)
	elif a>b:
		print(a,"is greater than",b)
	else:
		print(a,"equals",b)
a=int(input("Enter a : "))
b=int(input("Enter b : "))
compare(a,b)
