import re
#First program
string = '''hello hi this is Harvey
	hi this is PYTHON Lab
	hi this is lab 7'''

pattern = 'hI'

r = re.finditer(pattern,string,re.M + re.I)
for i in r:
	print("Starting Index of the matched pattern->",end=' ')
	print(i.start())

#Second program
print("\n Characters except vowels and space\n")
string= 'hello hi this is Harvey hi this is PYTHON Lab hi this is lab 7'
r = re.findall('[^aeiou\s]',string,re.M + re.I)
print(r)

#Third program
print("\nStrings starting with underscore or Digit\n")
l = ['_digit','hello','1hi']
for i in l:
	if re.match('\d|_',i):
		print(i)
