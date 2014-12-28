def fib(n):
	if(n==0):
		return 1
	elif(n==1):
		return 1
	else:
		return (fib(n-1) + fib(n-2))

n=int(input('Enter a number : '))
values = [str(fib(i)) for i in range(0,n+1)]
a=str.join(',',values)
print (a)
