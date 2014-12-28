def Pallindromes(*args):
	str_list=[]
	for string in args:
		#rev_str="".join(reversed(string)) #could also be written in another way
		rev_str=string[::-1]
		if (string==rev_str):
			str_list.append(string)
			
	return str_list

	
li=Pallindromes("ababa","ram","bob","vaibhav")
print ("The pallindrome strings are : ",li)
