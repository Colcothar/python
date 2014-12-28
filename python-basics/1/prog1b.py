import glob
import os
a=list(filter(os.path.isfile,glob.glob("*")))
print("The files in the directory are :\n")
print(a)
i=0
big=a[i]
for i in range(len(a)):
	if(os.path.getsize(a[i])>os.path.getsize(big)):
		big=a[i]
print("The biggest file is :",big)

