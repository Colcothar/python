import re
f=open("input.txt","r")
print("Names having a 3 digit area code phone numbers are ->")
for i in f:
	name,phone,mail=i.split()	
	if(re.search(r"\b\d\d\d\b-.*",phone)):
		print(name)
f.close()
