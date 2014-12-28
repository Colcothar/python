netAmount=0
while True:
	str=input('Enter the statement : ')
	if (not str):
		break
	a=str.split(' ')
	op=a[0]
	am=int(a[1])
	if(op == 'D'):
		netAmount += am
	elif(op == 'W'):
		netAmount -= am
	else:
		pass
print ('Net Amount ->',netAmount)
