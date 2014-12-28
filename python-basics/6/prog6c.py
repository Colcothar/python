import re
str=input("Enter passwords :\n")
list1=str.split(',')
for i in list1:
	a=re.search('[A-Z]',i)
	b=re.search('[a-z]',i)
	c=re.search('[0-9]',i)
	d=re.search('[$#@]',i)
	if(len(i)>=6 and len(i)<=12 and a!=None and b!=None and c!=None and d!=None):
		print (i,end=',')
print('\b\n')
