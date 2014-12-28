m=int(input("enter number:\n"))
h=range(1,m+1)
b='='
for i in range(m):
	a=''
	for j in range(i+1):
		s=str(h[j])
		a=a+s
	sum=(str.join("+",a))
	print(sum+b+str(eval(sum)))

