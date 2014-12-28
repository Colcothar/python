import re
s = """ hello hi how
are you
and what is ur college name?
is it PES Institute of Technology"""

m = re.findall(r" *([a-zA-Z]*)",s)
l=[]
for i in m:
	l.append(len(i))
#print(l)	
l.sort(reverse=True)
#print(l)
print("\n\n-----\n\n")

first = l[0]
second = l[1]
for i in m:
	if len(i)==first or len(i)==second:
		print("\""+i+"\" with length = ",len(i))
	

