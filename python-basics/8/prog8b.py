import re
regex=(r'IF|DO|ENDDO|THEN|ENDIF')
rc=re.compile(regex)
dict={}
dict['IF']=0
dict['DO']=0	
dict['THEN']=0
dict['ENDDO']=0	
dict['ENDIF']=0
string=''' IF x<8
       IF
       ENDDO
         x square
       ENDDO
       THEN x+8
       ENDIF'''
for i in rc.findall(string):
     if i=='IF':
        dict[i] += 1
     elif i=='DO':
        dict[i] += 1
     elif i=='THEN':
        dict[i] += 1
     elif i=='ENDDO':
        dict[i] += 1
     elif i=='ENDIF':
        dict[i] += 1
print(dict)

