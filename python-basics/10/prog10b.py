import threading
list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
class MyThread(threading.Thread):
	def __init__(self,low,high):
		threading.Thread.__init__(self)
		self.low=low
		self.high=high
		self.total=0
	def run(self):
		for i in range(self.low,(self.high)):
			self.total += list1[i]

j=0
k=4
sum=0
for i in range(0,4):
	th = MyThread(j,k)
	th.start()
	th.join()
	sum += th.total
	print ('Thread :',i,'->',th.total)
	j=k
	k=k+4
print('Sum ->',sum)
