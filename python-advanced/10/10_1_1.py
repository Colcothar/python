b=[]
def call(z,*word):
	#l=z
	s=[(lambda a:list(set(a)))(word[x]) for x in range(z)]
	print("The no of strings are...")
	print(z)
	print("The strings in the list with unique characters are:\n")
	print(s)	
while(True):
	ch=int(input("Enter ur choice:1>enter a string to the list\n2>exit\n"))
	if(ch==1):
		num=input("Enter the string:\n")
		b.append(num)
	elif(ch==2):
		z=len(b)
		call(z,*b)		
		break

