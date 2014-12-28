import re
f=open("input.txt","r")
print("All names whose phone numbers are not in proper format:")
for i in f:
	name,phone,mail=i.split()	
	if(re.search(r"\b\d\d\d?-\d\d\d\d\d\d\d\d\b",phone)==None):
		print(name)
f.close()
