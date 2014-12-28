date = input("Enter a date in the form dd-mm-yyyy : ")
date1=date.split('-')
d=int(date1[0])
m=int(date1[1])
y=int(date1[2])
if(d>0 and d<=31 and m>0 and m<12 and y>0):
	if(y%4!=0 and m==2 and d>28):
		print("Invalid Feb")
	elif((y%4==0 and y%100!=0) or y%400==0):
		print("Leap year")
	else:
		print("Not a leap year")
else:
	print("Invalid date")
