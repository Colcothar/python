import math
def a_c(r):
	return ((math.pi)*(r**2))
def a_r(l,b):
	return (l*b)
def a_t(a,b,c):
	s=(a+b+c)/2
	z=s*(s-a)*(s-b)*(s-c)
	return (z**0.5)
if __name__=="__main__":
	import sys	
	l=sys.argv[1:]
	shape=l[0]
	z=len(l)
	
	try:
		if shape=='circle' and z==2:
			r=float(l[1])
			a=a_c(r)
			print("Area of circle is...%f\n*****************"%a)
		elif shape=='rectangle' and z==3:
			leng=float(l[1])
			breadth=float(l[2])
			a=a_r(leng,breadth)
			print("Area of rectangle is...%f\n*****************"%a)
		elif shape=='triangle' and z==4:
			sa=float(l[1])
			sb=float(l[2])
			sc=float(l[3])
			a=a_t(sa,sb,sc)
			print("Area of triangle is...%f\n*****************"%a)
		else:
			raise Exception()	
	except:
		if (shape=='circle' and z<2) or (shape=='rectangle' and z<3) or (shape=='triangle' and z<4):
					print("arguments missing")		
		else:
					print("too many arguments passed")
