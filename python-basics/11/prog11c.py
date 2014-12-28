import re
r1=(r'[a-z]---[a-z]')
r2=(r'[a-z]<<[a-z]')
r3=(r'[a-z]<[a-z]-[a-z]')
string='''a---b\na<<b\na<b-c'''
print(string)
rc1=re.compile(r1)
rc2=re.compile(r2)
rc3=re.compile(r3)
print("a--b")
for i in rc1.findall(string):
    print(i[0],'ID')
    print(i[1]+i[2],'OP')
    print(i[3],'OP')
    print(i[4],'ID')
print("a<<b")
for i in rc2.findall(string):
    print(i[0],'ID')
    print(i[1]+i[2],'OP')
    print(i[3],'ID')
print("a<b-c")
for i in rc3.findall(string):
    print(i[0],'ID')
    print(i[1],'OP')
    print(i[2],'ID')
    print(i[3],'OP')
    print(i[4],'ID')

