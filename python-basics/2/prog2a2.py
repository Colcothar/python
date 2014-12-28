import glob,os
os.chdir('/home/sushant/PAP')
list1=glob.glob('*')
r=[]
for i in list1:
	if(os.path.getsize(i)==0):
		r.append(i)
		os.remove(i)
print (i)
