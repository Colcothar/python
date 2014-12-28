from collections import OrderedDict
dict={}
print("Dictionary programm")
while(True):
	a=int(input("Enter :\n 1. To search for a word meaning\n 2.To find words with have meaning \n 3.Remove an entry from dictionary \n 4.display all the words sorted alphabetically \n 5. Enter the new word \n 6. Exit \n "))
	#a=int(b)
	if(a==1):
		word=input("Enter the word to be searched for :\n")
		k=0
		for(i,j) in dict.items():
			if(i==word):
				print("The meaning is : ",j)
				k=k+1
		if(k==0):
			print("Meaning not found \n")
	elif(a==2):
		meaning=input("The word for which same meaning to be found: \n ")
		k=0
		for(i,j) in dict.items():
			if(j==meaning):
				print("Synonym  is : ",i)
				k=k+1
		if(k==0):
			print("Synonym not found \n")
	elif(a==3):
		word=input("Enter the word to be deleted \n")
		del(dict[word])
	elif(a==4):
		print(OrderedDict(sorted(dict.items(),key=lambda t:t[0])))
	elif(a==5):
		word=input("Enter the word to be added")
		meaning=input("Enter the meaning of the word")
		dict[word]=meaning
	elif(a==6):
		break
