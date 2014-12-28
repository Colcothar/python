x=int(input("Enter the num whose powers are to be found..."))
n=int(input("Enter the range uptil which powers are to be found..."))
s=[(lambda x,y:x**y)(x,y) for y in range(1,n+1)]
print(s)






		
