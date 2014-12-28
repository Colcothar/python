f = open("stateinfo.txt", "r")
l=[]
d={}
for line in f:
	s = tuple(line.split(":"))
	d[s[0]]=open(s[0],"a+")	
	l.append(s)
print(l)
for elem in l:
	d[elem[0]].write(elem[1])
for s,f in d.items():
	f.close()
