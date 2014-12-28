import Area


while(True):
	ch=int(input("Enter choice for area to be calculated...:\n1>Circle\n2>Rectangle\n3>Triangle\n4>Exit"))
	if(ch==1):
		r=float(input("Enter the radius..."))
		a=Area.a_c(r)
		print("area of circle of radius %f is %f\n*******************"%(r,a))
	elif(ch==2):
		l=float(input("Enter the length..."))
		b=float(input("Enter the breadth..."))			
		a=Area.a_r(l,b)
		print("area of rectangle of length %f and breadth %f is %f\n*******************"%(l,b,a))
	elif(ch==3):
		sa=float(input("Enter the side 1..."))
		sb=float(input("Enter the side 2..."))			
		sc=float(input("Enter the side 3..."))
		x=Area.a_t(sa,sb,sc)
		print("area of rectangle of sides %f,%f and %f is %f\n*******************"%(sa,sb,sc,x))
	else:
		print("***********end of program************")		
		break

