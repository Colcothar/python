import glob
import os
a=list(filter(os.path.isfile,glob.glob("*")))
print("The files are :")
print(a)
i=0
while i in range(0,len(a)):
	if(os.path.getsize(a[i]) == 0):
		os.remove(a[i])
	i += 1
a=list(filter(os.path.isfile,glob.glob("*")))
print (a)
