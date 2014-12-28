list1=[]
n=int(input("Enter the number of elements : "))
i=0
while i in range(0,n):
	a=input("Enter a number : ")
	list1.append(a)
	i += 1

d={}
for i in a:
	d[i]=0

for i in a:
	d[i] += 1

for i in d:
	print (i)
