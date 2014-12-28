import math
a=int(input("Enter the lower limit \n"))
b=int(input("Enter the upper limit \n"))
print("The numbers which are perfect squares and with sum of digits <10:")

l=[x for x in range(a,b+1) if(math.pow(int(math.sqrt(x)),2)==x) and sum(int(i) for i in str(x))<10]

print(l)
