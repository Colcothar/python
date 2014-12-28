import re
p1='[A-Z 0-9]'
p='<.+?>'
s='<text><sub>PAP</sub><abc></abc><date><dd>30</dd><mm>9</mm><yy>2013</yy></date></text>'
l=s.split(' ')
#print (l)
for i in l:
        l1=re.split(p1,i)
        #print (l1)
        for j in l1:
                a=re.search(p,j)
                #print (j)
                if a:
                        print(a.group())
