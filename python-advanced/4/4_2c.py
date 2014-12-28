import re
f=open("input.txt","r")
count=0
for i in f:
	name,phone,mail=i.split()
	
	m=re.search(r"(?P<user>\w+)@(?P<domain>[a-z]+)\.(?P<tld>[a-z]+)",mail)	
	if(m.group('domain')=='gmail'):
		count+=1
print("Total no. of people having gmail IDs:",count)
f.close()
