class City:
	
	def __init__(self, city, *places) :
		self.city = city
		self.places = list(places)
	
	def add_place(self, place) :
		self.places.append(place)
	
	def remove_place(self, place) :
		try :
			self.places.remove(place)
		except ValueError :
			print(str(place),'NOT PRESENT !\n\n')
	
	def display_places(self) :
		print('City : ', str(self.city))
		if len(self.places) != 0 :
			print("Welcome to  "+str(self.city)+"  The list of places which you can see are as follows")
			for i in self.places :
				print('\t', i)	
		else :
			print('No Places were there in the city '+str(self.city)+'\n')
while(1):	
        a=int(input("Enter: 1 To add city name . 2 exit \n "))
        if(a==1):
                d1=str(input("Enter the city name : "))
                c1 = City(d1)
                while(1):
                        b=int(input("Enter 1 to add places 2 to remove places  3 To Display Places  4 Stop adding places"))
                        if(b==1):
                                d2=str(input("Enter the location name for "+ str(d1) + " :"))
                                c1.add_place(d2)
                        elif(b==2):
                                d4=str(input("Enter the place to remove from " +str(d1) +" : "))
                                c1.remove_place(d4)
                        elif(b==3):
                                c1.display_places()
                        elif(b==4):
                                break
  
        
        elif(a==2):
                break


print("This is it")
