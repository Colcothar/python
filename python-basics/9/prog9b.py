def pal(n):
	r=0
	while(n):
		a=n%10
		r=(r*10)+a
		n=int(n/10)
	return r
n=int(input('Enter a number : '))
for i in range(1,n+1):
	n2=i*i
	ri=pal(i)
	r2=pal(n2)
	if((i==ri)and(n2==r2)):
		print(i)

