n = int(input("Enter the size of the matrix : "))
i=0
while i in range(0,n):
	j=0
	while j in range(0,n):
		if(i==j):
			print (1,end='\t')
		else:
			print (0,end='\t')
		j += 1
	print ('\n')
	i += 1
