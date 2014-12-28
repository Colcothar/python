from Shapes import *
while 1:
	ch=int(input("Enter ur choice:\n1=>Circle\t2=>Square\t3=>Triangle\t4=>Exit\n"))
	if(ch==1):
		radius=float(input("Enter r,radius for circle:"))
		print("Area of circle is.. %f"%(Circle.area(radius)))
		print("Perimeter of circle is.. %f"%(Circle.circumference(radius)))	
	elif(ch==2):
		side=float(input("Enter s,side of square.."))
		print("Area of square is..%f"%(Square.area(side)))	
		print("Perimeter of square is..%f"%(Square.perimeter(side)))
	elif(ch==3):
		a=float(input("Enter a side for triangle:"))
		b=float(input("Enter another side for triangle:"))
		c=float(input("Enter another side for triangle:"))
		print("Area of triangle is..%f"%(Triangle.area(a,b,c)))
		print("Perimeter of triangle is..%f"%(Triangle.perimeter(a,b,c)))
	elif(ch==4):
		break
