def pall(n):
	r=0
	while (n!=0):
		a=n%10
		r=(r*10)+a
		n=int(n/10)
	return r

def oddpall(n):
	a=pall(n)
	if(a==n and n%2==1):
		return 1
	else:
		return 0

a=int(input("Enter a : "))
b=int(input("Enter b : "))
for i in range(a,int(b+1)):
	c=oddpall(i)
	if(c==1):
		print(i)
