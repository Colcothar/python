input_xy = input("Enter the value of x and y : ")
list1 = input_xy.split(',')
row_d=int(list1[0])
col_d=int(list1[1])
list2=[]
i=0
while i in range(0,row_d):
	list3=[]
	j=0
	while j in range(0,col_d):
		list3.append(i*j)
		j += 1
	list2.append(list3)
	i += 1
print (list2)
