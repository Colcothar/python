import functools
l=[]
while(True):
	ch=int(input("Enter 1 to add an item to the list and 2 to exit.."))
	if(ch==1):
		num=int(input("Enter the no to be added.."))
		l.append(num)
	elif(ch==2):
		break
print("The list is:")
for y in l:
	print(y)
print("max no is.."+str(functools.reduce((lambda x,y: x if (x > y) else y),l)))



