l=[]
while(True):
	ch=int(input("Enter ur choice:1>enter a string to the list\n2>exit\n"))
	if(ch==1):
		num=input("Enter the string:\n")
		l.append(num)
	elif(ch==2):
		break
s=filter((lambda x:x[0].isdigit()==0),l)
print(list(s))
