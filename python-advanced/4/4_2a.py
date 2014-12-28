import re
f=open("input.txt","r")
print("Phone numbers having 4 consecutive 0s in the end ->")
for i in f:
	name,phone,mail=i.split()	
	if(re.match(".*0000$",phone)):
		print(phone)
f.close()
