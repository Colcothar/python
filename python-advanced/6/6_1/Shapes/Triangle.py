from . import Util
def perimeter(a,b,c):
	return(a+b+c)
def area(a,b,c):
	s=(a+b+c)/2
	a=s*(s-a)*(s-b)*(s-c)
	return(Util.sqrt(s))
