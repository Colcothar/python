import functools
l=[]
while(True):
	ch=int(input("Enter 1 to add an item to the list and 2 to exit.."))
	if(ch==1):
		num=int(input("Enter the no to be added.."))
		l.append(num)
	elif(ch==2):
		break
print("The list is..")
print(l)
print("The combined number is "+str(functools.reduce(lambda x,y: str(x)+str(y), l)))
