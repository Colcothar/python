list1=[1,2,3,4,5,6,7,8,9,10]
even=map(lambda x:x**2,filter(lambda x:x%2==0,list1))
print (list(even))

evenNumbers = filter(lambda x: x%2==0, range(1,21))
print (list(evenNumbers))
