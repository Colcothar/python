a=[]
b=[]
while(True):
	choice=input("Enter ur choice: \n  1.To enter a number \n 2.To exit \n")
	ch=int(choice)
	if(ch==1):
		item=input("Enter the number")
		j=int(item)
		a.append(j)
	elif(ch==2):
		break
l=len(a)
b=[sum(a[0:i]) for i in range(1,l+1)]
print(b)
