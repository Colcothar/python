import glob,os
a=list(filter(os.path.isfile,glob.glob('*')))
print(a)
b=[]
for i in range(0,5):
	big=a[0]
	for j in range(len(a)):
		if(os.path.getsize(a[j])>os.path.getsize(big)):
			big=a[j]
	b.append(big)
	a.remove(big)
print (b)
b.sort()
print (b)
