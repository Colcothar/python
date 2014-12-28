def prime(n):
	for i in range(2,int(n/2)):
		if(n%i == 0):
			return 0
	return 1

a=int(input("Enter a : "))
b=int(input("Enter b : "))
list1=[]
for i in range(a,b+1):
	c=prime(i)
	if(c==1):
		list1.append(i)
print (list1)
