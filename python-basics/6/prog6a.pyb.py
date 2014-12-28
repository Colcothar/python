import re
sub=input("Enter the string")
pat=input("Enter character")
m=re.findall(pat,sub)
if len(m)>=2:
     print("Character occurs more then once")
elif len(m)==1:
     print("Character occurs only once")
else:
     print("Character not found")

