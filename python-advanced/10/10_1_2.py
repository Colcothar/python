a=int(input("Enter 1 for default and 2 for giving values.."))
def func(z=",",first="result",*args):
	k=[first]
	print(args)
	l=list(args)
	for i in l:
		k.append(i)
		s=z.join(k)
	print(s)
#default args
if(a==2):
        sep=input("Enter the separator ")
        first_string=input("Enter the first String")
        variable_string=input("Enter th list of strings which u wanna concatenate")
        func(sep,first_string,variable_string)
elif(a==1):
        s=input("Enter strings")
        func(s)
