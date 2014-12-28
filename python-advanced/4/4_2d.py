import re
f=open("input.txt","r")
print("User name part of email ID for people whose names start with \'G\' or \'E\' and end with \'y\':")
for i in f:
	name,phone,mail=i.split()	
	m=re.search(r"(?P<user>\w+)@(?P<domain>[a-z]+)\.(?P<tld>[a-z]+)",mail)	
	if(re.search("^[GE].*y$",name)):
		print(m.group('user'))
f.close()
