def greatest(list2):
	if(list2 == []):
		return 0;
	i=0
	greatest=list2[i]
	for j in list2:
		if(j>greatest):
			greatest=j
	return greatest

n=int(input("Enter a positive number or 0 to exit : "))
list1=[]
while True:
	if(n==0):
		break
	elif(n<0):
		print("Positive Numbers only !!! Please Enter again")
		n=int(input("Enter a positive number or 0 to exit : "))
		continue
	list1.append(n)
	n=int(input("Enter a positive number or 0 to exit : "))
print ("The greatest number in the list is ->",greatest(list1))
