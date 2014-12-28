import os
import glob
list_of_files=glob.glob("/home/pesit/Desktop/shivam/*")
for files in list_of_files:
	if(os.path.getsize(files)==0):
		os.remove(files)
	



