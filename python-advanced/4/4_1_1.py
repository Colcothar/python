import os
import fnmatch
count=0
count1=0
count2=0
for root,dir,files in os.walk("."):
	count1=count1+1	
	print("%d"%(count1)+root)
	path=root.split('/')
	
	
	for items in fnmatch.filter(files,"*"):#pattern matching:fnmatch
		count2=count2+1		
		print("%d->\t"%(count2)+items)
		count =count+1
	
		
	count2=0
print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
print("\nTotal count of directories is..\t"+str(count1))

print("Total count of files is..\t"+str(count))
	#print("")
