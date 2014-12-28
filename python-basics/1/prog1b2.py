import glob,os
os.chdir("/home/sushant/PAP")
list1=glob.glob('*')
big = list1[0]
for i in list1:
	if(os.path.getsize(i)>os.path.getsize(big)):
		big=i
print ('Biggest file :->',big)
