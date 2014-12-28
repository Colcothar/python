s=input("Enter a sentence : ")
d={'Upper':0,'Lower':0}
for i in s:
	if(i.isupper()):
		d['Upper'] += 1
	elif(i.islower()):
		d['Lower'] +=1
	else:
		pass
print("Upper :",d['Upper'],"Lower :",d['Lower'])
