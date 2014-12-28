import re
f=open('re.doc','r')
s=''
for l in f:
        s=s+l
si=re.search(r"FUNCTIONS",s)
st=si.end()
sie=re.search(r"DATA",s)
en=sie.start()
string=s[st:en]
li=re.findall(r"(.*?)\(.*?\)[^.]",string)
print('the available functions are')
for ii in li:
	print(ii)
f1=open('out.txt','w')	
f1.write(str(li))
f.close()
f1.close()

